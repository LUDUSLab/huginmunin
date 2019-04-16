#!/usr/bin/env nodejs
const express = require('express');
const app = express();
const helmet = require('helmet');
app.use(helmet());
const fileUpload = require('express-fileupload');
app.use(fileUpload);

app.get('/', function(req, res){  
  res.send(req);
});

app.post('/upload', function(req, res) {
  console.log(req.files.foo); // the uploaded file object
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});

