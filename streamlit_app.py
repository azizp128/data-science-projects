import streamlit as st
import os
import json
import re
import requests
from urllib.parse import urlparse
from PIL import Image
from io import BytesIO

# Define the directory containing project folders
project_dir = "./"  # Replace with the correct path


def is_url(path):
    parsed = urlparse(path)
    return bool(parsed.scheme) and parsed.scheme in ["http", "https"]


def resize_image(image, new_width=330, new_height=200):
    resized_image = image.resize((new_width, new_height))  # Resize both width and height
    return resized_image


def load_projects(directory):
    projects = []
    if not os.path.isdir(directory):
        st.error(f"Directory does not exist: {directory}")
        return projects

    for folder in os.listdir(directory):
        project_path = os.path.join(directory, folder)
        if os.path.isdir(project_path):
            metadata_path = os.path.join(project_path, "project-info.json")
            if os.path.exists(metadata_path):
                try:
                    with open(metadata_path, "r") as f:
                        metadata = json.load(f)
                        
                        if "category" not in metadata:
                            metadata["category"] = "uncategorized"  # Default to uncategorized if not found

                        # Process the thumbnail URL or local image as before
                        if is_url(metadata["thumbnail"]):
                            response = requests.get(metadata["thumbnail"])
                            if response.status_code == 200:
                                image = Image.open(BytesIO(response.content))
                                resized_image = resize_image(image)
                                buffer = BytesIO()
                                resized_image.save(buffer, format="PNG")
                                buffer.seek(0)
                                metadata["thumbnail"] = buffer
                            else:
                                st.error(f"Failed to load image from URL: {metadata['thumbnail']}")
                        else:
                            local_thumbnail_path = os.path.join(project_path, metadata["thumbnail"])
                            if os.path.exists(local_thumbnail_path):
                                image = Image.open(local_thumbnail_path)
                                resized_image = resize_image(image)
                                buffer = BytesIO()
                                resized_image.save(buffer, format="PNG")
                                buffer.seek(0)
                                metadata["thumbnail"] = buffer
                            else:
                                st.error(f"Local thumbnail not found: {local_thumbnail_path}")
                        
                        metadata["base_path"] = project_path
                        projects.append(metadata)
                except json.JSONDecodeError:
                    st.error(f"Error parsing JSON in {metadata_path}.")
                except Exception as e:
                    st.error(f"Error loading metadata from {metadata_path}: {e}")
    return projects


def fix_path(base_path, match):
    relative_path = match.group(1)

    if relative_path.startswith("http://") or relative_path.startswith("https://"):
        return match.group(0)

    normalized_relative_path = os.path.normpath(relative_path).replace("\\", "/")

    if normalized_relative_path.startswith("/"):
        resolved_path = os.path.normpath(os.path.join(base_path, normalized_relative_path[1:])).replace("\\", "/")
    else:
        resolved_path = os.path.normpath(os.path.join(base_path, normalized_relative_path)).replace("\\", "/")

    return match.group(0).replace(relative_path, resolved_path)


def preprocess_readme(content, base_path):
    image_pattern = r"!\[.*?\]\((.*?)\)"
    link_pattern = r"\[.*?\]\((.*?)\)"

    normalized_base_path = os.path.normpath(base_path).replace("\\", "/")

    content = re.sub(image_pattern, lambda match: fix_path(normalized_base_path, match), content)
    content = re.sub(link_pattern, lambda match: fix_path(normalized_base_path, match), content)
    
    return content


def fetch_readme_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching README from URL: {e}")
        return None


# Load project data
projects = load_projects(project_dir)

# Sidebar for category selection
categories = list(set([project["category"] for project in projects]))  # Get unique categories
selected_category = st.sidebar.selectbox("Select a Category", ["All"] + categories)

# Filter projects based on the selected category
if selected_category != "All":
    filtered_projects = [project for project in projects if project["category"] == selected_category]
else:
    filtered_projects = projects

# Check if any projects were loaded after filtering
if not filtered_projects:
    st.write("No projects found. Please check your directory and metadata files.")

# State to track which project to display
if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

def go_back():
    st.session_state["selected_project"] = None


# Main UI
if st.session_state["selected_project"] is None:
    # Display project grid
    cols_per_row = 2
    rows = (len(filtered_projects) + cols_per_row - 1) // cols_per_row
    columns = [st.columns(cols_per_row) for _ in range(rows)]

    for idx, project in enumerate(filtered_projects):
        row = idx // cols_per_row
        col = idx % cols_per_row
        with columns[row][col]:
            with st.container(border=True, height=600):
                image_data = project["thumbnail"]
                image = Image.open(image_data)
                resized_image = resize_image(image)
                st.image(resized_image, width=330.5)

                st.markdown(f"### {project['title']}")
                st.markdown(project["description"])

                if st.button("View Project", key=f"view_project_{idx}", use_container_width=True):
                    st.session_state["selected_project"] = project
else:
    # Display the selected project's README.md
    project = st.session_state["selected_project"]

    st.markdown(f"# {project['title']}")
    st.markdown("---")

    readme_content = None

    if project.get("readme", "").startswith("http://") or project.get("readme", "").startswith("https://"):
        readme_content = fetch_readme_from_url(project["readme"])
    else:
        try:
            with open(project["readme"], "r") as f:
                readme_content = f.read()
        except FileNotFoundError:
            st.error("README.md not found for this project.")

    if readme_content:
        readme_content = preprocess_readme(readme_content, project["base_path"])
        st.markdown(readme_content, unsafe_allow_html=True)

    if st.button("Go Back"):
        go_back()
