import { BrowserRouter as Router, Routes, Route, Link, Outlet } from "react-router-dom";
import Navbar from "./components/Navbar";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import BookListPage from "./pages/BookListPage";
import RegisterBook from "./pages/RegisterBook";

function NestedMenuPage() {
  return (
    <div className="text-center text-white">
      <h2 className="text-2xl font-bold mb-4">Nested Menu Page</h2>
      <p>This is a placeholder for the Nested Menu content.</p>

      {/* Links to nested routes */}
      <div className="mt-4">
        <Link to="dashboard" className="text-lime-300 mx-2">Dashboard</Link>
      </div>

      <Outlet />
    </div>
  );
}

function DashboardPage() {
  return (
    <div className="text-center text-white">
      <h2 className="text-2xl font-bold mb-4">Dashboard</h2>
      <p>Welcome to your dashboard!</p>
      <div className="mt-4">
        <Link to="settings" className="text-lime-300 mx-2">Settings</Link>
      </div>

      <Outlet />
    </div>
  );
}

function SettingsPage() {
  return (
    <div className="text-center text-white">
      <h2 className="text-2xl font-bold mb-4">Settings</h2>
      <p>Manage your settings here.</p>
    </div>
  );
}

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

          {/* Parent route */}
          <Route path="/nestedmenu" element={<NestedMenuPage />}>
            {/* Child route */}
            <Route path="dashboard" element={<DashboardPage />}>
              {/* Nested inside dashboard */}
              <Route path="settings" element={<SettingsPage />} />
            </Route>
          </Route>
        </Routes>
      </div>

      <div className="bg-primary text-white p-4">Primary test</div>
    </Router>
  );
}

export default App;
