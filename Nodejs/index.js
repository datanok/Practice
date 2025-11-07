const { timeEnd } = require('console')
const fs = require('fs')
const path = require('path')
const filePath = path.join(process.cwd(), 'test.txt')

console.time()
// fs.readFile(filePath,'utf-8',(err,data)=>{
//     if(err){
//         console.log(err)
//         return
//     }
//     console.log(data)
//     console.timeEnd()
// })
// const readfileData  = async()=>{
//     console.time()
//     const fileData = await fs.promises.readFile(filePath,"utf-8")
//     console.log(fileData),
//     console.timeEnd()
// }
// readfileData()


// fs.open(filePath,'r',(err,fd)=>{
//     if(err){
//         console.error(err)
//         return
//     }
//     const buffer = Buffer.alloc(50)
//     fs.read(fd,buffer,0,buffer.length,0,(err,bytesread,buffer)=>{
//         if(err){
//             console.log(err)
//             return
//         }
//         console.log(buffer,"buff")
//         console.log(bytesread)
//         console.log('file content',buffer.toString('utf-8',0,bytesread))
//     })

// })

// fs.open(filePath,'r',(err,fd)=>{
//     if(err){
//         console.error("Error while opening File")
//         return
//     }

//     const buffer = Buffer.alloc(50)
//     fs.read(fd,buffer,0,buffer.length, 0,(err,bytesRead)=>{
//         console.log(buffer)
//         console.log("Chunk 1")
//         console.log(buffer.toString('utf-8',0,bytesRead))
//           fs.read(fd,buffer,0,buffer.length,50,(err,bytesRead)=>{
//         console.log("Chunk 2")
//         console.log(bytesRead,"sad")
//         console.log(buffer.toString('utf-8',0,bytesRead))
//     })
//     })

  
// })

// const text = "Hello\nWorld\n";
// const buf = Buffer.from(text, "utf8");
// console.log(buf.length)

// for(let i =0;i<buf.length;i++){
//     console.log(String.fromCharCode(buf[i]))
// }

// fs.readFile(filePath,'utf-8',(err,data)=>{
//     // console.log(data.split('\n').length)
//     const buf = Buffer.from(data, "utf8");

// console.log("Buffer length:", buf.length);
// console.log("String from buffer:", buf.toString());

// let newlineCount = 0;
// for (let i = 0; i < buf.length; i++) {
//   const byte = buf[i];
//   const hex = byte.toString(16).padStart(2, "0");
// //   console.log(`Index ${i}: decimal=${byte}, hex=0x${hex}, char=${String.fromCharCode(byte)}`);
//   if (byte === 0x0a) newlineCount++;
// }
// console.log(`Total newline bytes (0x0a): ${newlineCount}`);
// })

// const text = "Line1\nLine2\r\nLine3\n";
// const buf = Buffer.from(text, "utf8");

// let LF = 0, CR = 0;
// for (let b of buf) {
//   if (b === 0x0a) LF++;
//   if (b === 0x0d) CR++;
// }
// console.log("Buffer bytes:", buf);
// console.log("LF (\\n):", LF, " CR (\\r):", CR);

// function readSlice(start,end){
//     fs.open(filePath,'r',(err,fd)=>{
//         const size = end-start
//         const buffer = Buffer.alloc(size)
//         fs.read(fd,buffer,0,size,start,(err,bytesRead)=>{
//               console.log(`\nSlice [${start}, ${end}) => ${bytesRead} bytes`);
//             console.log(buffer.toString('utf-8',0,bytesRead))
//         })
//     })
// }
// readSlice(0, 50);
// readSlice(50, 100);
// readSlice(100, 150);

// let lastSize = 0;

// setInterval(() => {
//   fs.stat(filePath, (err, stats) => {
//     if (err) return console.error(err);
//     const diff = stats.size - lastSize;
//     if (diff !== 0) {
//       console.log(`[${new Date().toLocaleTimeString()}] Size: ${stats.size} (Δ ${diff})`);
//       lastSize = stats.size;
//     }
//   });
// }, 1000);


const { exec } = require('child_process')
const { BrowserManger } = require('../BroswerManger/BrowerManger')

async function startBrowser(browser,url){
   const browser = new BrowserManger('chrome')
   await browser.start("www.google.com")
}
startBrowser()

