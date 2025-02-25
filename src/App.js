import React from "react";
import { AuthProvider } from "./context/AuthContext";
import AppRoutes from "./routes";
import Navbar from "./components/Navbar";

const App = () => {
    return (
        <AuthProvider>
            <Navbar />
            <AppRoutes />
        </AuthProvider>
    );
};

export default App;
