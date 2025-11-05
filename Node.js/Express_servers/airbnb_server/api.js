const mongoose = require("mongoose");
const Airbnb = require("./model");

const BASE_URL = "http://localhost:3000";

/* ----------------------------- Get All Listings ----------------------------- */
async function getAllListings(limit = 10) {
  try {
    const listings = await Airbnb.find({}).limit(limit).lean();
    console.log("✅ Sample listing ID:", listings[0]?._id);
    return listings;
  } catch (error) {
    console.error("❌ Error fetching all Airbnb listings:", error);
    throw new Error("Failed to fetch listings");
  }
}

/* ---------------------------- Get Listing by ID ----------------------------- */
async function getListingById(propertyId) {
  try {
    // Since _id is a string, no ObjectId validation
    const listing = await Airbnb.findOne({ _id: propertyId }).lean();

    if (!listing) {
      throw new Error(`No listing found with ID ${propertyId}`);
    }

    return listing;
  } catch (error) {
    console.error("❌ Error fetching listing by ID:", error.message);
    throw new Error("Failed to fetch listing");
  }
}

/* -------------------------- Get Reviews by Listing ID ----------------------- */
async function getReviewsByListingId(propertyId) {
  try {
    const listing = await Airbnb.findOne(
      { _id: propertyId },
      { reviews: 1 }
    ).lean(); // only fetch 'reviews'

    if (!listing) {
      throw new Error(`No listing found with ID ${propertyId}`);
    }

    return listing.reviews || [];
  } catch (error) {
    console.error("❌ Error fetching reviews by listing ID:", error.message);
    throw new Error("Failed to fetch reviews");
  }
}

/* --------------------------------------------------------------------------- */
module.exports = {
  getAllListings,
  getListingById,
  getReviewsByListingId,
};
