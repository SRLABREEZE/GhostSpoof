document.addEventListener("DOMContentLoaded", function() {
    fetch('https://ghostspoof-backend.onrender.com/get_admin_data.php')
        .then(response => response.json())
        .then(data => {
            document.getElementById("admin-username").textContent = data.username;
        });
});
