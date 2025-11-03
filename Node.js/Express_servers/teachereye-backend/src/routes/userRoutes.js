import express from "express";
import {
  registerUser,
  loginUser,
  changePassword,
  refreshAccessToken,
} from "../controllers/userController.js";
import {protect} from "../middleware/authMiddleware.js";

const userRouter = express.Router();

userRouter.post("/register", registerUser);
userRouter.post("/login", loginUser);
userRouter.post("/refresh", refreshAccessToken);
userRouter.post("/change-password", protect, changePassword);


export default userRouter;
