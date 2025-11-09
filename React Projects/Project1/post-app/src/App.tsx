import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import BookListPage from "./pages/BookListPage";
import RegisterBook from "./pages/RegisterBook";

function App() {
  return (
    <Router>
      <Navbar />
      <div className="min-h-screen bg-slate-800 pt-20 flex flex-col items-center justify-center gap-6">
        <h1 className="text-3xl font-bold text-lime-300">Welcome to MyApp</h1>

        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/booklist" element={<BookListPage />} />
          <Route path="/registerbook" element={<RegisterBook />} />
        </Routes>
      </div>
      <div className="bg-primary text-white p-4">Primary test</div>
    </Router>
  );
}

export default App;