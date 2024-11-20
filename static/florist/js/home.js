


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
function includeHTML(targetElementId, filePath) {
    console.log('Próba załadowania:', filePath);
    fetch(filePath)
        .then(response => {
            console.log('Odpowiedź otrzymana:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            console.log('Dane otrzymane, długość:', data.length);
            document.getElementById(targetElementId).innerHTML = data;
        })
        .catch(error => {
            console.error('Błąd podczas wczytywania pliku:', error);
            document.getElementById(targetElementId).innerHTML = 'Nie udało się załadować zawartości.';
        });
}
