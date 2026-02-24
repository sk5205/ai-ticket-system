document.addEventListener("DOMContentLoaded", loadTickets);

async function loadTickets() {

    const container = document.getElementById("ticketList");
    if (!container) return;

    try {
        const response = await fetch("http://127.0.0.1:8000/tickets");
        const tickets = await response.json();

        container.innerHTML = "";

        tickets.reverse().forEach(ticket => {

            const formattedId = "#TKT-" + String(ticket.id).padStart(3, "0");

            let priorityClass =
                ticket.priority === "High" ? "high" :
                ticket.priority === "Medium" ? "medium" :
                "low";

            container.innerHTML += `
                <div class="ticket-card">

                    <div class="ticket-header">
                        <span class="ticket-id">${formattedId}</span>
                        <span class="priority ${priorityClass}">
                            ${ticket.priority}
                        </span>
                    </div>

                    <h3 class="ticket-title">
                        ${ticket.description}
                    </h3>

                    <div class="ticket-meta">
                        <span>${ticket.category}</span>
                        <span>${new Date(ticket.created_at).toLocaleString()}</span>
                    </div>

                </div>
            `;
        });

    } catch (error) {
        container.innerHTML = "<p>Unable to load tickets.</p>";
        console.error(error);
    }
}

setInterval(loadTickets, 5000);