#!/usr/bin/env nodejs
const express = require('express');
const helmet = require('helmet');
const fileType = require('file-type');
const multer  = require('multer')
const fs = require('fs');
const app = express();
const accepted_extensions = ['jpg', 'png', 'gif'];

app.use(helmet());

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
      // error first callback
      cb(null, 'uploads/');
  },
  filename: function (req, file, cb) {
      // error first callback
      cb(null, file.fieldname + '-' + Date.now() + '.png') 
  }
});
var upload = multer({ storage, fileFilter: (req, file, cb) => {
  // if the file extension is in our accepted list
  if (accepted_extensions.some(ext => file.originalname.endsWith("." + ext))) return cb(null, true);
  // otherwise, return error
  return cb(new Error('Only ' + accepted_extensions.join(", ") + ' files are allowed!'));
}})

app.get('/', function(req, res){  
  res.send("HEY");
});

app.post('/upload', upload.single('media'), function (req, res, next) {
  res.send("UPLOAD")
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});

