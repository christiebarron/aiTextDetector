document.addEventListener('DOMContentLoaded', function() {
    var tabLinks = document.getElementsByClassName('tab-link');
    for (var i = 0; i < tabLinks.length; i++) {
        tabLinks[i].addEventListener('click', switchTab);
    }

    document.getElementById('login-button').addEventListener('click', function() {
        // Handle login
        console.log('Login button clicked');
    });

    document.getElementById('register-button').addEventListener('click', function() {
        // Handle registration
        console.log('Register button clicked');
    });

    document.getElementById('forgot-password-button').addEventListener('click', function() {
        // Handle forgot password
        console.log('Forgot password button clicked');
    });
});

function switchTab() {
    var tabId = this.getAttribute('data-tab');
    var tabLinks = document.getElementsByClassName('tab-link');
    for (var i = 0; i < tabLinks.length; i++) {
        tabLinks[i].classList.remove('current');
        var tabContent = document.getElementById(tabLinks[i].getAttribute('data-tab'));
        tabContent.classList.remove('current');
    }
    this.classList.add('current');
    var tabContent = document.getElementById(tabId);
    tabContent.classList.add('current');
}
