import { createContext, useState, useEffect } from "react";
import { getToken, isAuthenticated, logout } from "../services/authService";

export const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        if (isAuthenticated()) {
            setUser(getToken());
        }
    }, []);

    return (
        <AuthContext.Provider value={{ user, setUser, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
