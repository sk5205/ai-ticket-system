function loginUser() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (email === "admin@gmail.com" && password === "1234") {
        window.location.href = "dashboard.html";
        return false;
    } else {
        document.getElementById("error-msg").innerText = "Invalid Credentials";
        return false;
    }
}

function logout() {
    window.location.href = "index.html";
}

function predictTicket() {
    const text = document.getElementById("ticketText").value;

    if (text.length < 5) {
        alert("Please enter valid ticket description");
        return;
    }

    // Dummy prediction for UI demo
    document.getElementById("result").innerHTML =
        "Predicted Category: Technical Issue <br> Predicted Priority: High";
}

function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: "smooth" });
}
