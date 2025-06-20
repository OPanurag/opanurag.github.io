// JavaScript for Portfolio Website Interactivity

// Wait for DOM to be fully loaded before executing scripts
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all interactive features
    initializeNavigation();
    initializeScrollEffects();
    initializeContactForm();
    initializeAnimations();
    initializeTypingEffect();
    
});

/**
 * Navigation functionality including mobile menu toggle and smooth scrolling
 */
function initializeNavigation() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Toggle mobile menu when hamburger is clicked
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }
    
    // Close mobile menu when a nav link is clicked
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });
    
    // Add active class to current section in navigation
    window.addEventListener('scroll', function() {
        let current = '';
        const sections = document.querySelectorAll('section');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').substring(1) === current) {
                link.classList.add('active');
            }
        });
    });
}

/**
 * Scroll effects including navbar background change and scroll-to-top button
 */
function initializeScrollEffects() {
    const navbar = document.querySelector('.navbar');
    
    // Change navbar background on scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Create and handle scroll-to-top button
    createScrollToTopButton();
}

/**
 * Create scroll-to-top button functionality
 */
function createScrollToTopButton() {
    // Create scroll-to-top button element
    const scrollButton = document.createElement('button');
    scrollButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollButton.className = 'scroll-to-top';
    scrollButton.setAttribute('aria-label', 'Scroll to top');
    
    // Add CSS styles for the button
    const buttonStyles = `
        .scroll-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: var(--primary-color);
            color: white;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            font-size: 1.2rem;
            box-shadow: var(--shadow-lg);
            transition: var(--transition);
            opacity: 0;
            visibility: hidden;
            z-index: 1000;
        }
        
        .scroll-to-top.visible {
            opacity: 1;
            visibility: visible;
        }
        
        .scroll-to-top:hover {
            background: var(--secondary-color);
            transform: translateY(-3px);
        }
    `;
    
    // Add styles to document if not already present
    if (!document.querySelector('#scroll-button-styles')) {
        const styleSheet = document.createElement('style');
        styleSheet.id = 'scroll-button-styles';
        styleSheet.textContent = buttonStyles;
        document.head.appendChild(styleSheet);
    }
    
    document.body.appendChild(scrollButton);
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            scrollButton.classList.add('visible');
        } else {
            scrollButton.classList.remove('visible');
        }
    });
    
    // Scroll to top when button is clicked
    scrollButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * Contact form handling with validation and submission
 */
function initializeContactForm() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(contactForm);
            const formObject = {};
            
            // Convert FormData to object
            for (let [key, value] of formData.entries()) {
                formObject[key] = value;
            }
            
            // Validate form
            if (validateContactForm(formObject)) {
                // Show loading state
                showFormLoading(true);
                
                // Simulate form submission (replace with actual API call)
                setTimeout(() => {
                    showFormLoading(false);
                    showFormSuccess();
                    contactForm.reset();
                }, 2000);
            }
        });
    }
}

/**
 * Validate contact form data
 * @param {Object} data - Form data object
 * @returns {boolean} - Validation result
 */
function validateContactForm(data) {
    const errors = [];
    
    // Validate required fields
    if (!data.name || data.name.trim().length < 2) {
        errors.push('Name must be at least 2 characters long');
    }
    
    if (!data.email || !isValidEmail(data.email)) {
        errors.push('Please enter a valid email address');
    }
    
    if (!data.subject) {
        errors.push('Please select a subject');
    }
    
    if (!data.message || data.message.trim().length < 10) {
        errors.push('Message must be at least 10 characters long');
    }
    
    // Display errors if any
    if (errors.length > 0) {
        showFormErrors(errors);
        return false;
    }
    
    return true;
}

/**
 * Validate email format
 * @param {string} email - Email address to validate
 * @returns {boolean} - Validation result
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Show form loading state
 * @param {boolean} loading - Loading state
 */
function showFormLoading(loading) {
    const submitButton = document.querySelector('#contactForm button[type="submit"]');
    const form = document.getElementById('contactForm');
    
    if (loading) {
        submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        submitButton.disabled = true;
        form.classList.add('loading');
    } else {
        submitButton.innerHTML = 'Send Message';
        submitButton.disabled = false;
        form.classList.remove('loading');
    }
}

