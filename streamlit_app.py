import streamlit as st # 1.40.2
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
    # Check if the path starts with http:// or https://
    parsed = urlparse(path)
    return bool(parsed.scheme) and parsed.scheme in ["http", "https"]

# Function to resize images to specific width and height
def resize_image(image, new_width=300, new_height=200):
    resized_image = image.resize((new_width, new_height))  # Resize both width and height
    return resized_image

# Function to load project data from metadata files
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
                        
                        # Check if thumbnail is a URL or a local path
                        if is_url(metadata["thumbnail"]):
                            # Fetch and resize the image if it's from a URL
                            response = requests.get(metadata["thumbnail"])
                            if response.status_code == 200:
                                image = Image.open(BytesIO(response.content))
                                resized_image = resize_image(image)  # Resize image
                                # Save the resized image to a buffer and set it as the thumbnail
                                buffer = BytesIO()
                                resized_image.save(buffer, format="PNG")  # Ensure it's saved as PNG
                                buffer.seek(0)  # Seek back to the start of the buffer
                                metadata["thumbnail"] = buffer
                            else:
                                st.error(f"Failed to load image from URL: {metadata['thumbnail']}")
                        else:
                            # Handle local images, resize them
                            local_thumbnail_path = os.path.join(project_path, metadata["thumbnail"])
                            if os.path.exists(local_thumbnail_path):
                                image = Image.open(local_thumbnail_path)
                                resized_image = resize_image(image)  # Resize image
                                buffer = BytesIO()
                                resized_image.save(buffer, format="PNG")  # Ensure it's saved as PNG
                                buffer.seek(0)  # Seek back to the start of the buffer
                                metadata["thumbnail"] = buffer
                            else:
                                st.error(f"Local thumbnail not found: {local_thumbnail_path}")
                        
                        metadata["base_path"] = project_path  # Base path for relative links
                        projects.append(metadata)
                except json.JSONDecodeError:
                    st.error(f"Error parsing JSON in {metadata_path}.")
                except Exception as e:
                    st.error(f"Error loading metadata from {metadata_path}: {e}")
    return projects

# Function to fix paths (can be used independently)
def fix_path(base_path, match):
    relative_path = match.group(1)

    # Skip absolute URLs (HTTP/HTTPS)
    if relative_path.startswith("http://") or relative_path.startswith("https://"):
        return match.group(0)

    # Normalize paths
    normalized_relative_path = os.path.normpath(relative_path).replace("\\", "/")

    # Check if the relative path is root-relative (starts with "/")
    if normalized_relative_path.startswith("/"):
        # For root-relative paths, join them with the base path
        resolved_path = os.path.normpath(os.path.join(base_path, normalized_relative_path[1:])).replace("\\", "/")
    else:
        # For normal relative paths, we join them with base_path
        resolved_path = os.path.normpath(os.path.join(base_path, normalized_relative_path)).replace("\\", "/")

    return match.group(0).replace(relative_path, resolved_path)


# Function to preprocess README.md content
def preprocess_readme(content, base_path):
    # Regex patterns for Markdown images and links
    image_pattern = r"!\[.*?\]\((.*?)\)"  # Matches ![alt](path)
    link_pattern = r"\[.*?\]\((.*?)\)"    # Matches [text](path)

    # Normalize base_path for comparison (ensure consistent slashes)
    normalized_base_path = os.path.normpath(base_path).replace("\\", "/")

    # Apply fixes to both image and link paths
    content = re.sub(image_pattern, lambda match: fix_path(normalized_base_path, match), content)
    content = re.sub(link_pattern, lambda match: fix_path(normalized_base_path, match), content)
    
    return content


# Function to fetch README from URL
def fetch_readme_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request fails
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching README from URL: {e}")
        return None


# Load project data
projects = load_projects(project_dir)

# Check if any projects were loaded
if not projects:
    st.write("No projects found. Please check your directory and metadata files.")

# State to track which project to display
if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

# Function to go back to the project grid
def go_back():
    st.session_state["selected_project"] = None

# Main UI
if st.session_state["selected_project"] is None:
    # Display project grid
    cols_per_row = 2
    rows = (len(projects) + cols_per_row - 1) // cols_per_row  # Efficient rows calculation
    columns = [st.columns(cols_per_row) for _ in range(rows)]

    for idx, project in enumerate(projects):
        row = idx // cols_per_row
        col = idx % cols_per_row
        with columns[row][col]:
            with st.container():  # Use container to ensure consistent height
                # Display the resized thumbnail image
                image_data = project["thumbnail"]
                image = Image.open(image_data)
                resized_image = resize_image(image)
                st.image(resized_image, width=300)

                # Title and description
                st.markdown(f"### {project['title']}")
                st.markdown(project["description"])

                # Ensure the button is at the bottom
                st.write("")  # Adds flexible space

                # Button at the bottom
                if st.button("View Project", key=f"view_project_{idx}"):
                    st.session_state["selected_project"] = project
else:
    # Display the selected project's README.md
    project = st.session_state["selected_project"]

    st.markdown(f"# {project['title']}")
    st.markdown("---")

    readme_content = None

    # Check if the readme is a URL or local path
    if project.get("readme", "").startswith("http://") or project.get("readme", "").startswith("https://"):
        # If the readme is a URL, fetch it
        readme_content = fetch_readme_from_url(project["readme"])
    else:
        # If the readme is a local file, read it
        try:
            with open(project["readme"], "r") as f:
                readme_content = f.read()
        except FileNotFoundError:
            st.error("README.md not found for this project.")

    # If readme_content is fetched or read, process and display
    if readme_content:
        readme_content = preprocess_readme(readme_content, project["base_path"])  # Fix image and link paths
        st.markdown(readme_content, unsafe_allow_html=True)  # Render Markdown with images and links

    # Go back button
    if st.button("Go Back"):
        go_back()
