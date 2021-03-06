#!/usr/bin/env nodejs
const express = require('express');
const fs = require('fs');
const helmet = require('helmet');
const multer  = require('multer')
const app = express();
const rp = require('request-promise');
const accepted_extensions = ['jpg', 'png', 'gif'];
const cameraIp = 'http://localhost:5000/'
app.use(helmet());

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
      // error first callback
      cb(null, 'uploads/');
  },
  filename: function (req, file, cb) {
      // error first callback
      lastPhoto = 'media-'+Date.now() + '.png'
      cb(null, lastPhoto)
  }
});
var upload = multer({ storage, fileFilter: (req, file, cb) => {
  // if the file extension is in our accepted list
  if (accepted_extensions.some(ext => file.originalname.endsWith("." + ext))) return cb(null, true);
  // otherwise, return error
  return cb(new Error('Only ' + accepted_extensions.join(", ") + ' files are allowed!'));
}})

app.get('/', function(req, res){
  console.log('Entrou!')
  res.send(200, "HEY");
});

app.post('/upload', upload.single('media'), function (req, res, next) {
  res.send("UPLOAD")
})

app.get('/lastphoto', function (req, res, next) {
  var files = fs.readdirSync('./uploads');
  var last = files.length-1
  res.sendFile(files[last], {root:'./uploads'})
})

app.get('/animate/:anim', function(req, res){  
    rp(cameraIp + req.params.anim).then(function (res) {
      console.log(res);
    })
    .catch(function (err) {
      console.log(err.statusCode);
    });
    res.send('animate')
});

app.listen(8000, function () {
  console.log('Example app listening on port 8000!');
});

