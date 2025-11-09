const express = require("express");
const { startBrowser, close, getTabList } = require("../controllers");
const { getActiveTabs } = require("../BroswerService/BrowserService");

const router = express.Router();

router.post("/start", startBrowser);
router.post("/close", close);
router.post("/getTab", getTabList);

module.exports = router;
