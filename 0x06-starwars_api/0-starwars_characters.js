#!/usr/bin/node
const request=require('request')

const charachters=[]
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,async (err,res,body) => {
    if(err) {
        return
        // console.log(err)
    } else {
        // const charactersApi=JSON.parse(body).characters
        printCharacter(JSON.parse(body).characters,0)
    }
})

const printCharacter=(charApi,index) => {
    if(index===charApi.length) return
    request(charApi[index],(err,res,data) => {
        if(err) {
            console.log(err)
        } else {
            console.log(JSON.parse(data).name)
            index+=1
            printCharacter(charApi,index)
        }
    })
}