/**
 * Show form success message
 */
function showFormSuccess() {
    showNotification('Message sent successfully! I\'ll get back to you soon.', 'success');
}

/**
 * Show form validation errors
 * @param {Array} errors - Array of error messages
 */
function showFormErrors(errors) {
    const errorMessage = errors.join('<br>');
    showNotification(errorMessage, 'error');
}

/**
 * Show notification message
 * @param {string} message - Notification message
 * @param {string} type - Notification type (success, error, info)
 */
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <span class="notification-message">${message}</span>
            <button class="notification-close" aria-label="Close notification">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `;
    
    // Add notification styles if not present
    addNotificationStyles();
    
    // Add to document
    document.body.appendChild(notification);
    
    // Show notification with animation
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        hideNotification(notification);
    }, 5000);
    
    // Handle close button click
    const closeButton = notification.querySelector('.notification-close');
    closeButton.addEventListener('click', () => {
        hideNotification(notification);
    });
}

/**
 * Hide notification with animation
 * @param {Element} notification - Notification element to hide
 */
function hideNotification(notification) {
    notification.classList.remove('show');
    setTimeout(() => {
        if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
        }
    }, 300);
}

/**
 * Add notification styles to document
 */
function addNotificationStyles() {
    if (document.querySelector('#notification-styles')) return;
    
    const styles = `
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            max-width: 400px;
            background: white;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-xl);
            z-index: 10000;
            transform: translateX(100%);
            transition: transform 0.3s ease;
        }
        
        .notification.show {
            transform: translateX(0);
        }
        
        .notification-success {
            border-left: 4px solid #10b981;
        }
        
        .notification-error {
            border-left: 4px solid #ef4444;
        }
        
        .notification-info {
            border-left: 4px solid var(--primary-color);
        }
        
        .notification-content {
            padding: 1rem;
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
        }
        
        .notification-message {
            flex: 1;
            margin-right: 1rem;
            line-height: 1.5;
        }
        
        .notification-close {
            background: none;
            border: none;
            cursor: pointer;
            color: var(--text-secondary);
            font-size: 1rem;
            padding: 0;
            width: 20px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .notification-close:hover {
            color: var(--text-primary);
        }
    `;
    
    const styleSheet = document.createElement('style');
    styleSheet.id = 'notification-styles';
    styleSheet.textContent = styles;
    document.head.appendChild(styleSheet);
}

/**
 * Initialize scroll-triggered animations
 */
function initializeAnimations() {
    // Create intersection observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.skill-category, .project-card, .timeline-card, .contact-item');
    animateElements.forEach(el => {
        observer.observe(el);
    });
    
    // Add CSS for animations
    addAnimationStyles();
}

/**
 * Add animation styles to document
 */
function addAnimationStyles() {
    if (document.querySelector('#animation-styles')) return;
    
    const styles = `
        .skill-category,
        .project-card,
        .timeline-card,
        .contact-item {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        
        .skill-category.animate,
        .project-card.animate,
        .timeline-card.animate,
        .contact-item.animate {
            opacity: 1;
            transform: translateY(0);
        }
        
        .experience-column .timeline-card {
            transform: translateX(-30px);
        }
        
        .achievements-column .timeline-card {
            transform: translateX(30px);
        }
        
        .experience-column .timeline-card.animate,
        .achievements-column .timeline-card.animate {
            transform: translateY(0);
        }
    `;
    
    const styleSheet = document.createElement('style');
    styleSheet.id = 'animation-styles';
    styleSheet.textContent = styles;
    document.head.appendChild(styleSheet);
}

/**
 * Initialize typing effect for hero section
 */
function initializeTypingEffect() {
    const typingElement = document.querySelector('.hero-subtitle');
    if (!typingElement) return;
    
    const texts = [
        'Data Science Graduate | Machine Learning Enthusiast',
        'Python Developer | Statistical Analyst',
        'AI Researcher | Data Visualization Expert',
        'Problem Solver | Innovation Driver'
    ];
    
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 100;
    
    function typeText() {
        const currentText = texts[textIndex];
        
        if (isDeleting) {
            // Remove characters
            typingElement.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
            typingSpeed = 50;
        } else {
            // Add characters
            typingElement.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
            typingSpeed = 100;
        }
        
        // Check if word is complete
        if (!isDeleting && charIndex === currentText.length) {
            // Pause before deleting
            typingSpeed = 2000;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            // Move to next text
            isDeleting = false;
            textIndex = (textIndex + 1) % texts.length;
            typingSpeed = 500;
        }
        
        setTimeout(typeText, typingSpeed);
    }
    
    // Start typing effect after a delay
    setTimeout(typeText, 1000);
}

/**
 * Utility function to debounce function calls
 * @param {Function} func - Function to debounce
 * @param {number} wait - Wait time in milliseconds
 * @returns {Function} - Debounced function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Utility function to throttle function calls
 * @param {Function} func - Function to throttle
 * @param {number} limit - Time limit in milliseconds
 * @returns {Function} - Throttled function
 */
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

/**
 * Handle project card interactions
 */
function initializeProjectCards() {
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        // Add click tracking for analytics (if needed)
        card.addEventListener('click', function(e) {
            // Only track if clicking on the card itself, not links
            if (!e.target.closest('.project-link')) {
                console.log('Project card clicked:', card.querySelector('h3').textContent);
            }
        });
        
        // Add keyboard navigation support
        card.setAttribute('tabindex', '0');
        card.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                const firstLink = card.querySelector('.project-link');
                if (firstLink) {
                    firstLink.click();
                }
            }
        });
    });
}

/**
 * Initialize skill tag interactions
 */
function initializeSkillTags() {
    const skillTags = document.querySelectorAll('.skill-tag');
    
    skillTags.forEach(tag => {
        tag.addEventListener('click', function() {
            // Add visual feedback for skill selection
            tag.classList.toggle('selected');
            
            // Could be used to filter projects by skill
            const skill = tag.textContent.trim();
            console.log('Skill selected:', skill);
        });
    });
}

/**
 * Initialize lazy loading for images
 */
function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

/**
 * Handle keyboard navigation for accessibility
 */
function initializeKeyboardNavigation() {
    // Skip to main content link
    const skipLink = document.createElement('a');
    skipLink.href = '#main';
    skipLink.textContent = 'Skip to main content';
    skipLink.className = 'skip-link';
    
    // Add skip link styles
    const skipLinkStyles = `
        .skip-link {
            position: absolute;
            top: -40px;
            left: 6px;
            background: var(--primary-color);
            color: white;
            padding: 8px;
            text-decoration: none;
            border-radius: 4px;
            z-index: 10000;
            transition: top 0.3s;
        }
        
        .skip-link:focus {
            top: 6px;
        }
    `;
    
    if (!document.querySelector('#skip-link-styles')) {
        const styleSheet = document.createElement('style');
        styleSheet.id = 'skip-link-styles';
        styleSheet.textContent = skipLinkStyles;
        document.head.appendChild(styleSheet);
    }
    
    document.body.insertBefore(skipLink, document.body.firstChild);
    
    // Add main landmark
    const heroSection = document.getElementById('home');
    if (heroSection) {
        heroSection.setAttribute('role', 'main');
        heroSection.id = 'main';
    }
}

/**
 * Initialize performance monitoring
 */
function initializePerformanceMonitoring() {
    // Monitor page load performance
    window.addEventListener('load', function() {
        setTimeout(() => {
            const perfData = performance.getEntriesByType('navigation')[0];
            console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
        }, 0);
    });
    
    // Monitor scroll performance
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        if (!scrollTimeout) {
            scrollTimeout = setTimeout(() => {
                scrollTimeout = null;
                // Scroll performance monitoring could go here
            }, 100);
        }
    });
}

// Initialize additional features when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initializeProjectCards();
    initializeSkillTags();
    initializeLazyLoading();
    initializeKeyboardNavigation();
    initializePerformanceMonitoring();
});

// Handle page visibility changes
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        // Page is hidden - pause animations, etc.
        console.log('Page hidden');
    } else {
        // Page is visible - resume animations, etc.
        console.log('Page visible');
    }
});

// Handle online/offline status
window.addEventListener('online', function() {
    showNotification('Connection restored', 'success');
});

window.addEventListener('offline', function() {
    showNotification('Connection lost. Some features may not work.', 'error');
});



// Export functions for potential external use
window.portfolioUtils = {
    showNotification,
    debounce,
    throttle
};