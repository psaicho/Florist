// Slider functionality
const slides = document.querySelectorAll('.slide');
const dotContainer = document.getElementById('dotContainer');
let currentSlide = 0;

function showSlide(index) {
    slides.forEach((slide, i) => {
        if (i === index) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });
    updateDots();
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

// Create dots
slides.forEach((_, index) => {
    const dot = document.createElement('span');
    dot.classList.add('dot');
    dot.addEventListener('click', () => {
        currentSlide = index;
        showSlide(currentSlide);
    });
    dotContainer.appendChild(dot);
});

function updateDots() {
    const dots = document.querySelectorAll('.dot');
    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentSlide);
    });
}

// Initialize the slider
showSlide(currentSlide);

// Auto-advance slides every 5 seconds
setInterval(nextSlide, 5000);

//include
document.addEventListener('DOMContentLoaded', function() {
    includeHTML('header', '../layout/header.html');
});

function includeHTML(targetElementId, filePath) {
    fetch(filePath)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            document.getElementById(targetElementId).innerHTML = data;
        })
        .catch(error => {
            console.error('Błąd podczas wczytywania pliku:', error);
            document.getElementById(targetElementId).innerHTML = 'Nie udało się załadować zawartości.';
        });
}