// Function to fetch and display the translation
function fetchAndDisplayTranslation() {
    const helloElement = document.querySelector('#hello');
  
    // URL for fetching the translation
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch translation');
        }
        return response.json();
      })
      .then(data => {
        const translation = data.hello;
        helloElement.textContent = translation;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
  fetchAndDisplayTranslation();