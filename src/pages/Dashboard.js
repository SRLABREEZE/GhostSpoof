import React, { useEffect } from "react";

const Dashboard = () => {
    useEffect(() => {
        window.location.href = "https://ghostspoof.com/dashboard";
    }, []);

    return (
        <div>
            <h1>Redirecting to Dashboard...</h1>
        </div>
    );
};

export default Dashboard;
