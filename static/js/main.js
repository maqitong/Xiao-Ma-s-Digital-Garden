document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initHeroCarousel();
    initStatsCounter();
});

// 1. Scroll Animations
function initScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.remove('opacity-0', 'translate-y-8');
                entry.target.classList.add('opacity-100', 'translate-y-0');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    animatedElements.forEach(el => {
        // Ensure initial state is hidden if not already (for elements we might have cleaned)
        // But mostly we rely on the HTML having 'opacity-0 translate-y-8'
        // If an element is missing opacity-0 but has animate-on-scroll, force it?
        // Let's just observe.
        observer.observe(el);
    });
}

// 2. Hero Carousel (Home Page)
function initHeroCarousel() {
    const slides = document.querySelectorAll('.relative.min-h-screen .absolute.inset-0 > div.transition-opacity');
    if (slides.length === 0) return;

    let currentSlide = 0;
    const interval = 4000; // 4 seconds

    // Initialize: ensure first is visible, others hidden
    // The HTML structure usually has opacity-0 for hidden slides and opacity-100 for active
    // We'll manage classes manually to be safe.

    // Check if we need to set initial state
    // The existing HTML seems to have one opacity-100 and others opacity-0.

    setInterval(() => {
        // Fade out current
        slides[currentSlide].classList.remove('opacity-100');
        slides[currentSlide].classList.add('opacity-0');

        // Next slide
        currentSlide = (currentSlide + 1) % slides.length;

        // Fade in next
        slides[currentSlide].classList.remove('opacity-0');
        slides[currentSlide].classList.add('opacity-100');
    }, interval);
}

// 3. Stats Counter (Home Page)
function initStatsCounter() {
    const statsSection = document.querySelector('.stats-section');
    if (!statsSection) return;

    const stats = [
        { el: statsSection.children[0]?.querySelector('.text-4xl'), target: 5, suffix: '+' },
        { el: statsSection.children[1]?.querySelector('.text-4xl'), target: 20, suffix: '+' },
        { el: statsSection.children[2]?.querySelector('.text-4xl'), target: 50, suffix: '+' },
        { el: statsSection.children[3]?.querySelector('.text-4xl'), target: 30, suffix: '+' }
    ];

    let started = false;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !started) {
                started = true;
                stats.forEach(stat => {
                    if (stat.el) animateValue(stat.el, 0, stat.target, 2000, stat.suffix);
                });
            }
        });
    });

    observer.observe(statsSection);
}

function animateValue(obj, start, end, duration, suffix) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = Math.floor(progress * (end - start) + start) + suffix;
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}
