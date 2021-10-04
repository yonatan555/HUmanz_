const express = require('express')
const router = express.Router()
const { clients } = require('../models/clients')
const { validateClient, validate_id } = require('../inputHandle/inputHandler')
var request = require('request')


//for fronted 
router.get('/', (req, res) => {
    res.render('moshe')
})

//get all clients
router.get('/api/clients', (req, res) => {
    clients.find({}, { _id: 0, __v: 0 }, (err, data) => {
        if (!err) {
            res.send(data)
        } else {
            console.log(err);
        }
    })
})

//filter clients
router.get('/api/client', (req, res) => {
    console.log(req.query)
    var queryDB = req.query
    // res.send(req.query)
    clients.find(queryDB, {_id : 0 , __v : 0 }, (err, data) => {
        if (!err) {
            res.send(data)
        } else {
            console.log(err);
        }
    })
})

//Save a new client
router.post('/api/client/add', (req, res) => {
    //  validate that user enter appropite parameters
    const { error_id} = validate_id(req.body.id.toString());
    if(error_id) return res.status(400).send({name : "ID ERROR", message : "NO VALID ID"})
    const { error } = validateClient(req.body);
    if (error) return res.status(400).send(error.details[0].message);
    //create new client'
    let cli = new clients({
        fullName: req.body.fullName,
        id: req.body.id,
        phoneNumber: req.body.phoneNumber,
        ipAddress: req.body.ipAddress,
    });
    const IP = req.body.ipAddress
    let web = 'http://ip-api.com/json/' + IP
    request(web, function (err, resp) {
        if (err) console.log(err.message);
        else {
            var ipInfo = JSON.parse(resp.body)
            cli['city'] = ipInfo.city;
            cli['country'] = ipInfo.country;
            cli.save((err, data) => {
                if (!err) {
                    console.log("Client has saved")
                    res.status(200).json({ code: 200, message: 'client has saved', clients: data })
                } else {
                    res.status(304).json({ code: 304, message: 'Something happend,dont worry nothing is changed', clients: data })
                }
            });
        }
    })
});
//Delete a client by id(TEUDAT ZEHOT)
router.delete('/api/client/:id', (req, res) => {
    clients.findOneAndRemove({ id: req.params.id }, (err, data) => {
        if (!err) { res.status(200).json({ code: 200, message: "Client Has Deleted Successfully", deleteClient: data }) }
    })
})


module.exports = router;