// Select the <ul> element with id "list_movies" using document.querySelector
const movieListElement = document.querySelector('#list_movies');

// URL of the API endpoint
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    return response.json();
  })
  .then(data => {
    const movies = data.results;
    movies.forEach(movie => {
      const movieTitle = movie.title;
      const listItem = document.createElement('li');
      listItem.textContent = movieTitle;
      movieListElement.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });