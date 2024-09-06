document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById('loginForm');

    if (loginForm) {
        const loginUrl = loginForm.getAttribute('data-login-url');
        const dashboardUrl = loginForm.getAttribute('data-dashboard-url');

        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);


            clearErrors();

            fetch(loginUrl, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = dashboardUrl; 
                } else {
                    if (data.errors) {
                        displayFieldErrors(data.errors); 
                    }
                    if (data.message) {
                        displayGeneralError(data.message); 
                    }
                }
            })
            .catch(error => {
                console.error('Fetch Error:', error);
                displayGeneralError('Error procesando la solicitud. Por favor, intente de nuevo más tarde.'); 
            });
        });
    }
});

function clearErrors() {
    const errorElements = document.querySelectorAll('.form-error');
    errorElements.forEach(element => {
        element.textContent = '';  // Limpiar el texto de error
    });
}

function displayFieldErrors(errors) {
    Object.keys(errors).forEach(field => {
        const errorMessages = errors[field];
        const errorContainer = document.getElementById(`error-${field}`);
        if (errorContainer) {
            errorContainer.textContent = errorMessages.join(', ');
        }
    });
}

function displayGeneralError(message) {
    const messageContainer = document.getElementById('messageContainer');
    if (messageContainer) {
        messageContainer.innerHTML = `<div class="alert alert-danger">${message}</div>`;
    }
}



