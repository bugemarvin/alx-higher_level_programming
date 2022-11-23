/* a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json */
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  $('#list_movies').append(...data.results.map((movie) => `<li>${movie.title}</li>`));
});
