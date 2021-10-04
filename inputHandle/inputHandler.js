const Joi = require('joi');
const { clients } = require('../models/clients');

//input validation handler
module.exports.validateClient = (client) => {
    //validate object
    const schema = Joi.object({
        fullName: Joi.string().min(1).max(40).required().pattern(new RegExp('^[A-Za-z ]+$')),
        id: Joi.number().integer().required(),
        phoneNumber: Joi.string().min(1).required().length(14),
        ipAddress: Joi.string().min(1).required().pattern(new RegExp('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')),
    })
    return schema.validate(client)
}
module.exports.validate_id = (id) => {
    let arr_1_2 = []
    for (var i = 0; i < id.length; i++) {
        if (i % 2 == 0)
            arr_1_2[i] = 1;
        else
            arr_1_2[i] = 2;
    }

    let arrAns = [];
    for (var i = 0; i < id.length; i++) {
        arrAns[i] = arr_1_2[i] * parseInt(id.charAt(i));
        if (arrAns[i] > 9) {
            var temp = arrAns[i].toString();
            var a = parseInt(temp.charAt(0));
            var b = parseInt(temp.charAt(1));
            arrAns[i] = a + b;
        }
    }

    var sum = 0;
    for (var i = 0; i < id.length; i++) {
        sum += arrAns[i];
    }
    if (sum % 10 == 0) return false;
    else return true;
}