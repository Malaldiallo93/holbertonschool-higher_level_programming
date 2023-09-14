// Select the element with id "character" using document.querySelector
const characterElement = document.querySelector('#character');
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Use the Fetch API to make a GET request to the API endpoint
fetch(apiUrl)
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Failed to fetch data');
    }
  })
  .then(data => {
    const characterName = data.name;
    characterElement.textContent = characterName;
  })
  .catch(error => {
    console.error('Error:', error);
  });