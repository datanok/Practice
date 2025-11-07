const {nanoid} = require('nanoid')
const { UrlModel } = require('../models/url')
const handleShorten = async (req, res, next) => {
    const { website } = req.body
    try {
        const newUrl = {
            shortUrl: nanoid(),
            longUrl: website,

        }
        const result = await UrlModel.create(newUrl)

        res.status(201).json({ result })
    } catch (err) {
        console.error(err)
        next()
    }

}

const getUrl = async (req, res) => {
    const {shortUrl} = req.params
    

    const url = await UrlModel.findOneAndUpdate({shortUrl:shortUrl},
        {
        $push:{
            visitHistory:{
                timeStamp:Date.now()
            }
        }
        
    },{new:true})
    if (!url) {
    return res.status(404).json({ error: "URL not found" });
}
   
    res.redirect(url.longUrl)
}
const getAnalytics = async (req, res) => {
    const {shortUrl} = req.params
    

    const url = await UrlModel.findOne({shortUrl:shortUrl})
    if (!url) {
    return res.status(404).json({ error: "URL not found" });
}
 
    await url.save()
    res.status(200).json({visits:url.visitHistory.length})
}

module.exports = { handleShorten, getUrl,getAnalytics }