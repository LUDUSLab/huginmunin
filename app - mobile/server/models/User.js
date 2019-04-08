const mongoose = require("mongoose");
const Schema = mongoose.Schema;
const UserSchema = new Schema({
 nome : {
 type : String,
 required : true
 },
 idade : {
 type : String,
 required : true
 },
 cpf : {
 type : String,
 required : true
 },
 status: {
  type : Boolean,
  required : true
 }
})
const User = mongoose.model("users", UserSchema);
module.exports = User;