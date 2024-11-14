#!/usr/bin/node
const arg = process.argv.slice(2)
const request = require("request")
let url = 'https://swapi-api.alx-tools.com/api/films/' + arg[0];
request(url, (error, response, body) => {
	if (error) console.log(error)

	console.log(response.statusCode);

	const filmdata = JSON.parse(body)
	
	filmdata.characters.forEACH(characterurl => {
		request(characterurl, (error, response, body) => {
			if (!error && response.statusCode === 200) {
				const characterData = JSON.parse(body);
				console.log(characterData.name);
			}
		});
	});
});
