const CONFIG = {
    API_URL: process.env.REACT_APP_API_URL || "http://localhost:5000",
    TOKEN_KEY: "ghostspoof_token",
    TIMEOUT: 5000,
    ENV: process.env.NODE_ENV || "development",
};
export default CONFIG;
