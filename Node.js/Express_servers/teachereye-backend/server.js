import dotenv from 'dotenv';
import app from './src/app.js';
import connectDB from './config/db.js';

// Load environment variables from .env file
dotenv.config();

const PORT = process.env.PORT || 5000;

// Connect to the database
connectDB();

// Start the server
app.listen(PORT, () => {
  console.log(`✅ Teachereye server running at http://localhost:${PORT}`);
});
