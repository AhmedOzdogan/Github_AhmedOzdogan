import dotenv from "dotenv";
import mongoose from "mongoose";

dotenv.config();

// Schema & model
const userSchema = new mongoose.Schema(
  {
    name: { type: String, required: true, unique: true, trim: true },
    age: { type: Number, required: true, min: 0, max: 120 },
  },
  { timestamps: true }
);
// being explicit also helps:
userSchema.index({ name: 1 }, { unique: true });

const User = mongoose.model("User", userSchema);

async function createUser(name, age) {
  try {
    const user = await User.create({ name, age });
    console.log("User created:", user.toJSON());
  } catch (err) {
    if (err.code === 11000) {
      console.error("Duplicate name not allowed:", err.keyValue);
    } else {
      console.error("Create error:", err.message);
    }
  }
}

async function findUsers() {
  const users = await User.find().lean();
  console.log("All users:", users);
}

async function main() {
  const uri = process.env.MONGODB_URI;
  if (!uri) throw new Error("Missing MONGODB_URI");

  await mongoose.connect(uri);
  console.log("Connected to MongoDB");

  // Dev-only: make sure index exists and collection is clean for demo
  await User.syncIndexes(); // builds the unique index if missing
  await User.deleteMany({});

  await createUser("Alice", 30);
  await createUser("Bob", 25);
  await createUser("Bob", 28); // triggers E11000 duplicate key
  await findUsers();

  await mongoose.disconnect();
  console.log("Disconnected");
}

main().catch(console.error);
