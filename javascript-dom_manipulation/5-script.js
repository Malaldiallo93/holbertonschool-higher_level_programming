// Select the element with id "update_header" using document.querySelector
const updateHeaderElement = document.querySelector('#update_header');
const headerElement = document.querySelector('header');
updateHeaderElement.addEventListener('click', function() {
  headerElement.textContent = 'New Header!!!';
});