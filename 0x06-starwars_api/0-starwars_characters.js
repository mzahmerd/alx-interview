#!/usr/bin/node
const request=require ('request')

const charachters = []
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}` , (err, res, body) => {
    if (err) return console.log(err)
    if (res&&res.statusCode) {
        const charactersApi = JSON.parse(body).characters
        charactersApi.map(charApi => request(charApi, (err, res, data) => console.log(JSON.parse(data).name)))
    }
})

