document.getElementById('createAccountBtn').addEventListener('click', function() {
    // Redirect to the create account page
    window.location.href = "{% url 'src:create_account' %}";
});

document.getElementById('createTicketBtn').addEventListener('click', function() {
    // Redirect to the create account page
    window.location.href = "{% url 'src:create_ticket' %}";
});



//function createAccount() {
//    window.location.href = "{% url 'create_account' %}";
//    // Make AJAX request to create account endpoint
//    fetch('accounts/create/', {
//        method: 'POST',
//        body: JSON.stringify({ /* account data */ }),
//        headers: {
//            'Content-Type': 'application/json'
//        }
//    })
//    .then(response => response.json())
//    .then(data => {
//        // Display account info in HTML
//        document.getElementById('accountInfo').innerHTML = `<p>Account created: ${data.username}</p>`;
//    })
//    .catch(error => console.error('Error:', error));
//}
//
//function createTicket() {
//    // Make AJAX request to create ticket endpoint
//    fetch('support-tickets/create/', {
//        method: 'POST',
//        body: JSON.stringify({ /* ticket data */ }),
//        headers: {
//            'Content-Type': 'application/json'
//        }
//    })
//    .then(response => response.json())
//    .then(data => {
//        // Display ticket info in HTML
//        document.getElementById('ticketList').innerHTML += `<p>Ticket created: ${data.subject}</p>`;
//    })
//    .catch(error => console.error('Error:', error));
//}
