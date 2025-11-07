const { BrowserManger } = require("./BrowerManger")

const express = require('express')
const app  = express()
const PORT = 8000

app.use(express.json())



app.listen(PORT,()=>{
    console.log(`Listening on port ${PORT}`)
})

