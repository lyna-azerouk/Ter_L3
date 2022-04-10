/* var express = require('express');
const fs = require('fs')
var server= express();
server.listen(8333);
server.post('/macarte.html', function(request, response) {
let donnees = JSON.stringify(request.body.button)
 fs.appendFile("teste.json", donnees, (err) => {
    if (err) {
      console.log(err);
    }
})
}); */
let express = require('express')
let app = express()
let server = require('http').Server(app)
let bodyParser = require('body-parser')
let fs = require("fs")
let xml2js = require("xml2js")
 
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
 
app.get('/', (req, res) => {
    res.render('index')
})
 
app.post('/form-handling', (req, res)=>{
    let builder = new xml2js.Builder()
    let xml = builder.buildObject(req.body)
 
    fs.writeFile("file.xml", xml, function(err, data) {
        if (err) console.log(err)
        console.log("successfully written our xml to file")
        res.send(true)
    });
})

server.listen('8080', ()=>{
    console.log(`Server listening on port 8080`)
})

 

