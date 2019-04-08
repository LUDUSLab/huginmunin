const router = require('express').Router();
const User = require("../models/User.js");
router.get("/", (req,res) => {
    User.find({})
    .then(data => res.send(data))
})
router.post("/", (req,res) => {
 User.create(req.body)
 .then(data => res.send(data))
})
router.put("/:id", (req,res) => {
 const id = req.params.id;
 const {nome , idade, cpf, status} = req.body
User.findByIdAndUpdate(id, {$set: { nome, idade, cpf, status}})
 .then(data => {
 User.findById(id)
 .then(data => res.send(data))
 })
})
router.delete("/:id", (req,res) => {
 const id = req.params.id;
User.findByIdAndRemove(id)
 .then(data => {
 res.send("Has Been Deleted")
 })
})
module.exports = router;