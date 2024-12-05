ocument.querySelectorAll('.quantity-btn').forEach(button => {
    button.addEventListener('click', function() {
        const input = this.parentNode.querySelector('.quantity-input');
        const currentValue = parseInt(input.value);

        if (this.classList.contains('plus')) {
            input.value = currentValue + 1;
        } else if (this.classList.contains('minus') && currentValue > 1) {
            input.value = currentValue - 1;
        }
    });
});