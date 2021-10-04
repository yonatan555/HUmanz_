const mongoose = require('mongoose')

const clients = mongoose.model('clients', {
    fullName: {
        type: String,
        required: true
    }, id: {
        type: String,
        required: true
    }, phoneNumber: {
        type: String,
        required: true
    }, ipAddress: {
        type: String,
        required: true
    }, city: {
        type: String,
        required: true
    }, country: {
        type: String,
        required: true
    }
})


module.exports = { clients }