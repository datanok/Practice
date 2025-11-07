const express = require('express');
const UserManager = require("./UserManager.ts")
const userManager = new UserManager("Tanmay","tanmay@gmail.com");
const app = express()
const PORT = 3000


console.log(userManager)
app.use(express.json())

app.get('/',(req,res)=>{
    res.send("Hello")
})

app.get('/users',(req,res)=>{
    const userList = userManager.listUsers()
    if (!userList || userList.length < 1) return res.status(404).json({success:false, message:"No Users Found"})
    res.status(200).json({success:true, data:userList})
})

app.get('/user/:id',(req,res)=>{
    const {id} = req.params

    if (!id) return res.status(404).json({success:false, message:"Not valid User ID"})
    const user = userManager.getUser(parseInt(id))
    if(!user) return res.status(404).json({success:false,message:"User Not Found"})
    res.status(200).json({success:true,user})
})

app.post('/user/new',(req,res)=>{
    const {name, email} = req.body
    if(!name || !email) return res.status(400).json({success:false,message:"Please Enter Name and Email"})

 
    const newUser = userManager.addUser(name,email)
    return res.status(201).json({success:true, message:"User Created Successfully",data:newUser})
})

app.put('/users/update/:id',(req,res)=>{
    const {id} = req.params
    const updatedData = req.body
    console.log(req.body,updatedData)
    const updatedUser = userManager.updateUser(parseInt(id),updatedData)
    if(!updatedUser) res.status(400).json({success:false,message:"User not found"})
    res.status(201).json({success:true,message:'User Information Updated',data:updatedUser})
})

app.delete('/user/delete/:id',(req,res)=>{
    const {id} = req.params
    const deletedUser = userManager.deleteUser(parseInt(id))
    if(!deletedUser) return res.status(404).json({success:false,message:"User Not Found"})
    res.status(200).json({success:true,message:"User Deleted Successfully",data:deletedUser})
})

app.delete('/users/deleteAll',(req,res)=>{
    console.log("gi")
    const deletedUsers = userManager.deleteAll()
    res.status(200).json({success:true,message:"All Users Deleted Successfully",count:deletedUsers})
})


app.listen(PORT,()=>{
    console.log(`Running On Port ${PORT}`)
})