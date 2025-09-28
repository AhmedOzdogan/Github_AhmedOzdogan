import axios from "axios";

// Base URL of your Express server
const BASE_URL = "http://localhost:3000";

// ----------------------
// Task 10: Get all books – Using async/await
// ----------------------
async function getAllBooks() {
  try {
    const res = await axios.get(`${BASE_URL}/books`);
    console.log("Task 10 - All Books:", res.data);
  } catch (err) {
    console.error("Error fetching books:", err.message);
  }
}

// ----------------------
// Task 11: Search by ISBN – Using Promises
// ----------------------
function getBookByISBN(isbn) {
  axios
    .get(`${BASE_URL}/books/isbn/${isbn}`)
    .then((res) => {
      console.log("Task 11 - Book by ISBN:", res.data);
    })
    .catch((err) => {
      console.error("Error fetching book by ISBN:", err.message);
    });
}

// ----------------------
// Task 12: Search by Author – Async callback style
// ----------------------
function getBooksByAuthor(authorKey, callback) {
  axios
    .get(`${BASE_URL}/books/author/${authorKey}`)
    .then((res) => callback(null, res.data))
    .catch((err) => callback(err));
}

// ----------------------
// Task 13: Search by Title – Async/Await again
// ----------------------
async function getBooksByTitle(title) {
  try {
    const res = await axios.get(`${BASE_URL}/books/title/${title}`);
    console.log("Task 13 - Books by Title:", res.data);
  } catch (err) {
    console.error("Error fetching books by title:", err.message);
  }
}

// ----------------------
// Run the tasks
// ----------------------
async function run() {
  await getAllBooks(); // Task 10
  getBookByISBN("9780140328721"); // Task 11
  getBooksByAuthor("tolkien", (err, data) => {
    if (err) console.error("Error fetching by author:", err.message);
    else console.log("Task 12 - Books by Author:", data);
  });
  await getBooksByTitle("harry potter"); // Task 13
}

run();
