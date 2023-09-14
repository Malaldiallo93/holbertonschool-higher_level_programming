// Select the element with id "add_item" using document.querySelector
const addItemElement = document.querySelector('#add_item');
const myListElement = document.querySelector('.my_list');

addItemElement.addEventListener('click', function() {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  myListElement.appendChild(newItem);
});