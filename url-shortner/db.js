const mongoose = require('mongoose')
const connectToDb = async () => {
  try {
    const mongoUri = 'mongodb://localhost:27017/url-shortner';

    await mongoose.connect(mongoUri, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });

    console.log('MongoDB connected successfully');
  } catch (err) {
    console.error(' MongoDB connection error:', err);
    process.exit(1); // Exit app if connection fails
  }
};
module.exports = connectToDb

