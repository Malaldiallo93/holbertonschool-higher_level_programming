// Select the element with id "red_header" using document.querySelector
const redHeaderElement = document.querySelector('#red_header');
redHeaderElement.addEventListener('click', function() {
  const headerElement = document.querySelector('header');
  headerElement.classList.add('red');
});
