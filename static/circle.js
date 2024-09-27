document.addEventListener('DOMContentLoaded', function() {
    const circles = document.querySelectorAll('.progress-circle');

    circles.forEach(circle => {
        const value = parseFloat(circle.getAttribute('data-value')) * 10;
        const progress = circle.querySelector('.circle-progress');

        // Calcular el desplazamiento basado en el nuevo perímetro
        const offset = 150 - (150 * value) / 100;
        progress.style.strokeDashoffset = offset;

        // Cambiar el color según el valor
        if (value < 50) {
            progress.style.stroke = 'red';
        } else if (value >= 50 && value < 60) {
            progress.style.stroke = 'orange';
        } else if (value >= 60 && value < 77) {
            progress.style.stroke = 'green';
        } else {
            progress.style.stroke = 'oklch(86.59% 0.37 145.48)';
        }

        // Actualizar el texto dentro del círculo con 2 decimales
        const text = circle.querySelector('.progress-text');
        text.textContent = `${(value / 10).toFixed(2)}`; // Mostrar el valor original con 2 decimales
    });
});
