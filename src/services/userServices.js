import CONFIG from "../config";

// Fetch user profile
export const getUserProfile = async () => {
    try {
        const token = localStorage.getItem(CONFIG.TOKEN_KEY);
        if (!token) throw new Error("User not authenticated");

        const response = await fetch(`${CONFIG.API_URL}/user/profile`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) throw new Error("Failed to fetch user profile");

        return await response.json();
    } catch (error) {
        console.error("Profile error:", error);
        throw error;
    }
};

// Update user profile
export const updateUserProfile = async (userData) => {
    try {
        const token = localStorage.getItem(CONFIG.TOKEN_KEY);
        if (!token) throw new Error("User not authenticated");

        const response = await fetch(`${CONFIG.API_URL}/user/profile`, {
            method: "PUT",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userData),
        });

        if (!response.ok) throw new Error("Failed to update profile");

        return await response.json();
    } catch (error) {
        console.error("Profile update error:", error);
        throw error;
    }
};

// Change user password
export const changePassword = async (currentPassword, newPassword) => {
    try {
        const token = localStorage.getItem(CONFIG.TOKEN_KEY);
        if (!token) throw new Error("User not authenticated");

        const response = await fetch(`${CONFIG.API_URL}/user/change-password`, {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ currentPassword, newPassword }),
        });

        if (!response.ok) throw new Error("Failed to change password");

        return await response.json();
    } catch (error) {
        console.error("Password change error:", error);
        throw error;
    }
};

// Delete user account
export const deleteUserAccount = async () => {
    try {
        const token = localStorage.getItem(CONFIG.TOKEN_KEY);
        if (!token) throw new Error("User not authenticated");

        const response = await fetch(`${CONFIG.API_URL}/user/delete`, {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) throw new Error("Failed to delete account");

        return await response.json();
    } catch (error) {
        console.error("Account deletion error:", error);
        throw error;
    }
};
