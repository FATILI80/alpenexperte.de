/**
 * ALPEN-EXPERTE — Main JavaScript
 * Mobile Navigation, sanfte Interaktionen & Performance
 */

document.addEventListener('DOMContentLoaded', () => {

    /* =========================================================
        0. HEADER-SUCHE (Google Site Search)
       ========================================================= */
    const headerSearchForm = document.querySelector('.header-search');
    if (headerSearchForm) {
        headerSearchForm.addEventListener('submit', function(e) {
            const input = this.querySelector('.header-search-input');
            const hiddenQ = this.querySelector('input[name="q"]');
            const searchTerm = input ? input.value.trim() : '';
            if (searchTerm === '') {
                e.preventDefault();
                return false;
            }
            // Kombiniere site:alpenexperte.de mit dem Suchbegriff
            if (hiddenQ) {
                hiddenQ.value = 'site:alpenexperte.de ' + searchTerm;
            }
            // Entferne das q2-Feld (nur Dummy)
            const q2 = this.querySelector('input[name="q2"]');
            if (q2) q2.remove();
            return true;
        });
    }

    /* =========================================================
        1. MOBILE NAVIGATION
       ========================================================= */
    const navToggle = document.getElementById('navToggle');
    const mainNav = document.getElementById('mainNav');

    if (navToggle && mainNav) {
        const closeNav = () => {
            mainNav.classList.remove('is-open');
            mainNav.classList.remove('open');
            document.body.classList.remove('nav-open');
            navToggle.setAttribute('aria-expanded', 'false');
            navToggle.setAttribute('aria-label', 'MenÃ¼ Ã¶ffnen');
        };

        navToggle.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const isOpen = mainNav.classList.toggle('is-open');
            mainNav.classList.toggle('open', isOpen);
            document.body.classList.toggle('nav-open', isOpen);
            navToggle.setAttribute('aria-expanded', isOpen);
            navToggle.setAttribute('aria-label', isOpen ? 'MenÃ¼ schlieÃŸen' : 'MenÃ¼ Ã¶ffnen');
        });

        // Navigation schlieÃŸen bei Klick auf einen echten Link (Mobile)
        mainNav.querySelectorAll('a.nav-link, a.megamenu-item, .nav-dropdown a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 900) closeNav();
            });
        });

        // Klick ausserhalb schliesst (Mobile)
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 900 && mainNav.classList.contains('is-open')) {
                if (!mainNav.contains(e.target) && !navToggle.contains(e.target)) {
                    closeNav();
                }
            }
        });

        // Navigation schlieÃŸen bei Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && mainNav.classList.contains('is-open')) {
                closeNav();
                navToggle.focus();
            }
        });
    }

    /* =========================================================
        1b. NAV DROPDOWN-TOGGLE (Mobile)
        ========================================================= */
    document.querySelectorAll('.nav-dropdown-toggle').forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 900) {
                e.preventDefault();
                e.stopPropagation();
                const dropdown = toggle.nextElementSibling;
                if (dropdown && dropdown.classList.contains('nav-dropdown')) {
                    const isOpen = dropdown.classList.toggle('is-open');
                    toggle.setAttribute('aria-expanded', isOpen);
                }
            }
        });
    });
    /* =========================================================
        2. SMOOTH SCROLL FÜR ANCHOR-LINKS
       ========================================================= */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const targetId = anchor.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    /* 2b. SICHERUNG: Externe Links (z.B. Komoot) NIE abfangen - immer normal oeffnen */
    document.querySelectorAll('a[href^="http"]').forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.hasAttribute('target') && this.getAttribute('target') === '_blank') { return; }
            e.stopPropagation();
        }, true);
    });

    /* =========================================================
       3. INTERSECTION OBSERVER – Sanfte Animationen
       ========================================================= */
    const animateElements = document.querySelectorAll('.silo-card, .trust-item, .featured-layout');

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function revealElement(el) {
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
    }

    if (animateElements.length > 0 && 'IntersectionObserver' in window && !prefersReducedMotion) {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        revealElement(entry.target);
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0, rootMargin: '0px 0px 200px 0px' }
        );

        animateElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            observer.observe(el);
        });

        // Sicherheitsnetz: Nach 1,5 s alles einblenden, was noch unsichtbar ist
        setTimeout(() => {
            animateElements.forEach(el => {
                if (el.style.opacity === '0') {
                    revealElement(el);
                }
            });
        }, 1500);
    }

    /* =========================================================
       4. NEWSLETTER-FORMULAR (Platzhalter-Logik)
       ========================================================= */
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('newsletter-email');
            if (email && email.value.trim()) {
                // Platzhalter: Hier später Mailchimp/Kit-Anbindung
                const btn = newsletterForm.querySelector('.btn');
                const originalText = btn.textContent;
                btn.textContent = '✅ Anmeldung erfolgreich!';
                btn.disabled = true;
                email.value = '';
                setTimeout(() => {
                    btn.textContent = originalText;
                    btn.disabled = false;
                }, 3000);
            }
        });
    }

    /* =========================================================
       5. PERFORMANCE – Lazy Loading für Bilder sicherstellen
       ========================================================= */
    if ('loading' in HTMLImageElement.prototype) {
        // Native lazy loading wird vom Browser unterstützt (Fallback via HTML)
    } else {
        // Fallback: IntersectionObserver für Bild-LazyLoading
        const lazyImages = document.querySelectorAll('img[loading="lazy"]');
        if ('IntersectionObserver' in window && lazyImages.length > 0) {
            const imgObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.src; // Trigger native load
                        imgObserver.unobserve(img);
                    }
                });
            });
            lazyImages.forEach(img => imgObserver.observe(img));
        }
    }

    /* =========================================================
        6. JAHRESZAHL IM FOOTER AUTOMATISIEREN
        ========================================================= */
    const footerYear = document.querySelector('.site-footer p');
    if (footerYear) {
        const currentYear = new Date().getFullYear();
        footerYear.innerHTML = footerYear.innerHTML.replace('2025–2026', `2025–${currentYear}`);
    }

    /* =========================================================
        7. COOKIE-BANNER — DSGVO-konforme Einwilligung
        ========================================================= */
    const cookieBanner = document.getElementById('cookieBanner');
    const btnAccept = document.getElementById('cookieAccept');
    const btnDecline = document.getElementById('cookieDecline');

    function getCookie(name) {
        const match = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
        return match ? decodeURIComponent(match.pop()) : null;
    }

    function setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
        document.cookie = name + '=' + encodeURIComponent(value) +
            '; expires=' + date.toUTCString() +
            '; path=/; SameSite=Lax';
    }

    if (cookieBanner && !getCookie('cookie_consent')) {
        // Banner anzeigen mit leichter Verzögerung für flüssiges Rendering
        setTimeout(() => {
            cookieBanner.classList.add('is-visible');
        }, 500);
    }

    if (btnAccept) {
        btnAccept.addEventListener('click', () => {
            setCookie('cookie_consent', 'accepted', 365);
            cookieBanner.classList.remove('is-visible');
        });
    }

    if (btnDecline) {
        btnDecline.addEventListener('click', () => {
            setCookie('cookie_consent', 'declined', 30);
            cookieBanner.classList.remove('is-visible');
        });
    }

    /* =========================================================
        8. SIDEBAR DROPDOWN-TOGGLE
        ========================================================= */
    document.querySelectorAll('.sidebar-dropdown-toggle').forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault();
            const dropdown = toggle.nextElementSibling;
            if (dropdown && dropdown.classList.contains('sidebar-dropdown')) {
                const isOpen = dropdown.classList.toggle('is-open');
                toggle.setAttribute('aria-expanded', isOpen);
            }
        });

        // Auf mobilen Geräten: Dropdown geöffnet lassen, wenn aktiver Link enthalten
        const dropdown = toggle.nextElementSibling;
        if (dropdown && dropdown.classList.contains('sidebar-dropdown')) {
            const hasActive = dropdown.querySelector('.sidebar-link--active');
            if (hasActive) {
                dropdown.classList.add('is-open');
                toggle.setAttribute('aria-expanded', 'true');
            }
        }
    });

    console.log('🏔️ Alpen-Experte — Initialisiert. DSGVO-konform, keine externen Server.');

    /* =========================================================
        5. NEWS-TICKER — Laden aus /_news_ticker.html (absoluter Pfad)
           Automatische Filterung: Meldungen älter als 14 Tage werden ausgeblendet
       ========================================================= */
    const newsContainer = document.getElementById('news-ticker-container');
    if (newsContainer) {
        // Absoluter Pfad vom Root – funktioniert von jeder Unterseite
        const tickerUrl = '/_news_ticker.html';

        fetch(tickerUrl)
            .then(response => {
                if (!response.ok) throw new Error('News-Ticker nicht gefunden');
                return response.text();
            })
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const ticker = doc.getElementById('news-ticker');
                if (ticker) {
                    // Automatische Filterung: Meldungen älter als 14 Tage ausblenden
                    const now = new Date();
                    const maxAgeDays = 14;
                    ticker.querySelectorAll('.news-ticker-item').forEach(item => {
                        const dateEl = item.querySelector('.news-date');
                        if (dateEl) {
                            const dateStr = dateEl.textContent.trim(); // DD.MM.YYYY
                            const parts = dateStr.split('.');
                            if (parts.length === 3) {
                                const itemDate = new Date(parts[2], parts[1] - 1, parts[0]);
                                const diffDays = (now - itemDate) / (1000 * 60 * 60 * 24);
                                if (diffDays > maxAgeDays) {
                                    item.style.display = 'none';
                                }
                            }
                        }
                    });
                    newsContainer.appendChild(ticker);
                }
            })
            .catch(err => {
                console.warn('📢 News-Ticker konnte nicht geladen werden:', err.message);
            });
    }

    /* =========================================================
        9. LIVE-WETTER-WIDGET — Open-Meteo API (kostenlos, kein API-Key)
           Schliersee / Spitzingsee (47.71°N, 11.87°E)
       ========================================================= */
    const weatherWidget = document.getElementById('weather-widget');
    if (weatherWidget) {
        const lat = 47.710;
        const lon = 11.870;
        const apiUrl = 'https://api.open-meteo.com/v1/forecast'
            + '?latitude=' + lat
            + '&longitude=' + lon
            + '&current=temperature_2m,apparent_temperature,weather_code,wind_speed_10m,relative_humidity_2m'
            + '&daily=temperature_2m_max,temperature_2m_min,weather_code,wind_speed_10m_max'
            + '&timezone=Europe/Berlin'
            + '&forecast_days=3';

        // WMO Weather Codes → Deutsche Beschreibung + Icon
        function weatherIcon(code) {
            if (code === 0) return { icon: '☀️', text: 'Klarer Himmel' };
            if (code === 1) return { icon: '🌤️', text: 'Überwiegend sonnig' };
            if (code === 2) return { icon: '⛅', text: 'Teilweise bewölkt' };
            if (code === 3) return { icon: '☁️', text: 'Bedeckt' };
            if (code >= 45 && code <= 48) return { icon: '🌫️', text: 'Nebel/Dunst' };
            if (code >= 51 && code <= 55) return { icon: '🌦️', text: 'Nieselregen' };
            if (code >= 56 && code <= 57) return { icon: '🌨️', text: 'Gefrierender Niesel' };
            if (code >= 61 && code <= 65) return { icon: '🌧️', text: 'Regen' };
            if (code >= 66 && code <= 67) return { icon: '❄️', text: 'Gefrierender Regen' };
            if (code >= 71 && code <= 77) return { icon: '🌨️', text: 'Schneefall' };
            if (code >= 80 && code <= 82) return { icon: '🌦️', text: 'Regenschauer' };
            if (code >= 85 && code <= 86) return { icon: '🌨️', text: 'Schneeschauer' };
            if (code >= 95) return { icon: '⛈️', text: 'Gewitter' };
            return { icon: '🌤️', text: 'Unbeständig' };
        }

        function dayName(dateStr) {
            const d = new Date(dateStr + 'T12:00:00');
            const today = new Date();
            const tomorrow = new Date(today);
            tomorrow.setDate(tomorrow.getDate() + 1);
            if (d.toDateString() === today.toDateString()) return 'Heute';
            if (d.toDateString() === tomorrow.toDateString()) return 'Morgen';
            return d.toLocaleDateString('de-DE', { weekday: 'long' });
        }

        fetch(apiUrl)
            .then(res => {
                if (!res.ok) throw new Error('HTTP ' + res.status);
                return res.json();
            })
            .then(data => {
                const current = data.current;
                const daily = data.daily;
                const currWeather = weatherIcon(current.weather_code);

                let html = '<div class="weather-grid" style="display: grid; grid-template-columns: 1fr 2fr; gap: var(--space-md); align-items: stretch;">';

                // ── Current weather card ──
                html += '<div class="weather-current" style="background: linear-gradient(135deg, var(--color-primary-dark), var(--color-primary)); color: var(--color-white); border-radius: var(--radius-lg); padding: var(--space-lg); text-align: center;">';
                html += '<div style="font-size: 3rem; margin-bottom: var(--space-xs);">' + currWeather.icon + '</div>';
                html += '<div style="font-size: 2.5rem; font-weight: 700; line-height: 1.1;">' + Math.round(current.temperature_2m) + '°C</div>';
                html += '<div style="font-size: 0.9rem; opacity: 0.9; margin-top: var(--space-xs);">' + currWeather.text + '</div>';
                html += '<div style="font-size: 0.8rem; opacity: 0.75; margin-top: var(--space-sm);">';
                html += 'Gefühlt: ' + Math.round(current.apparent_temperature) + '°C &nbsp;|&nbsp; Wind: ' + Math.round(current.wind_speed_10m) + ' km/h</div>';
                html += '</div>';

                // ── 3-day forecast ──
                html += '<div class="weather-forecast" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-sm);">';
                for (let i = 0; i < 3; i++) {
                    const dayWeather = weatherIcon(daily.weather_code[i]);
                    html += '<div class="weather-day" style="background: var(--color-surface); border-radius: var(--radius-md); padding: var(--space-md); text-align: center; border: 1px solid var(--color-border);">';
                    html += '<div style="font-weight: 600; font-size: 0.85rem; margin-bottom: var(--space-xs);">' + dayName(daily.time[i]) + '</div>';
                    html += '<div style="font-size: 1.75rem; margin-bottom: var(--space-xs);">' + dayWeather.icon + '</div>';
                    html += '<div style="font-size: 0.85rem; color: var(--color-text-light);">' + dayWeather.text + '</div>';
                    html += '<div style="font-size: 1.1rem; font-weight: 600; margin-top: var(--space-xs);">' + Math.round(daily.temperature_2m_max[i]) + '° / ' + Math.round(daily.temperature_2m_min[i]) + '°</div>';
                    html += '<div style="font-size: 0.75rem; color: var(--color-text-light); margin-top: var(--space-xs);">💨 ' + Math.round(daily.wind_speed_10m_max[i]) + ' km/h</div>';
                    html += '</div>';
                }
                html += '</div>';

                html += '</div>'; // close weather-grid

                weatherWidget.innerHTML = html;
            })
            .catch(err => {
                weatherWidget.innerHTML = '<div style="text-align: center; padding: var(--space-lg); color: var(--color-text-light);">'
                    + '<p style="font-size: 1.5rem; margin-bottom: var(--space-sm);">⚠️</p>'
                    + '<p>Wetterdaten konnten nicht geladen werden.</p>'
                    + '<p style="font-size: 0.8rem; margin-top: var(--space-xs);">(' + err.message + ')</p>'
                    + '</div>';
                console.warn('🌤️ Wetter-Widget Fehler:', err.message);
            });
    }

    /* =========================================================
        10. DYNAMISCHER DATUMSTEMPEL (Google Freshness Signal)
        ========================================================= */
    const dateSpan = document.getElementById('current-update-date');
    if (dateSpan) {
        const now = new Date();
        const formatted = now.toLocaleDateString('de-DE', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric'
        });
        dateSpan.textContent = formatted;
        console.log('📅 Datumstempel aktualisiert: ' + formatted);
    }
});


