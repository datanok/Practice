const {exec} = require('child_process')
class BrowserManger {
    constructor(browserName = 'chrome') {
        this.browserName = browserName
    }

    async start(url) {
        console.log(url)
        const cmd = `start ${this.browserName} "${url}"`
        return new Promise((resolve,reject)=>{
            exec(cmd, (err, stdout, stderr) => {
            if (err) {
                reject(err)
                console.error(err)
                return
            }
            if(stderr){
               return console.err(stderr)
            }
            resolve(stdout)
        })
        })
    }
}

module.exports = { BrowserManger }