document.getElementById("login-form").addEventListener("submit", function(event) {
  event.preventDefault();

  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/login", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        // Login successful, redirect to analysis_page.html
        window.location.href = "/dashboard";
      } else {
        // Login failed, display error message
        var response = JSON.parse(xhr.responseText);
        alert(response.message);
      }
    }
  };

  var data = JSON.stringify({ "username": username, "password": password });
  xhr.send(data);
});

