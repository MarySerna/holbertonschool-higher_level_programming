const $ = window.$;
// Semistandart sucks
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(res => res.json())
    .then(res => {
        // console.log(res.results);
        res.results.forEach(film => {
            // console.log(film.title)
            $('UL#list_movies').append(`<li>${film.title}</li>`);
        });
    });
