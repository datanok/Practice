const express = require('express')
const { handleShorten, getUrl, getAnalytics } = require('./controllers/urlController')
const connectToDb = require('./db')
const app = express()

app.use(express.json())
const PORT = 8000

app.post('/shorten',handleShorten)
app.get('/:shortUrl',getUrl)
app.get('/analytics/:shortUrl',getAnalytics)


connectToDb()

app.listen(PORT,()=>{
    console.log(`Listening on ${PORT}`)
})