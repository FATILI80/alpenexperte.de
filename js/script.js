/**
 * ALPEN-EXPERTE — Main JavaScript
 * Mobile Navigation, sanfte Interaktionen & Performance
 */

document.addEventListener('DOMContentLoaded', () => {

    /* =========================================================
       1. MOBILE NAVIGATION
       ========================================================= */
    const navToggle = document.getElementById('navToggle');
    const mainNav = document.getElementById('mainNav');

    if (navToggle && mainNav) {
        navToggle.addEventListener('click', () => {
            const isOpen = mainNav.classList.toggle('is-open');
            navToggle.setAttribute('aria-expanded', isOpen);
            navToggle.setAttribute('aria-label', isOpen ? 'Menü schließen' : 'Menü öffnen');
        });

        // Navigation schließen bei Klick auf einen Link (Mobile)
        mainNav.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                mainNav.classList.remove('is-open');
                navToggle.setAttribute('aria-expanded', 'false');
                navToggle.setAttribute('aria-label', 'Menü öffnen');
            });
        });

        // Navigation schließen bei Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && mainNav.classList.contains('is-open')) {
                mainNav.classList.remove('is-open');
                navToggle.setAttribute('aria-expanded', 'false');
                navToggle.setAttribute('aria-label', 'Menü öffnen');
                navToggle.focus();
            }
        });
    }

    /* =========================================================
        1b. NAV DROPDOWN-TOGGLE (Mobile)
        ========================================================= */
    document.querySelectorAll('.nav-dropdown-toggle').forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            // Nur auf mobilen Geräten togglen (Dropdown ist sichtbar)
            if (window.innerWidth <= 768) {
                e.preventDefault();
                const dropdown = toggle.nextElementSibling;
                if (dropdown && dropdown.classList.contains('nav-dropdown')) {
                    const isOpen = dropdown.classList.toggle('is-open');
                    toggle.setAttribute('aria-expanded', isOpen);
                }
            }
        });

        // Desktop: aria-expanded anpassen bei hover
        const dropdown = toggle.nextElementSibling;
        if (dropdown && dropdown.classList.contains('nav-dropdown')) {
            toggle.parentElement.addEventListener('mouseenter', () => {
                if (window.innerWidth > 768) {
                    toggle.setAttribute('aria-expanded', 'true');
                }
            });
            toggle.parentElement.addEventListener('mouseleave', () => {
                if (window.innerWidth > 768) {
                    toggle.setAttribute('aria-expanded', 'false');
                }
            });
        }
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

    /* =========================================================
        9. LOKALE DNA — Zufallsfakt aus der Region anzeigen
        ========================================================= */
    const faktBanner = document.getElementById('lokalFaktBanner');
    if (faktBanner) {
        const faktText = faktBanner.querySelector('.lokal-fakt-text');
        const faktQuelle = faktBanner.querySelector('.lokal-fakt-quelle');
        const faktLabel = faktBanner.querySelector('.lokal-fakt-label');
        if (faktText) {
            faktBanner.classList.add('is-loading');
            fetch('/lokale_fakten.json')
                .then(function (response) {
                    if (!response.ok) throw new Error('Netzwerkfehler: ' + response.status);
                    return response.json();
                })
                .then(function (fakten) {
                    if (!fakten || fakten.length === 0) {
                        faktBanner.style.display = 'none';
                        return;
                    }
                    var zufall = fakten[Math.floor(Math.random() * fakten.length)];
                    faktText.textContent = zufall.fakt;

                    if (faktLabel) {
                        var kategorieLabels = {
                            'geschichte': 'Geschichte',
                            'natur': 'Natur & Umwelt',
                            'kultur': 'Kultur & Brauchtum',
                            'wandern': 'Wandern',
                            'huetten': 'Hütten',
                            'mtb': 'MTB',
                            'winter': 'Winter',
                            'oepnv': 'ÖPNV'
                        };
                        faktLabel.textContent = '🏔️ ' + (kategorieLabels[zufall.kategorie] || 'Wusstest du?');
                    }

                    if (faktQuelle) {
                        faktQuelle.innerHTML = 'Quelle: <a href="' + zufall.quelle_url + '" target="_blank" rel="noopener">' + zufall.quelle + '</a>';
                    }

                    faktBanner.classList.remove('is-loading');
                })
                .catch(function () {
                    faktBanner.style.display = 'none';
                });
        }
    }

    console.log('🏔️ Alpen-Experte — Initialisiert. DSGVO-konform, keine externen Server.');
});

