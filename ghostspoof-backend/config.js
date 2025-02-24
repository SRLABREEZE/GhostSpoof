module.exports = {
  jwtSecret: process.env.JWT_SECRET || "your-secret-key",
  mongoURI: process.env.MONGO_URI || "your-mongodb-connection-string"
};
export const API_URL = "https://api.ghostspoof.com/api"; 

};
