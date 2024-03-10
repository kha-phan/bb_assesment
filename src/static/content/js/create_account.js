document.getElementById('createAccountForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;

    // Make AJAX request to create account endpoint
    fetch('accounts/create/', {
        method: 'POST',
        body: JSON.stringify({ username }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert('Account created successfully!');
        console.log('Account:', data);
        // Redirect or update UI as needed
    })
    .catch(error => console.error('Error:', error));
});