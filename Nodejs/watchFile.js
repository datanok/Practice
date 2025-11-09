const fs = require('fs')

function watchFileForChanges(file,onNewLines,interval = 1000){

    let lastSize = 0
    fs.stat(file,(err,stats)=>{
        lastSize = stats.size

    })

    setInterval(()=>{
        fs.stat(file,(err,stats)=>{
        const newSize = stats.size


        if(newSize>lastSize){
            const stream  = fs.createReadStream(file,{start:lastSize,end:newSize})
            let buffer = ''

            stream.on('data',chunk=>(buffer = buffer + chunk))

            stream.on('end',()=>{
                const newLines = buffer.split('\n').filter(Boolean)
                if (newLines.length > 0) onNewLines(newLines);
          lastSize = newSize;
            })
        }

    })
    },interval)

}

function onNewLines (lines){
    console.log(lines)
}

watchFileForChanges('logs.txt',onNewLines)