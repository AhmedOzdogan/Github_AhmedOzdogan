import express from 'express';
import userRouter from './routes/userRoutes.js';
import quizRouter from './routes/quizRoutes.js';

const app = express();

// Middleware to parse JSON bodies
app.use(express.json());


//Routes

app.get('/', (req, res) => {
  res.send('Welcome to the Teachereye Backend!');
});

app.use('/api/users', userRouter);
app.use('/api/quizzes', quizRouter);

export default app;