// Select the element with id "red_header" using document.querySelector
const redHeaderElement = document.querySelector('#red_header');

// Add a click event listener to the "red_header" element
redHeaderElement.addEventListener('click', function() {
  // Select the header element using document.querySelector
  const headerElement = document.querySelector('header');
  
  // Update the text color to red (#FF0000)
  headerElement.style.color = '#FF0000';
});