// ===== READ-MORE / ACCORDION (Mobile) =====
document.addEventListener('DOMContentLoaded', function() {
    if (window.innerWidth <= 768) {
        document.querySelectorAll('.section-desc, .silo-card-text').forEach(function(el) {
            if (el.textContent.length > 120) {
                var wrap = document.createElement('div');
                wrap.className = 'read-more-wrap';
                el.parentNode.insertBefore(wrap, el);
                wrap.appendChild(el);
                
                var fade = document.createElement('div');
                fade.className = 'read-more-fade';
                wrap.appendChild(fade);
                
                var btn = document.createElement('button');
                btn.className = 'read-more-btn';
                btn.textContent = 'Weiterlesen …';
                btn.type = 'button';
                btn.addEventListener('click', function() {
                    wrap.classList.toggle('expanded');
                    btn.textContent = wrap.classList.contains('expanded') ? 'Weniger anzeigen' : 'Weiterlesen …';
                });
                wrap.parentNode.insertBefore(btn, wrap.nextSibling);
            }
        });
    }
});

// ===== Back-to-Top Button =====
(function() {
    const btn = document.getElementById('backToTop');
    if (!btn) return;
    const checkScroll = function() {
        if (window.scrollY > 500) {
            btn.classList.add('visible');
        } else {
            btn.classList.remove('visible');
        }
    };
    window.addEventListener('scroll', checkScroll, { passive: true });
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    checkScroll();
})();
