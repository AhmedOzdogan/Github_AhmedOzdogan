import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";

function App() {
  return (
    <Router>
      <Navbar />
      <div className="min-h-screen bg-gray-50 pt-20 flex flex-col items-center justify-center gap-6">
        <h1 className="text-3xl font-bold text-gray-800">Welcome to MyApp</h1>

        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
