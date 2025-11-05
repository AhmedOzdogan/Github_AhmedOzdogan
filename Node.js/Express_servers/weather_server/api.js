// api.js
const axios = require("axios");
const mongoose = require("mongoose");
const Weather = require("./model");

const BaseURL = "http://localhost:3000";

// API endpoints (optional for external API calls)
const APIEndpoints = {
  getWeather: `${BaseURL}/weather`,
  getForecast: `${BaseURL}/forecast`,
};

// -------- Fetch all weather data --------
async function getWeatherDataAll() {
  try {
    const data = await Weather.find({}).limit(10);
    return data;
  } catch (error) {
    console.error("Error fetching all weather data:", error);
    throw error;
  }
}

// -------- Fetch weather for one city --------
async function getWeatherData(city) {
  try {
    const data = await Weather.findOne({ callLetters: city });
    if (!data) throw new Error(`No weather data found for ${city}`);
    return data;
  } catch (error) {
    console.error("Error fetching weather data:", error);
    throw error;
  }
}

// -------- Fetch forecast data (example external call) --------
async function getForecastData(city) {
  try {
    const response = await axios.get(
      `${APIEndpoints.getForecast}?city=${city}`
    );
    return response.data;
  } catch (error) {
    console.error("Error fetching forecast data:", error);
    throw error;
  }
}

module.exports = {
  getWeatherData,
  getForecastData,
  getWeatherDataAll,
};
