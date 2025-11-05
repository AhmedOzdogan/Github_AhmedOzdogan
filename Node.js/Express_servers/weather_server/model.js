// models/Weather.js
const mongoose = require("mongoose");

const weatherSchema = new mongoose.Schema({
  st: String,
  ts: Date,
  position: {
    type: {
      type: String,
      enum: ["Point"],
      required: false,
    },
    coordinates: {
      type: [Number],
      required: false,
    },
  },
  elevation: Number,
  callLetters: String,
  qualityControlProcess: String,
  dataSource: String,
  type: String,
  airTemperature: Object,
  dewPoint: Object,
  pressure: Object,
  wind: Object,
  visibility: Object,
  skyCondition: Object,
  sections: Array,
  precipitationEstimatedObservation: Object,
  pastWeatherObservationManual: Array,
  skyConditionObservation: Object,
  presentWeatherObservationManual: Array,
});

weatherSchema.index({ position: "2dsphere" });

module.exports = mongoose.model("Weather", weatherSchema);
