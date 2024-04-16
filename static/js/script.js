console.log("Hello World!");

function copyToClipboard(text) {
  // Create a temporary input element
  var tempInput = document.createElement("input");

  // Set the value of the input to the text to be copied
  tempInput.value = text;

  // Append the input to the body
  document.body.appendChild(tempInput);

  // Select the text in the input
  tempInput.select();

  // Copy the selected text to the clipboard
  document.execCommand("copy");

  // Remove the temporary input
  document.body.removeChild(tempInput);

  // Optionally, provide feedback to the user
  alert("URL copied to clipboard: " + text);
}
