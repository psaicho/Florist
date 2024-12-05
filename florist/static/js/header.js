document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;

    // Sprawdzanie stanu przy ładowaniu
    const darkModeCookie = getCookie('darkMode');
    if (darkModeCookie === 'true') {
        body.classList.add('dark-mode');
        if (darkModeToggle) {
            darkModeToggle.checked = true;
        }
    }

    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            const isDarkMode = body.classList.contains('dark-mode');
            document.cookie = `darkMode=${isDarkMode};path=/;max-age=${30*24*60*60};SameSite=Strict`;
        });
    }
});
