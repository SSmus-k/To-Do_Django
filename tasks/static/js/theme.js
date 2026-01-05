// Theme switcher functionality
document.addEventListener('DOMContentLoaded', function() {
    const themeWarm = document.getElementById('theme-warm');
    const themeCool = document.getElementById('theme-cool');
    const themeDark = document.getElementById('theme-dark');
    const themeCustom = document.getElementById('theme-custom');
    const body = document.body;

    // Load saved theme
    const savedTheme = localStorage.getItem('theme');
    const savedCustomColor = localStorage.getItem('customColor');
    if (savedTheme) {
        body.setAttribute('data-theme', savedTheme);
    }
    if (savedCustomColor) {
        document.documentElement.style.setProperty('--primary-color', savedCustomColor);
        themeCustom.value = savedCustomColor;
    }

    // Theme switchers
    themeWarm.addEventListener('click', function() {
        setTheme('warm');
    });

    themeCool.addEventListener('click', function() {
        setTheme('cool');
    });

    themeDark.addEventListener('click', function() {
        setTheme('dark');
    });

    themeCustom.addEventListener('input', function() {
        const color = this.value;
        document.documentElement.style.setProperty('--primary-color', color);
        localStorage.setItem('customColor', color);
        body.setAttribute('data-theme', 'custom');
        localStorage.setItem('theme', 'custom');
    });

    function setTheme(theme) {
        body.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        // Reset custom color if switching to preset
        if (theme !== 'custom') {
            localStorage.removeItem('customColor');
        }
    }

    // Sidebar navigation active state
    const navItems = document.querySelectorAll('.nav-item');
    const urlParams = new URLSearchParams(window.location.search);
    const currentCategory = urlParams.get('category') || 'all';

    navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (href.includes(`category=${currentCategory}`)) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });

    // Smooth animations for interactions
    const cards = document.querySelectorAll('.activity-card, .habit-card, .reminder-card, .todo-item');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // To-do filter functionality
    const filterBtns = document.querySelectorAll('.filter-btn');
    const todoItems = document.querySelectorAll('.todo-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            const filter = this.getAttribute('data-filter');
            todoItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-status') === filter) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    // Right panel checklist functionality
    const checklistItems = document.querySelectorAll('.checklist input[type="checkbox"]');
    checklistItems.forEach(item => {
        item.addEventListener('change', function() {
            // Could save to localStorage or send to server
            console.log('Checklist item changed:', this.checked);
        });
    });
    
});