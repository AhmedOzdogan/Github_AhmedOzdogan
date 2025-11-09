import { useState, useContext } from "react";
import InputField from "../components/InputField";
import FormContainer from "../components/FormContainer";
import SubmitButton from "../components/SubmitButton";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

function LoginPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);

        if (!username || !password) {
            setError("Please fill in all fields.");
            return;
        }

        setLoading(true);

        try {
            const response = await fetch("http://127.0.0.1:8000/api/token/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password }),
            });

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.detail || "Invalid credentials");
            }

            const data = await response.json();
            console.log("✅ API response:", data);

            // Call the context login — this already stores tokens in IndexedDB
            await login(username, data.access, data.refresh);
            navigate("/");

            alert(`✅ Login successful! Welcome, ${username}`);
            window.location.href = "/"; // Optional: redirect to home page
        } catch (err: any) {
            console.error("❌ Login error:", err);
            setError(err.message || "Login failed. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <FormContainer title="Login">
            <form onSubmit={handleLogin}>
                <InputField
                    label="Username"
                    type="text"
                    placeholder="Enter your username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <InputField
                    label="Password"
                    type="password"
                    placeholder="Enter your password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                {error && <p className="text-red-500 text-sm mb-2">{error}</p>}

                <SubmitButton label="Login" loading={loading} />

                <p className="text-sm text-white text-center mt-4">
                    Don’t have an account?{" "}
                    <a href="/signup" className="text-lime-300 hover:underline">
                        Sign Up
                    </a>
                </p>
            </form>
        </FormContainer>
    );
}

export default LoginPage;
