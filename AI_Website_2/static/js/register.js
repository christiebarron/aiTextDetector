
document.addEventListener('DOMContentLoaded', function () {
    // Add event listener for the new user button
    let newUserButton = document.getElementById('new-user-btn');
    if (newUserButton) {
        newUserButton.addEventListener('click', function () {
            window.location.href = '/register';
        });
    }

    // Similarly, add event listeners for other buttons here
});