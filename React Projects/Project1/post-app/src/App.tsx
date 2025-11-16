import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import { lazy, Suspense } from "react";

const LoginPage = lazy(() => import("./pages/LoginPage"));
const SignupPage = lazy(() => import("./pages/SignupPage"));
const BookListPage = lazy(() => import("./pages/BookListPage"));
const RegisterBook = lazy(() => import("./pages/RegisterBook"));
const BookDetailPage = lazy(() => import("./pages/BookDetailPage"));

function WelcomePage() {
  return (
    <div className="text-center text-white">
      <h2 className="text-2xl font-bold mb-4">Welcome to MyApp</h2>
      <p>This is the welcome page.</p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Navbar />

      <Suspense
        fallback={
          <div className="flex justify-center items-center text-white text-xl mt-10">
            Loading...
          </div>
        }
      >
        <div className="min-h-screen bg-slate-800 pt-20 flex flex-col items-center gap-6">
          <Routes>
            <Route path="/" element={<WelcomePage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/signup" element={<SignupPage />} />
            <Route path="/booklist" element={<BookListPage />} />
            <Route path="/registerbook" element={<RegisterBook />} />
            <Route path="/details/:bookId" element={<BookDetailPage />} />
            <Route path="*" element={<div className="text-white">404 Not Found</div>} />
          </Routes>
        </div>
      </Suspense>
    </Router>
  );
}

export default App;
