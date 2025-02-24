import React from "react";

const Login = () => {
    // Inline styles for neon glow effect
    const styles = {
        container: {
            background: "rgba(0, 0, 0, 0.8)",
            border: "2px solid #00ffcc",
            borderRadius: "10px",
            boxShadow: "0px 0px 20px #00ffcc",
            padding: "20px",
            width: "320px",
            margin: "50px auto",
            textAlign: "center",
        },
        input: {
            background: "#111",
            color: "white",
            border: "2px solid #00ffcc",
            padding: "12px",
            width: "90%",
            marginBottom: "10px",
            borderRadius: "5px",
            outline: "none",
            boxShadow: "0 0 5px #00ffcc",
            transition: "all 0.3s ease-in-out",
        },
        inputFocus: {
            boxShadow: "0 0 15px #00ffcc",
        },
        button: {
            background: "#00ffcc",
            color: "black",
            fontWeight: "bold",
            border: "none",
            padding: "12px 20px",
            width: "100%",
            cursor: "pointer",
            transition: "0.3s ease-in-out",
            boxShadow: "0 0 5px #00ffcc",
            borderRadius: "5px",
        },
        buttonHover: {
            boxShadow: "0 0 15px #00ffcc",
            transform: "scale(1.05)",
        },
        title: {
            color: "#00ffcc",
            textShadow: "0px 0px 10px #00ffcc, 0px 0px 20px #00ffcc",
        },
    };

    return (
        <div style={styles.container}>
            <h1 style={styles.title}>Login to GhostSpoof</h1>
            <input type="email" placeholder="Enter Email" style={styles.input} />
            <input type="password" placeholder="Enter Password" style={styles.input} />
            <button style={styles.button}>Login</button>
        </div>
    );
};

export default Login;
