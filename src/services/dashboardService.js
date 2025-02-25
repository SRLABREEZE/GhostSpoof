import CONFIG from "../config";

// Fetch dashboard stats
export const getDashboardStats = async () => {
    try {
        const token = localStorage.getItem(CONFIG.TOKEN_KEY);
        if (!token) throw new Error("User not authenticated");

        const response = await fetch(`${CONFIG.API_URL}/dashboard/stats`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) throw new Error("Failed to fetch dashboard stats");

        return await response.json();
    } catch (error) {
        console.error("Dashboard stats error:", error);
        throw error;
    }
};

// Fetch recent activity
export const getRecentActivity = async () => {
    try {
        const token = localStorage.getItem(CONFIG.TOKEN_KEY);
        if (!token) throw new Error("User not authenticated");

        const response = await fetch(`${CONFIG.API_URL}/dashboard/activity`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) throw new Error("Failed to fetch recent activity");

        return await response.json();
    } catch (error) {
        console.error("Recent activity error:", error);
        throw error;
    }
};
