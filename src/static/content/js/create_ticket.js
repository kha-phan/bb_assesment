document.getElementById('createTicketForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const subject = document.getElementById('subject').value;
    const description = document.getElementById('description').value;

    // Make AJAX request to create support ticket endpoint
    fetch('support-tickets/create/', {
        method: 'POST',
        body: JSON.stringify({ subject, description }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert('Support ticket created successfully!');
        console.log('Ticket:', data);
        // Redirect or update UI as needed
    })
    .catch(error => console.error('Error:', error));
});
