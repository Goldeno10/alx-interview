#!/usr/bin/node
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

async function req (url) {
  request.get(url, (err, resp) => {
    if (err) {
      return;
    }

    if (resp) {
      try {
        const data = JSON.parse(resp.body);
        const chars = data.characters;
        getCharacters(chars);
      } catch (parseError) {
        console.log('Error parsing response body:', parseError);
      }
    }
  });
}

async function getCharacters (chars) {
  for (const item of chars) {
    request.get(item, (err, resp) => {
      if (err) {
        return;
      }
      if (resp) {
        try {
          const data = JSON.parse(resp.body);
          console.log(data.name);
        } catch (parseError) {
          console.log('Error parsing response body:', parseError);
        }
      }
    });
  }
}

const movieId = process.argv.slice(2)[0];
try {
  if (Number.isInteger(Number(movieId))) {
    const url = baseUrl + movieId + '/';
    req(url);
  }
} catch (error) {
  console.log('Error : ', error);
}
