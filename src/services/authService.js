import CONFIG from "../config";

export const login = async (email, password) => {
    try {
        const response = await fetch(`${CONFIG.API_URL}/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password }),
        });

        if (!response.ok) throw new Error("Login failed");

        const data = await response.json();
        localStorage.setItem(CONFIG.TOKEN_KEY, data.token);
        return data;
    } catch (error) {
        console.error("Login error:", error);
        throw error;
    }
};

export const register = async (email, password) => {
    try {
        const response = await fetch(`${CONFIG.API_URL}/register`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password }),
        });

        if (!response.ok) throw new Error("Registration failed");

        const data = await response.json();
        localStorage.setItem(CONFIG.TOKEN_KEY, data.token);
        return data;
    } catch (error) {
        console.error("Registration error:", error);
        throw error;
    }
};

export const logout = () => {
    localStorage.removeItem(CONFIG.TOKEN_KEY);
};

export const getToken = () => {
    return localStorage.getItem(CONFIG.TOKEN_KEY);
};

export const isAuthenticated = () => {
    return !!getToken();
};
