const { default: axios } = require("axios");
const { exec } = require("child_process");
const { platform } = require("os");

const buildStartCmd = (browser, url) => {
  const os = platform();
  console.log(os);
  switch (os) {
    case "aix":
    case "android":

    case "darwin":
    case "freebsd":
    case "haiku":
    case "linux":
    case "openbsd":
    case "sunos":
    case "win32":
      return `start ${browser} ${url}`;
    case "cygwin":
    case "netbsd":
    default:
      return `start ${browser} ${url}`;
  }
};
class BrowserSevice {
  static async startBrowser(browser, url) {
    if (!browser || !url) throw new Error("Browser and Url required");

    return new Promise((resolve, reject) => {
      exec(buildStartCmd(browser, url), (err, stdout, stderr) => {
        if (err) reject("Something went wrong", err);
        if (stderr) console.error("stderr", stderr);
        resolve(stdout);
      });
    });
  }

  static async closeBrowser(browser) {
    if (!browser) throw new Error("Browser required");
    const cmd = `taskkill /F /IM ${browser}.exe`;
    return new Promise((resolve, reject) => {
      exec(cmd, (err, stdout, stderr) => {
        if (err) reject("Something went wrong", err);
        if (stderr) console.error("stderr", stderr);
        resolve(stdout);
      });
    });
  }
  static async getActiveTabs(browser) {
    if (!browser) throw new Error("Browser required");
    let activeTab;
    try {
      const { data } = await axios.get("http://localhost:9222/json");

      activeTab = data.find((tab) => tab.type === "page");
    } catch (err) {
      console.log(err);
    }
    return new Promise((resolve, reject) => {
      resolve(activeTab);
    });
  }
}

module.exports = BrowserSevice;
