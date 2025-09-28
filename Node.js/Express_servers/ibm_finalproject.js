import express from "express";
import crypto from "crypto";

const app = express();
const port = 3000;

app.use(express.json());

// Mock "database"
let users = [];
let sessions = {}; // token → username

// Reviews now stored per user: { isbn: { username: "review text" } }
let reviews = {
  9780140328721: { demoUser: "Great book!" },
  9780747532699: { demoUser: "Magical and fun!" },
};

// Task 1: Get a book list
app.get("/books", async (req, res) => {
  try {
    const response = await fetch(
      "https://openlibrary.org/search.json?q=book&limit=5"
    );
    const data = await response.json();
    res.json(data.docs);
  } catch (err) {
    res.status(500).send("Error fetching books");
  }
});

// Task 2: Get book by ISBN
app.get("/books/isbn/:isbn", async (req, res) => {
  try {
    const { isbn } = req.params;
    const response = await fetch(`https://openlibrary.org/isbn/${isbn}.json`);
    if (!response.ok) throw new Error("Not found");
    const data = await response.json();
    res.json(data);
  } catch (err) {
    res.status(404).send("Book not found");
  }
});

// Task 3: Get books by Author
app.get("/books/author/:authorKey", async (req, res) => {
  try {
    const { authorKey } = req.params;
    const response = await fetch(
      `https://openlibrary.org/search.json?author=${authorKey}`
    );
    const data = await response.json();
    res.json(data.docs);
  } catch (err) {
    res.status(500).send("Error fetching author books");
  }
});

// Task 4: Get books by Title
app.get("/books/title/:title", async (req, res) => {
  try {
    const { title } = req.params;
    const response = await fetch(
      `https://openlibrary.org/search.json?title=${title}`
    );
    const data = await response.json();
    res.json(data.docs);
  } catch (err) {
    res.status(500).send("Error fetching books");
  }
});

// Task 5: Get book Reviews
app.get("/books/:isbn/reviews", (req, res) => {
  const { isbn } = req.params;
  res.json({ isbn, reviews: reviews[isbn] || {} });
});

// Task 6: Register user
app.post("/register", (req, res) => {
  try {
    const { username, password } = req.body;
    if (users.find((u) => u.username === username)) {
      return res.status(400).send("User already exists");
    }
    users.push({ username, password });
    res.send("User registered successfully");
  } catch (err) {
    res.status(500).send("Error registering user");
  }
});

// Task 7: Login user
app.post("/login", (req, res) => {
  try {
    const { username, password } = req.body;
    const user = users.find(
      (u) => u.username === username && u.password === password
    );
    if (user) {
      const token = crypto.randomBytes(16).toString("hex");
      sessions[token] = username; // Save session
      res.json({ message: "Login successful", token });
    } else {
      res.status(401).send("Invalid credentials");
    }
  } catch (err) {
    res.status(500).send("Error logging in");
  }
});

// Middleware for auth
function authenticate(req, res, next) {
  const token = req.headers["authorization"];
  if (token && sessions[token]) {
    req.user = sessions[token];
    next();
  } else {
    res.status(401).send("Unauthorized");
  }
}

// Task 8: Add/Modify a book review
app.post("/books/:isbn/reviews", authenticate, (req, res) => {
  const { isbn } = req.params;
  const { review } = req.body;
  const username = req.user;

  if (!review) return res.status(400).send("Review is required");

  if (!reviews[isbn]) reviews[isbn] = {};

  reviews[isbn][username] = review; // add or overwrite review
  res.json({ message: "Review added/updated", reviews: reviews[isbn] });
});

// Task 9: Delete review by logged-in user
app.delete("/books/:isbn/reviews", authenticate, (req, res) => {
  const { isbn } = req.params;
  const username = req.user;

  if (reviews[isbn] && reviews[isbn][username]) {
    delete reviews[isbn][username];
    res.json({ message: "Review deleted" });
  } else {
    res.status(404).send("No review found for this user");
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
