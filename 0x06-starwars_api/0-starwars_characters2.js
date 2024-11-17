#!/usr/bin/node
const arg = process.argv.slice(2); // Get arguments after the script name
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg[0];// Add endpoint from command-line args
request(url, (error, response, body) => {
  if (error) {
	  console.error('ERROR:', error);
	  return;
  }

  if (response.statusCode !== 200) {
	  console.log('Film not found.');
	  return;
  }
  const filmdata = JSON.parse(body);

  filmdata.characters.forEach(characterurl => {
    request(characterurl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
});
