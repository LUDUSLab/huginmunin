const express = require('express');
const bodyParser = require("body-parser");
const mongoose = require('mongoose');
mongoose.Promise = global.Promise;
mongoose.connect("mongodb://localhost:27017/app", {useNewUrlParser: true})
.then(() => console.log("Connected to Mongo"))
// RoutesFile
const approutes = require('./routes/app-routes');
const app = express();
//Bodyparser Middleware
app.use(bodyParser.json());
//Routes Middleware
app.use("/app", approutes)
//Port
const port = 5000 || process.env.PORT;
app.listen(port, () => console.log(`Listen to the port of ${port}`))