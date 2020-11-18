const bodyParser = require('body-parser')
const express = require('express')
const app = express()
const fs = require("fs")
const pathToJSONFile = 'js/dados.json';

app.use(express.static('.'))
app.use(bodyParser.urlencoded({extended: true}))
app.use(bodyParser.json())

const multer = require('multer')

const storage = multer.diskStorage({
    destination: function (req, file, callback){
        callback(null, './upload')
    },
    filename: function (req, file, callback){
        callback(null, `${Date.now()}_${file.originalname}`)
    }
})

app.post('/formulario', (req, res) => {
    // Estou retornando isso pro front end
    console.log(req.body)
    res.send({
        ...req.body,
        id: 1
    })
    let myData = JSON.stringify(req.body)
    

    fs.writeFileSync(pathToJSONFile, myData); //default: 'utf8'

})

app.listen(3002, ()=> console.log('Executando...'))