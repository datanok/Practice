const BrowserSevice = require("../BroswerService/BrowserService");

exports.startBrowser = async (req, res, next) => {
  try {
    const { browser, url } = req.body;
    console.log(req.body);
    await BrowserSevice.startBrowser(browser, url);
    res.status(200).json({ message: "Broswer Openmed" });
  } catch (err) {
    next(err);
  }
};
exports.close = async (req, res, next) => {
  try {
    const { browser } = req.body;
    console.log(req.body);
    await BrowserSevice.closeBrowser(browser);
    res.status(200).json({ message: "Broswer Closed" });
  } catch (err) {
    next(err);
  }
};
exports.getTabList = async (req, res, next) => {
  try {
    const { browser } = req.body;
    console.log(req.body);
    const data = await BrowserSevice.getActiveTabs(browser);
    console.log(data);
    res.status(200).json({ data });
  } catch (err) {
    next(err);
  }
};
