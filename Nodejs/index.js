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


// const readerStream  = fs.createReadStream(filePath,{ encoding: "utf8", highWaterMark: 32 })
// const writeStream  = fs.createWriteStream("output.txt")
// readerStream.pipe(writeStream)
// readerStream.on("end",()=>{
//    console.log("file end")
// })

// setInterval(()=>{
//    const log = `${new Date} \n`
// fs.appendFile('logs.txt',log,(err)=>{
//    if (err) console.log(err)
//    else{
// console.log("logged")}
// })
// },1000)

// fs.stat('logs.txt',(err,stats)=>{
//    if(err )throw err

//    const size  = stats.size
//    const readSize = 100
//    const start = stats.size - readSize
//    const stream  = fs.createReadStream('logs.txt',{start:start,end:size-1,encoding:"utf-8"})
//    console.log(`Reading last ${readSize} bytes...`);
//   stream.pipe(process.stdout);
// })
// reader.on('data',(chunk)=>{
//    console.log("\n--- New Chunk ---");
//    reader.pause()
//    setTimeout(()=>{
//       console.log("resuming")
//       reader.resume()
//    },2000)
//    console.log(chunk.toString())
// })


// let lastSize = 0;

// setInterval(() => {
//   fs.stat('logs.txt', (err, stats) => {
//     if (err) return;
//     const newSize = stats.size;

//     // file grew
//     if (newSize > lastSize) {
//       const stream = fs.createReadStream(filePath, {
//         start: lastSize,
//         end: newSize - 1,
//         encoding: "utf8",
//       });

//       stream.on("data", chunk => process.stdout.write(chunk));
//       stream.on("end", () => {
//         lastSize = newSize; // update our pointer
//       });
//     }

//     // file got truncated (rotated)
//     if (newSize < lastSize) {
//       console.log("[File truncated — resetting]");
//       lastSize = 0;
//     }
//   });
// }, 1000);


// async function readLastNlines(file,n){
//    const data = await fs.promises.readFile(file,"utf-8")

//    const lines = data.trimEnd().split('\n')
//    console.log(lines.slice(-n),";ines")

// }

// readLastNlines('logs.txt',2)
// readLastNLines-large.js
// async function readLastNline(filePath,n){
//    const data = await fs.promises.readFile(filePath,"utf-8")

//    const lines  = data.trimEnd().split('\n')
   
//    console.log(lines.splice(-n))
// }
// async function readLastNLines(filePath, n) {
//   const CHUNK_SIZE = 64 * 1024; // 64 KB per read
//   const NEWLINE = 0x0a; // '\n' byte
//   const fd = await fs.promises.open(filePath, "r");
//   const stat = await fd.stat();
//   const fileSize = stat.size;

//   let position = fileSize;
//   let lines = [];
//   let leftover = "";

//   while (lines.length <= n && position > 0) {
//     // Move back by chunk size (or to 0)
//     console.log(position,"position")
//     const bytesToRead = Math.min(CHUNK_SIZE, position);
//     console.log(bytesToRead)
//     position -= bytesToRead;
//      console.log(position,"position")

//     // Allocate buffer for chunk
//     const buffer = Buffer.alloc(bytesToRead);
//     const { bytesRead } = await fd.read(buffer, 0, bytesToRead, position);

//     // Convert chunk to string and prepend leftover
//     const chunkText = buffer.slice(0, bytesRead).toString("utf8") + leftover;
//     console.log(chunkText,"chunkText")
//     console.log(leftover,"leftover")
//     const chunkLines = chunkText.split(/\r?\n/);
//     console.log(chunkLines,"chunkLines")

//     // Keep first element as new leftover (incomplete line at chunk boundary)
//     leftover = chunkLines.shift();

//     // Prepend to total lines
//     lines = chunkLines.concat(lines);

//     // Stop when we have enough
//     if (lines.length >= n) break;
//   }

//   await fd.close();

//   // Combine leftover (start of file if any)
//   if (leftover) lines.unshift(leftover);

//   // Return only last n
//   const cleanLines = lines;
// if (cleanLines.length && cleanLines[cleanLines.length - 1] === "") {
//   cleanLines.pop(); // remove trailing empty line
// }
// return cleanLines.slice(-n);
// }

// Example usage:
// (async () => {
//   const lines = await readLastNLines("logs.txt", 10);
//   console.log(lines.join("\n"));
// })();


// process the file in chunks
//start fromt the end and count how many new lines chars we get and then stop



async function readLastNLines(filePath, n) {
  const CHUNK_SIZE = 64 * 1024; // 64 KB per read
  const fd = await fs.promises.open(filePath, "r");
  const stat = await fd.stat();
  const fileSize = stat.size;

  let position = fileSize;
  let lines = [];
  let leftover = "";

  while (lines.length <= n ) {
    // Move back by chunk size (or to 0)
    const bytesToRead = Math.min(CHUNK_SIZE, position);
    position -= bytesToRead;

    // Allocate buffer for chunk
    const buffer = Buffer.alloc(bytesToRead);
    const { bytesRead } = await fd.read(buffer, 0, bytesToRead, position);

    // Convert chunk to string and prepend leftover
    const chunkText = buffer.toString("utf8",0,bytesRead) + leftover;
    const chunkLines = chunkText.trimEnd().split(/\r?\n/);

    // Keep first element as new leftover (incomplete line at chunk boundary)
    leftover = chunkLines.shift();

    // Prepend to total lines
    lines = chunkLines.concat(lines);

    // Stop when we have enough
    if (lines.length > n) break;
  }

  await fd.close();

  // Combine leftover (start of file if any)
  if (leftover) lines.unshift(leftover);

  // Return only last n
  return lines.slice(-n);
}

// Example usage:
(async () => {
  const lines = await readLastNLines("logs.txt", 2);
  console.log(lines.join("\n"));
})();
