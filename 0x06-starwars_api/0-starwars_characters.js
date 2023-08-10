#!/usr/bin/node
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

async function req (url) {
  request.get(url, (err, resp) => {
    if (err) {
      console.log('error: ', err);
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
  // const actors = [];
  for (const item of chars) {
    request.get(item, (err, resp) => {
      if (err) {
        console.log('Error: ', err);
        return;
      }
      if (resp) {
        try {
          const data = JSON.parse(resp.body);
          // actors.push(data.name);
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
    const url = baseUrl + movieId;
    req(url);
  }
} catch (error) {
  console.log('Error : ', error);
}
