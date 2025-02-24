const API_BASE_URL = "https://api.ghostspoof.com";

async function loadDashboard() {
    const response = await fetch(`${API_BASE_URL}/users/minutes`, {
        method: "GET",
        headers: { "Authorization": `Bearer ${localStorage.getItem("token")}` },
    });

    const data = await response.json();
    document.getElementById("minutes").innerText = data.minutes;
}

async function loadCallHistory() {
    const response = await fetch(`${API_BASE_URL}/calls/logs`, {
        method: "GET",
        headers: { "Authorization": `Bearer ${localStorage.getItem("token")}` },
    });

    const calls = await response.json();
    const callList = document.getElementById("call-history");
    callList.innerHTML = "";
    
    calls.forEach(call => {
        let li = document.createElement("li");
        li.innerText = `Called: ${call.number} - Duration: ${call.duration} min`;
        callList.appendChild(li);
    });
}

loadDashboard();
loadCallHistory();
