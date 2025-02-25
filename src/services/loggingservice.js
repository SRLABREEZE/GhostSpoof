import CONFIG from "../config";

// Log error messages
export const logError = async (message) => {
    try {
        await fetch(`${CONFIG.API_URL}/logs/error`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message }),
        });
    } catch (error) {
        console.error("Logging error failed:", error);
    }
};

// Log user activity
export const logActivity = async (activity) => {
    try {
        const token = localStorage.getItem(CONFIG.TOKEN_KEY);
        if (!token) throw new Error("User not authenticated");

        await fetch(`${CONFIG.API_URL}/logs/activity`, {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ activity }),
        });
    } catch (error) {
        console.error("Logging activity failed:", error);
    }
};
