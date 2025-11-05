const express = require("express");
const bodyParser = require("body-parser");
const {
  getAllListings,
  getListingById,
  getReviewsByListingId,
} = require("./api");

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(express.static("public"));

//----------------------------Routes----------------------------//

// Get all listings
app.get("/airbnb", async (req, res) => {
  try {
    const listings = await getAllListings();
    res.json(listings);
  } catch {
    res.status(500).json({ error: "Internal Server Error" });
  }
});

// Get listing by ID
app.get("/airbnb/listing/:id", async (req, res) => {
  try {
    const listing = await getListingById(req.params.id);
    res.json(listing);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get reviews by listing ID
app.get("/airbnb/listing/:id/reviews", async (req, res) => {
  try {
    const reviews = await getReviewsByListingId(req.params.id);
    res.json(reviews);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`✅ Airbnb server running at http://localhost:${port}`);
});
