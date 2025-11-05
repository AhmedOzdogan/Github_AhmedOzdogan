// server.js
const express = require("express");
const mongoose = require("mongoose");
const { getWeatherData, getForecastData, getWeatherDataAll } = require("./api");

const app = express();
const port = 3000;

// Middleware
app.use(express.json());

// MongoDB connection
mongoose
  .connect("mongodb://localhost:27017/weatherdata", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("✅ MongoDB connected"))
  .catch((err) => console.error("MongoDB connection error:", err));

// ----------- Routes -----------
app.get("/", (req, res) => {
  res.send("Weather API is running 🌦️");
});

app.get("/weather/all", async (req, res) => {
  try {
    const data = await getWeatherDataAll();
    res.json(data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to fetch all weather data" });
  }
});

app.get("/weather", async (req, res) => {
  const city = req.query.city;
  try {
    const data = await getWeatherData(city);
    res.json(data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to fetch weather data" });
  }
});

app.get("/forecast", async (req, res) => {
  const city = req.query.city;
  try {
    const data = await getForecastData(city);
    res.json(data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to fetch forecast data" });
  }
});

// ----------- Start Server -----------
app.listen(port, () => {
  console.log(`🚀 Server is running at http://localhost:${port}`);
});
