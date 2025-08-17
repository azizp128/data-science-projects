const button = document.querySelector(".btn");
var resultText = document.querySelector(".result-text");

button.addEventListener("click", function (event) {
  if (resultText.style.visibility == "hidden") {
    resultText.style.visibility = "visible";
  } else {
    resultText.style.visibility = "hidden";
  }
  event.preventDefault();
});
