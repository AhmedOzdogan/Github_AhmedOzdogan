import Quiz from "../models/quizModel.js";

// Get all quizzes
export const getAllQuizzes = async (req, res) => {
  try {
    const quizzes = await Quiz.find().populate("createdBy", "username");
    res.status(200).json(quizzes);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// Create a new quiz
export const createQuiz = async (req, res) => {
  try {
    const { title, description, questions } = req.body;
    if (!title || !description || !questions || questions.length === 0) {
      return res.status(400).json({ error: "All fields are required" });
    }
    const quiz = new Quiz({
      title,
      description,
      questions,
    });
    quiz.createdBy = req.user._id; // save the creator's ID
    await quiz.save();
    res.status(201).json({
        message: "Quiz created successfully",
        quiz: {
          id: quiz._id,
          title: quiz.title,
            description: quiz.description,
            questions: quiz.questions,
            createdBy: quiz.createdBy,
        },
    });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// Get a quiz by ID
export const getQuizById = async (req, res) => {
  try {
    const quiz = await Quiz.findById(req.params.id).populate("createdBy", "username");
    if (!quiz) {
      return res.status(404).json({ error: "Quiz not found" });
    }
    res.status(200).json(quiz);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

//edit quiz

export const editQuiz = async (req, res) => {
  try {
    const quiz = await Quiz.findById(req.params.id);
    if (!quiz) {
      return res.status(404).json({ error: "Quiz not found" });
    }
    const { title, description, questions } = req.body;
    quiz.title = title || quiz.title;
    quiz.description = description || quiz.description;
    quiz.questions = questions || quiz.questions;
    await quiz.save();
    res.status(200).json({
        message: "Quiz updated successfully",
        quiz: {
          id: quiz._id,
          title: quiz.title,
            description: quiz.description,
            questions: quiz.questions,
            createdBy: quiz.createdBy,
        },
    });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

//delete quiz
export const deleteQuiz = async (req, res) => {
  try {
    const quiz = await Quiz.findById(req.params.id);
    if (!quiz) {
      return res.status(404).json({ error: "Quiz not found" });
    }
    await quiz.remove();
    res.status(200).json({ message: "Quiz deleted successfully" });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};
