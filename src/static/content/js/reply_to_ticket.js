document.getElementById('replyToTicketForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const ticketId = document.getElementById('ticketId').value;
    const message = document.getElementById('message').value;

    // Make AJAX request to reply to support ticket endpoint
    fetch(`support-tickets/<int:ticket_id>/reply/`, {
        method: 'POST',
        body: JSON.stringify({ message }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert('Reply posted successfully!');
        console.log('Reply:', data);
        // Redirect or update UI as needed
    })
    .catch(error => console.error('Error:', error));
});
