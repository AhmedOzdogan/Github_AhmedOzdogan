const mongoose = require("mongoose");

// Connect to MongoDB (database: airbnb)
mongoose
  .connect("mongodb://localhost:27017/airbnb", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('✅ MongoDB connected to "airbnb" database'))
  .catch((err) => console.error("❌ Connection error:", err));

// Define flexible schema (accepts all fields)
const airbnbSchema = new mongoose.Schema(
  {
    _id: String, //  define _id as a String
  },
  { strict: false }
);

// Explicitly set the collection name to "airbnb_data"
module.exports = mongoose.model("Airbnb", airbnbSchema, "airbnb_data");
