const mongoose = require('mongoose')

const urlSchema = new mongoose.Schema({
    shortUrl: {
        type: String,
        unique: true,
    },
    longUrl:{
        type: String,
        required: true
    },
    visitHistory:[
        {
            timeStamp:{type : Date, default:Date.now()},
        }
    ]
})

const UrlModel = mongoose.model("Urls",urlSchema)

module.exports = {UrlModel}
