import mongoose from "mongoose";

// Define the Quiz schema

const quizSchema = new mongoose.Schema(
  {
    title: {
      type: String,
      required: [true, "Quiz title is required"],
    },
    description: {
      type: String,
      required: [true, "Quiz description is required"],
    },
    questions: [
      {
        question: {
          type: String,
          required: [true, "Question text is required"],
        },
        options: [
          {
            option: {
              type: String,
              required: [true, "Option text is required"],
            },
            isCorrect: {
              type: Boolean,
              default: false,
            },
          },
        ],
      },
    ],
    createdBy: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
    },
  },

  {
    timestamps: true,
  }
);

const Quiz = mongoose.model("Quiz", quizSchema);

export default Quiz;
