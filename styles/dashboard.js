document.addEventListener("DOMContentLoaded", function() {
    fetch('https://ghostspoof-backend.onrender.com/get_user_data.php')
        .then(response => response.json())
        .then(data => {
            document.getElementById("username").textContent = data.username;
            document.getElementById("minutes").textContent = data.minutes;
        });
});
