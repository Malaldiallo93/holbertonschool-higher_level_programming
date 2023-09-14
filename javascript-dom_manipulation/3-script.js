// Select the element with id "toggle_header" using document.querySelector
const toggleHeaderElement = document.querySelector('#toggle_header');
const headerElement = document.querySelector('header');
toggleHeaderElement.addEventListener('click', function() {
  if (headerElement.classList.contains('red')) {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
