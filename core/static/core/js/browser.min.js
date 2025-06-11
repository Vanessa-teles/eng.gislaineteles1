// Arquivo JS principal para o site da Gislaine Teles
document.addEventListener('DOMContentLoaded', function() {
    // Animação suave para links internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Destacar o item de menu ativo
    const currentLocation = window.location.pathname;
    const menuItems = document.querySelectorAll('#nav ul li a');
    
    menuItems.forEach(item => {
        const href = item.getAttribute('href');
        if (currentLocation.endsWith(href)) {
            item.style.backgroundColor = 'var(--primary-color)';
            item.style.color = 'white';
        }
    });

    // Efeito de fade-in para elementos ao rolar a página
    const fadeElements = document.querySelectorAll('.service-description, .portfolio-image');
    
    function checkFade() {
        fadeElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < window.innerHeight - elementVisible) {
                element.classList.add('visible');
            }
        });
    }

    // Adicionar classe para estilização CSS
    fadeElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transition = 'opacity 0.5s ease-in-out';
    });

    window.addEventListener('scroll', checkFade);
    checkFade(); // Verificar elementos visíveis no carregamento inicial
});
