document.getElementById('deleteReplyBtn').addEventListener('click', function() {
    const replyId = 'REPLY_ID_HERE'; // Replace with the actual reply ID

    // Make AJAX request to delete reply to support ticket endpoint
    fetch(`support-ticket-replies/<int:reply_id>/`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            alert('Reply deleted successfully!');
            console.log('Reply deleted successfully!');
            // Redirect or update UI as needed
        } else {
            throw new Error('Failed to delete reply');
        }
    })
    .catch(error => {
        alert('Failed to delete reply');
        console.error('Error:', error);
    });
});
