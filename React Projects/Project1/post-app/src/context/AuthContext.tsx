import { createContext, useContext, useEffect, useState } from "react";
import { get, set, del } from "idb-keyval";

interface UserData {
    id: number;
    username: string;
    email: string;
    role: string;
    blocked: boolean;
}

interface AuthContextType {
    user: UserData | null;
    login: (user: UserData) => Promise<void>;
    logout: () => Promise<void>;
}

export const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
    const [user, setUser] = useState<UserData | null>(null);

    useEffect(() => {
        const loadStoredUser = async () => {
            const savedUser = await get("user");
            if (savedUser) setUser(savedUser);
        };
        loadStoredUser();
    }, []);

    const login = async (userData: UserData) => {
        await set("user", userData);
        setUser(userData);
    };

    const logout = async () => {
        await del("user");
        setUser(null);

        // hit logout endpoint to clear cookies
        await fetch("http://127.0.0.1:8000/api/logout/", {
            method: "POST",
            credentials: "include",
        });
    };

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const ctx = useContext(AuthContext);
    if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
    return ctx;
}
