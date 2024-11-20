
document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;

    if (darkModeToggle) {
        console.log('test');
        darkModeToggle.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
        });
    }
});
