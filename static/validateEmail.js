document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');
    const emailField = document.querySelector('input[name="username"]'); // Asegúrate de que este nombre coincida con el campo de nombre de usuario en tu formulario
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', function(event) {
        const email = emailField.value;
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(email)) {
            event.preventDefault(); // Evita el envío del formulario
            errorMessage.style.display = 'block';
            emailField.focus();
        } else {
            errorMessage.style.display = 'none';
        }
    });
});
