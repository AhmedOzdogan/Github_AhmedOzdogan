import { createContext, useContext, useEffect, useState } from "react";
import { get, set, del } from "idb-keyval";

interface AuthContextType {
    username: string | null;
    login: (username: string, accessToken: string, refreshToken: string) => Promise<void>;
    logout: () => Promise<void>;
}

export const AuthContext = createContext<AuthContextType | null>(null); 

export function AuthProvider({ children }: { children: React.ReactNode }) {
    const [username, setUsername] = useState<string | null>(null);

    useEffect(() => {
        const loadUser = async () => {
            const storedUsername = await get("username");
            if (storedUsername) setUsername(storedUsername);
        };
        loadUser();
    }, []);

    const login = async (username: string, accessToken: string, refreshToken: string) => {
        await set("username", username);
        await set("accessToken", accessToken);
        await set("refreshToken", refreshToken);
        setUsername(username);
    };

    const logout = async () => {
        await del("username");
        await del("accessToken");
        await del("refreshToken");
        setUsername(null);
    };

    return (
        <AuthContext.Provider value={{ username, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);
    if (!context) throw new Error("useAuth must be used within an AuthProvider");
    return context;
}
