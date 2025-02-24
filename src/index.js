import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

const globalStyles = {
    body: {
        backgroundColor: "black",
        color: "white",
        fontFamily: "Arial, sans-serif",
        textAlign: "center",
        margin: "0",
        padding: "0",
    }
};

// Apply styles globally
Object.assign(document.body.style, globalStyles.body);

ReactDOM.render(<App />, document.getElementById("root"));
