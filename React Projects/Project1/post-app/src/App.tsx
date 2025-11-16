import { BrowserRouter as Router, Routes, Route, Link, Outlet } from "react-router-dom";
import Navbar from "./components/Navbar";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import BookListPage from "./pages/BookListPage";
import RegisterBook from "./pages/RegisterBook";
import BookDetailPage from "./pages/BookDetailPage";


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
      <div className="min-h-screen bg-slate-800 pt-20 flex flex-col items-center justify-center gap-6">

        <Routes>
          <Route path="/" element={<WelcomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/booklist" element={<BookListPage />} />
          <Route path="/registerbook" element={<RegisterBook />} />
          <Route path="/details/:bookId" element={<BookDetailPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
