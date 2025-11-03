import express from "express";
import { getAllQuizzes, createQuiz, getQuizById, editQuiz,deleteQuiz } from "../controllers/quizController.js";
import { protect, authorizeQuizOwnerOrAdmin } from "../middleware/authMiddleware.js";
import { authorizeRoles } from "../middleware/roleMiddleware.js";

const quizRouter = express.Router();

// Anyone logged in can view all quizzes
quizRouter.get("/", protect, getAllQuizzes);

// Anyone logged in can view a specific quiz
quizRouter.get("/:id", protect, getQuizById);

// Only creators (teachers) and admins can edit or delete quizzes
quizRouter.put("/:id", authorizeQuizOwnerOrAdmin, authorizeRoles("teacher", "admin"), editQuiz);

// Only creators (teachers) and admins can delete quizzes
quizRouter.delete(
  "/:id",
  authorizeQuizOwnerOrAdmin,
  authorizeRoles("teacher", "admin"),
  deleteQuiz
);

// Only teachers and admins can create quizzes
quizRouter.post("/", protect, authorizeRoles("teacher", "admin"), createQuiz);

// Students submit their answers to a specific quiz
//quizRouter.post("/:id/submit", protect, submitQuiz);


export default quizRouter;
