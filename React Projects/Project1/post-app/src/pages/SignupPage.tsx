import { useState } from "react";
import InputField from "../components/InputField";
import FormContainer from "../components/FormContainer";
import SubmitButton from "../components/SubmitButton";

function SignupPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const handleSignup = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);

        if (!username || !password || !confirmPassword) {
            setError("Please fill in all fields.");
            return;
        }

        if (password !== confirmPassword) {
            setError("Passwords do not match.");
            return;
        }

        setLoading(true);

        try {
            const response = await fetch("http://127.0.0.1:8000/api/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username,
                    password,
                }),
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            console.log("API response:", data);

            alert(`Signup successful! Welcome, ${username}`);
        } catch (err) {
            setError("Signup failed. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <FormContainer title="Signup">
            <form onSubmit={handleSignup} className="space-y-4">
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

                <InputField
                    label="Confirm Password"
                    type="password"
                    placeholder="Re-enter your password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                />

                {error && <p className="text-red-500 text-sm mb-2">{error}</p>}

                <SubmitButton label="Signup" loading={loading} />
            </form>

            <p className="text-sm text-white text-center mt-4">
                Already have an account?{" "}
                <a href="/login" className="text-lime-300 hover:underline">
                    Login
                </a>
            </p>
        </FormContainer>
    );
}

export default SignupPage;
