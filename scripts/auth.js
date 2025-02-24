const API_BASE_URL = "https://api.ghostspoof.com"; // Adjust this to backend

document.getElementById("login-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    
    if (data.success) {
        alert("Login Successful!");
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid credentials, try again.");
    }
});
