var express = require('express');
const fs = require('fs')
var server= express();
server.listen(8050);
server.get('/index.html', function(request, response) {
  response.sendFile('./index.html');
});

let personne = {
    "prenom" : "djouher",
    "age" : 45,
    "passion" : " créatifs, histoire",
    "taille" : 172
 }
  
 let donnees = JSON.stringify(personne)
 fs.appendFile("teste.json", donnees, (err) => {
    if (err) {
      console.log(err);
    }
})