/* =========================================================================
   System-Update B: Alpen-Karten-Interface (Leaflet.js)
   ========================================================================= */

(function () {
    'use strict';

    var karteEl = document.getElementById('alpenKarte');
    if (!karteEl) return; // Nur auf der Kartenseite

    // ------------------------------------------------------------------
    // POI-Daten
    // ------------------------------------------------------------------
    var poiData = [
        // --- Hütten ---
        {
            id: 'taubenstein-haus',
            name: 'Taubenstein-Haus',
            type: 'huette',
            icon: '🏠',
            lat: 47.6692,
            lng: 11.8880,
            desc: 'Berggasthof mit Sonnenterrasse, direkt an der Taubensteinbahn',
            url: '../huetten/index.html',
            category: 'huetten',
            family_friendly: true,
            oepnv: true,
            difficulty: 'easy',
            affiliate: true
        },
        {
            id: 'obere-firstalm',
            name: 'Obere Firstalm',
            type: 'huette',
            icon: '🍽️',
            lat: 47.6728,
            lng: 11.8792,
            desc: 'Bewirtschaftete Alm mit bayerischer Küche und Biergarten',
            url: '../huetten/wanderwege/obere-firstalm.html',
            category: 'huetten',
            family_friendly: true,
            oepnv: false,
            difficulty: 'easy',
            affiliate: false
        },
        {
            id: 'valepp',
            name: 'Valepp',
            type: 'huette',
            icon: '🌲',
            lat: 47.6347,
            lng: 11.8961,
            desc: 'Forsthaus Valepp – uriges Jägerhaus im Valepptal',
            url: '../huetten/wanderwege/valepp.html',
            category: 'huetten',
            family_friendly: true,
            oepnv: false,
            difficulty: 'moderate',
            affiliate: false
        },
        // --- BRB / ÖPNV-Stops ---
        {
            id: 'brb-schliersee',
            name: 'Bahnhof Schliersee (BRB)',
            type: 'brb',
            icon: '🚆',
            lat: 47.7359,
            lng: 11.8592,
            desc: 'BRB-Regiobahn München Hbf → Schliersee, ca. 50 Min.',
            url: '../praxis/oepnv-guide/index.html',
            category: 'oepnv',
            family_friendly: true,
            oepnv: true,
            difficulty: 'easy',
            affiliate: false
        },
        {
            id: 'brb-fischhausen',
            name: 'Bahnhof Fischhausen-Neuhaus (BRB)',
            type: 'brb',
            icon: '🚆',
            lat: 47.7250,
            lng: 11.8450,
            desc: 'BRB-Halt Fischhausen-Neuhaus, guter Zustieg für Tegernsee-Touren',
            url: '../praxis/oepnv-guide/index.html',
            category: 'oepnv',
            family_friendly: true,
            oepnv: true,
            difficulty: 'easy',
            affiliate: false
        },
        {
            id: 'bus-spitzingsee',
            name: 'Bus 356 – Spitzingsee',
            type: 'brb',
            icon: '🚌',
            lat: 47.6642,
            lng: 11.8850,
            desc: 'Buslinie 356: Schliersee Bahnhof → Spitzingsee (20 Min.)',
            url: '../praxis/oepnv-guide/index.html',
            category: 'oepnv',
            family_friendly: true,
            oepnv: true,
            difficulty: 'easy',
            affiliate: false
        },
        // --- Wander-Parkplätze ---
        {
            id: 'parkplatz-spitzingsee',
            name: 'Parkhaus Spitzingsee',
            type: 'parkplatz',
            icon: '🅿️',
            lat: 47.6640,
            lng: 11.8855,
            desc: 'Großes Parkhaus, ca. 8 €/Tag. Früh anreisen empfohlen!',
            url: '../praxis/oepnv-guide/index.html',
            category: 'parken',
            family_friendly: true,
            oepnv: false,
            difficulty: 'easy',
            affiliate: false
        },
        // --- Ausrüstungs-Verleih ---
        {
            id: 'intersport-spitzingsee',
            name: 'Intersport Spitzingsee',
            type: 'ausruestung',
            icon: '🎒',
            lat: 47.6655,
            lng: 11.8860,
            desc: 'Sportgeschäft mit Leihausrüstung: Ski, Snowboard, Schneeschuhe',
            url: '../ausruestung/index.html',
            category: 'ausruestung',
            family_friendly: true,
            oepnv: true,
            difficulty: 'easy',
            affiliate: true
        },
        // --- Wanderziele ---
        {
            id: 'rotwand-gipfel',
            name: 'Rotwand (1.884 m)',
            type: 'wandern',
            icon: '⛰️',
            lat: 47.6458,
            lng: 11.8894,
            desc: 'Aussichtsreicher Wander-/Skitouren-Gipfel. Anspruchsvoll.',
            url: '../wandern/rotwand.html',
            category: 'wandern',
            family_friendly: false,
            oepnv: false,
            difficulty: 'hard',
            affiliate: false
        },
        {
            id: 'taubenstein-gipfel',
            name: 'Taubenstein',
            type: 'wandern',
            icon: '⛰️',
            lat: 47.6681,
            lng: 11.8897,
            desc: 'Familienfreundlicher Gipfel mit Berggasthof und Klettersteig',
            url: '../wandern/taubenstein.html',
            category: 'wandern',
            family_friendly: true,
            oepnv: true,
            difficulty: 'moderate',
            affiliate: false
        },
        {
            id: 'brecherspitz-gipfel',
            name: 'Brecherspitz',
            type: 'wandern',
            icon: '⛰️',
            lat: 47.6805,
            lng: 11.8742,
            desc: 'Aussichtsberg über dem Spitzingsee',
            url: '../huetten/wanderwege/brecherspitz-gipfelweg.html',
            category: 'wandern',
            family_friendly: false,
            oepnv: false,
            difficulty: 'hard',
            affiliate: false
        },
        // --- MTB ---
        {
            id: 'mtb-drei-seen',
            name: 'Drei-Seen-Runde',
            type: 'mtb',
            icon: '🚵',
            lat: 47.6680,
            lng: 11.8700,
            desc: '24 km, S0–S1. Königs-Einsteigertour',
            url: '../mtb/drei-seen-runde.html',
            category: 'mtb',
            family_friendly: true,
            oepnv: false,
            difficulty: 'easy',
            affiliate: false
        }
    ];

    // ------------------------------------------------------------------
    // Filter-Kategorien
    // ------------------------------------------------------------------
    var activeFilter = 'all';
    var mapInstance = null;
    var markersLayer = null;
    var markers = [];

    function buildFilterButtons() {
        var container = document.getElementById('kartenFilter');
        if (!container) return;

        var filterDefs = [
            { value: 'all', label: '🗺️ Alle' },
            { value: 'huette', label: '🏠 Hütten' },
            { value: 'oepnv', label: '🚆 ÖPNV' },
            { value: 'wandern', label: '⛰️ Wandern' },
            { value: 'mtb', label: '🚵 MTB' },
            { value: 'parken', label: '🅿️ Parken' },
            { value: 'ausruestung', label: '🎒 Ausrüstung' }
        ];

        filterDefs.forEach(function (f) {
            var btn = document.createElement('button');
            btn.className = 'karten-filter-btn' + (f.value === 'all' ? ' is-active' : '');
            btn.textContent = f.label;
            btn.dataset.filter = f.value;
            btn.addEventListener('click', function () {
                setFilter(f.value);
            });
            container.appendChild(btn);
        });
    }

    function setFilter(value) {
        activeFilter = value;
        // Buttons aktualisieren
        var btns = document.querySelectorAll('.karten-filter-btn');
        btns.forEach(function (b) { b.classList.remove('is-active'); });
        var activeBtn = document.querySelector('.karten-filter-btn[data-filter="' + value + '"]');
        if (activeBtn) activeBtn.classList.add('is-active');
        renderPOIList();
        updateMapMarkers();
    }

    // ------------------------------------------------------------------
    // POI-Liste rendern
    // ------------------------------------------------------------------
    function filterPOI(data) {
        if (activeFilter === 'all') return data;
        return data.filter(function (p) { return p.category === activeFilter && p.type !== 'mtb' || p.type === activeFilter; });
    }

    function renderPOIList() {
        var container = document.getElementById('kartenPOIListe');
        if (!container) return;

        var gefiltert = poiData.filter(function (p) {
            return activeFilter === 'all' || p.category === activeFilter || p.type === activeFilter;
        });

        if (gefiltert.length === 0) {
            container.innerHTML = '<div class="karten-leer"><div class="karten-leer-icon">🔍</div><p>Keine POIs gefunden.</p></div>';
            return;
        }

        var html = '';
        gefiltert.forEach(function (poi) {
            var badgeHtml = poi.affiliate ? '<span class="karten-poi-badge">⭐ Affiliate</span>' : '';
            html += '<div class="karten-poi-card" data-poi-id="' + poi.id + '">';
            html += '    <div class="karten-poi-icon karten-poi-icon--' + poi.type + '">' + poi.icon + '</div>';
            html += '    <div class="karten-poi-body">';
            html += '        <h4>' + poi.name + '</h4>';
            html += '        <p>' + poi.desc + '</p>';
            html +=         badgeHtml;
            html += '    </div>';
            html += '</div>';
        });
        container.innerHTML = html;

        // Klick auf POI-Karte → Marker zentrieren + Popup öffnen
        container.querySelectorAll('.karten-poi-card').forEach(function (card) {
            card.addEventListener('click', function () {
                var id = this.dataset.poiId;
                var poi = poiData.find(function (p) { return p.id === id; });
                if (poi && mapInstance) {
                    mapInstance.setView([poi.lat, poi.lng], 14);
                    // Marker-Popup öffnen
                    markers.forEach(function (m) {
                        if (m.poiId === id) {
                            m.marker.openPopup();
                        }
                    });
                }
            });
        });
    }

    // ------------------------------------------------------------------
    // Leaflet-Karte initialisieren
    // ------------------------------------------------------------------
    function initMap() {
        if (mapInstance) return;

        // OpenStreetMap-Tiles (kostenlos, keine API-Key erforderlich)
        mapInstance = L.map('alpenKarte', {
            center: [47.668, 11.878],
            zoom: 13,
            zoomControl: true,
            fadeAnimation: true,
            zoomAnimation: true
        });

        // Basiskarte mit Cache-freundlichen Einstellungen
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap</a>',
            maxZoom: 18,
            minZoom: 10,
            detectRetina: true,
            keepBuffer: 8,
            updateWhenIdle: true,
            reuseTiles: true
        }).addTo(mapInstance);

        markersLayer = L.layerGroup().addTo(mapInstance);
        updateMapMarkers();
    }

    // ------------------------------------------------------------------
    // Marker aktualisieren
    // ------------------------------------------------------------------
    function updateMapMarkers() {
        if (!markersLayer) return;
        markersLayer.clearLayers();
        markers = [];

        var gefiltert = poiData.filter(function (p) {
            return activeFilter === 'all' || p.category === activeFilter || p.type === activeFilter;
        });

        gefiltert.forEach(function (poi) {
            var markerIcon = L.divIcon({
                className: 'alpen-marker-icon',
                html: poi.icon,
                iconSize: [32, 32],
                iconAnchor: [16, 16],
                popupAnchor: [0, -20]
            });

            var marker = L.marker([poi.lat, poi.lng], { icon: markerIcon }).addTo(markersLayer);

            var popupContent = '<h4>' + poi.icon + ' ' + poi.name + '</h4>';
            popupContent += '<p>' + poi.desc + '</p>';
            if (poi.url) {
                popupContent += '<a href="' + poi.url + '" class="popup-link">→ Mehr erfahren</a>';
            }
            if (poi.affiliate) {
                popupContent += '<div class="popup-affiliate-tag">⭐ Affiliate-Partner</div>';
            }

            marker.bindPopup(popupContent, { closeButton: true, maxWidth: 260 });

            markers.push({ poiId: poi.id, marker: marker });
        });
    }

    // ------------------------------------------------------------------
    // Initialisierung
    // ------------------------------------------------------------------
    buildFilterButtons();
    renderPOIList();
    initMap();

    // Fenstergrößenänderung: Karte neuzeichnen
    window.addEventListener('resize', function () {
        if (mapInstance) mapInstance.invalidateSize();
    });

})();
