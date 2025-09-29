// Professional Investor Platform JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Property card hover effects
    const propertyCards = document.querySelectorAll('.property-card');
    propertyCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
            this.style.boxShadow = '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)';
        });
    });

    // Filter form enhancement
    const filterForm = document.querySelector('.filter-section form');
    if (filterForm) {
        // Auto-submit on filter change
        const filterInputs = filterForm.querySelectorAll('select, input');
        filterInputs.forEach(input => {
            input.addEventListener('change', function() {
                // Add loading state
                const submitBtn = filterForm.querySelector('button[type="submit"]');
                if (submitBtn) {
                    const originalText = submitBtn.innerHTML;
                    submitBtn.innerHTML = '<span class="loading"></span> Filtering...';
                    submitBtn.disabled = true;
                    
                    // Submit form after a short delay
                    setTimeout(() => {
                        filterForm.submit();
                    }, 300);
                }
            });
        });
    }

    // Investment metrics animation
    const metricValues = document.querySelectorAll('.metric-value');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const value = entry.target;
                const finalValue = value.textContent;
                const numericValue = parseFloat(finalValue.replace(/[^0-9.-]/g, ''));
                
                if (!isNaN(numericValue)) {
                    animateNumber(value, 0, numericValue, 1000, finalValue);
                }
            }
        });
    });

    metricValues.forEach(value => {
        observer.observe(value);
    });

    // Number animation function
    function animateNumber(element, start, end, duration, originalText) {
        const startTime = performance.now();
        const isPercentage = originalText.includes('%');
        const isCurrency = originalText.includes('$');
        
        function updateNumber(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            const current = start + (end - start) * progress;
            let displayValue = current.toFixed(2);
            
            if (isPercentage) {
                displayValue += '%';
            } else if (isCurrency) {
                displayValue = '$' + displayValue;
            }
            
            element.textContent = displayValue;
            
            if (progress < 1) {
                requestAnimationFrame(updateNumber);
            } else {
                element.textContent = originalText;
            }
        }
        
        requestAnimationFrame(updateNumber);
    }

    // Search functionality
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                // Implement live search here if needed
                console.log('Searching for:', this.value);
            }, 300);
        });
    }

    // Property comparison functionality
    const compareButtons = document.querySelectorAll('.compare-btn');
    const comparedProperties = [];
    
    compareButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const propertyId = this.dataset.propertyId;
            const propertyTitle = this.dataset.propertyTitle;
            
            if (comparedProperties.includes(propertyId)) {
                // Remove from comparison
                const index = comparedProperties.indexOf(propertyId);
                comparedProperties.splice(index, 1);
                this.textContent = 'Compare';
                this.classList.remove('btn-warning');
                this.classList.add('btn-outline-primary');
            } else {
                // Add to comparison
                if (comparedProperties.length < 3) {
                    comparedProperties.push(propertyId);
                    this.textContent = 'Remove from Compare';
                    this.classList.remove('btn-outline-primary');
                    this.classList.add('btn-warning');
                } else {
                    alert('You can compare up to 3 properties at once.');
                    return;
                }
            }
            
            updateComparisonUI();
        });
    });

    function updateComparisonUI() {
        const comparisonBadge = document.querySelector('.comparison-badge');
        if (comparisonBadge) {
            comparisonBadge.textContent = comparedProperties.length;
            comparisonBadge.style.display = comparedProperties.length > 0 ? 'inline' : 'none';
        }
    }

    // Investment calculator
    const calculatorForm = document.querySelector('.investment-calculator');
    if (calculatorForm) {
        calculatorForm.addEventListener('submit', function(e) {
            e.preventDefault();
            calculateInvestment();
        });
    }

    function calculateInvestment() {
        const propertyPrice = parseFloat(document.getElementById('property-price').value) || 0;
        const downPayment = parseFloat(document.getElementById('down-payment').value) || 0;
        const monthlyRent = parseFloat(document.getElementById('monthly-rent').value) || 0;
        const expenses = parseFloat(document.getElementById('expenses').value) || 0;
        
        const loanAmount = propertyPrice - downPayment;
        const monthlyPayment = loanAmount * 0.005; // Simplified calculation
        const netIncome = monthlyRent - monthlyPayment - expenses;
        const roi = (netIncome * 12) / downPayment * 100;
        
        // Display results
        document.getElementById('monthly-payment').textContent = '$' + monthlyPayment.toFixed(2);
        document.getElementById('net-income').textContent = '$' + netIncome.toFixed(2);
        document.getElementById('roi').textContent = roi.toFixed(2) + '%';
    }

    // Event registration
    const eventRegistrationForms = document.querySelectorAll('.event-registration');
    eventRegistrationForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.textContent = 'Registering...';
            submitBtn.disabled = true;
            
            // Simulate registration process
            setTimeout(() => {
                submitBtn.textContent = 'Registered!';
                submitBtn.classList.remove('btn-primary');
                submitBtn.classList.add('btn-success');
                
                // Show success message
                const alert = document.createElement('div');
                alert.className = 'alert alert-success alert-dismissible fade show';
                alert.innerHTML = `
                    <strong>Success!</strong> You have been registered for this event.
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                `;
                this.parentNode.insertBefore(alert, this);
            }, 1500);
        });
    });

    // Lazy loading for images
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => {
        imageObserver.observe(img);
    });

    // Mobile menu enhancement
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
        });
        
        // Close mobile menu when clicking on a link
        const navLinks = navbarCollapse.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navbarCollapse.classList.remove('show');
            });
        });
    }

    // Scroll to top functionality
    const scrollToTopBtn = document.createElement('button');
    scrollToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollToTopBtn.className = 'btn btn-primary position-fixed';
    scrollToTopBtn.style.cssText = `
        bottom: 2rem;
        right: 2rem;
        z-index: 1000;
        border-radius: 50%;
        width: 3rem;
        height: 3rem;
        display: none;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    `;
    document.body.appendChild(scrollToTopBtn);

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollToTopBtn.style.display = 'block';
        } else {
            scrollToTopBtn.style.display = 'none';
        }
    });

    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});
