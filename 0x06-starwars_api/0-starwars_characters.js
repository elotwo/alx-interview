#!/usr/bin/node
const arg = process.argv.slice(2); // Get arguments after the script name
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg[0]; // Add endpoint from command-line args

request(url, (error, response, body) => {
  if (error) {
    console.error('ERROR:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log('Film not found.');
    return;
  }

  const filmData = JSON.parse(body);

  const characterPromises = filmData.characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          reject(new Error(`Failed to retrieve character data from ${characterUrl}`));
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name); // Resolve with the character's name
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      // Print each character name in the original order
      characterNames.forEach(name => console.log(name));
    })

    .catch(error => {
      console.error('An error occurred:', error);
    });
});
