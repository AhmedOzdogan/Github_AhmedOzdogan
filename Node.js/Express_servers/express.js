const express = require("express");
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Sample route
app.get("/", (req, res) => {
  res.send("Hello World!");

  req.query; // Access query parameters
  console.log(req.query);
  req.body; // Access JSON body (if any)
  console.log(req.body);
});

app.get("/hello", (req, res) => {
  res.send("Hello from /hello route!");
});

// Post route to demonstrate JSON body parsing
app.post("/data", (req, res) => {
  res.json({ received: req.body });
});

// Example with params
app.get("/user/:id", (req, res) => {
  res.json({ userId: req.params.id });
});

app.listen(port, () => {
  console.log(`🚀 Server running at http://localhost:${port}`);
});
