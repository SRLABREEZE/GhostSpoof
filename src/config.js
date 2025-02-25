const CONFIG = {
    API_URL: process.env.REACT_APP_API_URL || "http://localhost:5000",
    TOKEN_KEY: "ghostspoof_token",  // LocalStorage key for JWT
    TIMEOUT: 5000,  // API request timeout in milliseconds
    ENV: process.env.NODE_ENV || "development",  // Environment setting
};

// Export the config object
export default CONFIG;
