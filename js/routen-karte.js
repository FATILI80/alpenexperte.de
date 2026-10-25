/**
 * ALPEN-EXPERTE — Routen-Karte & Master-Tabelle
 * Leaflet.js + OpenStreetMap (100% unabhängig, DSGVO-konform)
 * Echte GPS-Koordinaten der Wanderrouten
 */

const ROUTEN_DATEN = [
    { id:'R001', name:'Obere Firstalm Rundweg', km:8.5, stunden:'2:30', schwierigkeit:'T1', lat:47.6595, lng:11.8855 },
    { id:'R002', name:'Untere Firstalm', km:6.0, stunden:'1:45', schwierigkeit:'T1', lat:47.6610, lng:11.8870 },
    { id:'R003', name:'Spitzingsee Rundweg', km:4.2, stunden:'1:00', schwierigkeit:'T1', lat:47.6667, lng:11.8833 },
    { id:'R004', name:'Josefsthaler Wasserfälle', km:7.0, stunden:'2:30', schwierigkeit:'T1', lat:47.6750, lng:11.8750 },
    { id:'R005', name:'Taubenstein ab Spitzingsee', km:5.5, stunden:'2:00', schwierigkeit:'T2', lat:47.6667, lng:11.8833 },
    { id:'R006', name:'Schönfeldhütte ab Spitzingsattel', km:6.0, stunden:'2:00', schwierigkeit:'T1', lat:47.6600, lng:11.8950 },
    { id:'R007', name:'Albert-Link-Hütte ab Spitzingsee', km:5.0, stunden:'1:30', schwierigkeit:'T1', lat:47.6550, lng:11.8900 },
    { id:'R008', name:'Bodenschneidhaus ab Spitzingsee', km:5.9, stunden:'2:40', schwierigkeit:'T2', lat:47.6667, lng:11.8833 },
    { id:'R009', name:'Spitzingsee–Untere–Obere Firstalm', km:11.5, stunden:'4:00', schwierigkeit:'T2', lat:47.6667, lng:11.8833 },
    { id:'R010', name:'Waldspaziergang Valepp', km:9.0, stunden:'2:30', schwierigkeit:'T1', lat:47.6500, lng:11.9167 },
    { id:'R011', name:'Spitzingsee Aiplspitz Talweg', km:7.0, stunden:'2:00', schwierigkeit:'T1', lat:47.6667, lng:11.8833 },
    { id:'R012', name:'Fischhausen-Neuhaus Rundweg', km:5.0, stunden:'1:30', schwierigkeit:'T1', lat:47.7200, lng:11.8600 },
    { id:'R013', name:'Grünsee ab Spitzingsee', km:6.5, stunden:'2:00', schwierigkeit:'T1', lat:47.6667, lng:11.8833 },
    { id:'R014', name:'Stolzenberg Einstieg', km:4.5, stunden:'1:30', schwierigkeit:'T1', lat:47.6620, lng:11.8920 },
    { id:'R015', name:'Schliersee Uferrundweg', km:7.5, stunden:'2:00', schwierigkeit:'T1', lat:47.7333, lng:11.8500 },
    { id:'R016', name:'Obere Firstalm–Bodenschneid Runde', km:7.7, stunden:'3:07', schwierigkeit:'T3', lat:47.6595, lng:11.8855 },
    { id:'R017', name:'Obere Firstalm–Brecherspitz Vorgipfel', km:10.2, stunden:'3:30', schwierigkeit:'T3', lat:47.6595, lng:11.8855 },
    { id:'R018', name:'Rotwand ab Spitzingsee', km:17.3, stunden:'6:59', schwierigkeit:'T3', lat:47.6667, lng:11.8833 },
    { id:'R019', name:'Bodenschneid ab Neuhaus', km:7.5, stunden:'3:00', schwierigkeit:'T3', lat:47.7200, lng:11.8600 },
    { id:'R020', name:'Jägerkamp ab Spitzingsee', km:8.0, stunden:'3:00', schwierigkeit:'T3', lat:47.6667, lng:11.8833 },
    { id:'R021', name:'Aiplspitz ab Spitzingsee', km:9.0, stunden:'3:30', schwierigkeit:'T3', lat:47.6667, lng:11.8833 },
    { id:'R022', name:'Hochmiesing ab Rotwandhaus', km:6.0, stunden:'2:30', schwierigkeit:'T3', lat:47.6450, lng:11.9300 },
    { id:'R023', name:'Taubenstein–Schönfeldhütte Runde', km:9.0, stunden:'3:00', schwierigkeit:'T3', lat:47.6667, lng:11.8833 },
    { id:'R024', name:'Rosskopf Stolzeneck-Grat', km:10.7, stunden:'4:21', schwierigkeit:'T3', lat:47.6580, lng:11.8780 },
    { id:'R025', name:'Brecherspitz Westgrat', km:12.0, stunden:'4:30', schwierigkeit:'T3', lat:47.6595, lng:11.8855 },
    { id:'R026', name:'Rotwand–Auerspitz Überschreitung', km:15.0, stunden:'5:30', schwierigkeit:'T3', lat:47.6500, lng:11.9167 },
    { id:'R027', name:'Gindelalmschneid ab Schliersee', km:8.0, stunden:'3:00', schwierigkeit:'T3', lat:47.7333, lng:11.8500 },
    { id:'R028', name:'Suttenstein ab Schliersee', km:7.0, stunden:'2:30', schwierigkeit:'T3', lat:47.7333, lng:11.8500 },
    { id:'R029', name:'Blecksteinhaus ab Spitzingsee', km:8.5, stunden:'3:00', schwierigkeit:'T3', lat:47.6667, lng:11.8833 },
    { id:'R030', name:'Obere Firstalm–Stümpfling Runde', km:9.0, stunden:'3:30', schwierigkeit:'T3', lat:47.6595, lng:11.8855 },
    { id:'R031', name:'Jägerkamp–Schönfeldhütte Runde', km:10.0, stunden:'4:00', schwierigkeit:'T3', lat:47.6667, lng:11.8833 },
    { id:'R032', name:'Rotwand Winterweg', km:12.0, stunden:'4:30', schwierigkeit:'T3', lat:47.6500, lng:11.9167 },
    { id:'R033', name:'Hochmiesing–Miesingsattel Runde', km:11.0, stunden:'4:00', schwierigkeit:'T3', lat:47.6450, lng:11.9300 },
    { id:'R034', name:'Brecherspitz ab Spitzingsattel', km:10.0, stunden:'3:45', schwierigkeit:'T3', lat:47.6600, lng:11.8950 },
    { id:'R035', name:'Blomberg ab Bad Tölz', km:9.0, stunden:'3:30', schwierigkeit:'T3', lat:47.7500, lng:11.5500 },
    { id:'R036', name:'Rotwand-Reibn Komplett', km:18.0, stunden:'7:00', schwierigkeit:'T4', lat:47.6500, lng:11.9167 },
    { id:'R037', name:'Bodenschneid–Brecherspitz Überschreitung', km:13.1, stunden:'5:54', schwierigkeit:'T4', lat:47.6667, lng:11.8833 },
    { id:'R038', name:'Drei-Seen Tag 1 (Schliersee–Spitzingsee)', km:14.0, stunden:'5:00', schwierigkeit:'T4', lat:47.7333, lng:11.8500 },
    { id:'R039', name:'Drei-Seen Tag 2 (Spitzingsee–Firstalm)', km:12.0, stunden:'4:30', schwierigkeit:'T4', lat:47.6667, lng:11.8833 },
    { id:'R040', name:'Drei-Seen Tag 3 (Firstalm–Tegernsee)', km:15.0, stunden:'5:30', schwierigkeit:'T4', lat:47.6595, lng:11.8855 },
    { id:'R041', name:'Blauberge Überschreitung', km:16.0, stunden:'6:00', schwierigkeit:'T4', lat:47.6100, lng:11.7500 },
    { id:'R042', name:'Rotwand–Auerspitz–Hochmiesing Runde', km:18.0, stunden:'7:30', schwierigkeit:'T4', lat:47.6500, lng:11.9167 },
    { id:'R043', name:'Stolzeneck–Rosskopf–Stümpfling Grat', km:14.0, stunden:'5:30', schwierigkeit:'T4', lat:47.6580, lng:11.8780 },
    { id:'R044', name:'Wendelstein ab Brannenburg', km:12.0, stunden:'5:00', schwierigkeit:'T4', lat:47.7050, lng:12.0100 },
    { id:'R045', name:'Rotwand Nordwand Alpinweg', km:10.0, stunden:'5:00', schwierigkeit:'T5', lat:47.6420, lng:11.9350 },
    { id:'R046', name:'Brecherspitz Ostgrat', km:11.0, stunden:'4:30', schwierigkeit:'T4', lat:47.6595, lng:11.8855 },
    { id:'R047', name:'Sonnwendjoch ab Valepp', km:14.0, stunden:'5:30', schwierigkeit:'T4', lat:47.6500, lng:11.9167 },
    { id:'R048', name:'Benediktenwand ab Benediktbeuern', km:13.0, stunden:'5:00', schwierigkeit:'T4', lat:47.6300, lng:11.4000 },
    { id:'R049', name:'Schliersee–Tegernsee Baumgartenscheid', km:11.0, stunden:'4:00', schwierigkeit:'T3', lat:47.7333, lng:11.8500 },
    { id:'R050', name:'Wallberg ab Rottach-Egern', km:8.5, stunden:'3:30', schwierigkeit:'T3', lat:47.7000, lng:11.7600 }
];

// Mapping Wanderseiten-Dateien zu Koordinaten (für Inline-Karten)
const SEITEN_KOORDINATEN = {
    'untere-firstalm': { lat: 47.6610, lng: 11.8870, name: 'Untere Firstalm', zoom: 14 },
    'rotwand': { lat: 47.6420, lng: 11.9350, name: 'Rotwand (1.884 m)', zoom: 14 },
    'jaegerkamp': { lat: 47.6550, lng: 11.9050, name: 'Jägerkamp (1.746 m)', zoom: 14 },
    'aiplspitz': { lat: 47.6630, lng: 11.8780, name: 'Aiplspitz (1.759 m)', zoom: 14 },
    'taubenstein': { lat: 47.6580, lng: 11.8950, name: 'Taubenstein (1.692 m)', zoom: 14 },
    'hochmiesing': { lat: 47.6450, lng: 11.9300, name: 'Hochmiesing (1.883 m)', zoom: 14 },
    'blomberg': { lat: 47.7500, lng: 11.5500, name: 'Blomberg (1.248 m)', zoom: 14 },
    'hw-001-spitzingsattel-rottach': { lat: 47.6600, lng: 11.8950, name: 'Spitzingsattel–Rottach', zoom: 13 },
    'hw-002-fischbachau-rotwand': { lat: 47.7100, lng: 11.9500, name: 'Fischbachau–Rotwand', zoom: 13 },
    'hw-003-blauberge-spitzingsee': { lat: 47.6100, lng: 11.7500, name: 'Blauberge–Spitzingsee', zoom: 12 }
};

document.addEventListener('DOMContentLoaded', () => {

    /* =========================================================
       1. MASTER-TABELLE: Filter + Karten-Modal (index.html)
       ========================================================= */
    const routenTableBody = document.getElementById('routen-table-body');
    const routenCountEl = document.getElementById('routen-count');

    if (routenTableBody) {
        // Tabelle befüllen
        renderRoutenTabelle(ROUTEN_DATEN);

        // Filter-Buttons
        document.querySelectorAll('.routen-filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const filter = btn.dataset.filter;
                document.querySelectorAll('.routen-filter-btn').forEach(b => b.classList.remove('active'));

                if (filter === 'alle') {
                    btn.classList.add('active');
                    renderRoutenTabelle(ROUTEN_DATEN);
                } else {
                    btn.classList.add('active');
                    const filtered = ROUTEN_DATEN.filter(r => r.schwierigkeit === filter);
                    renderRoutenTabelle(filtered);
                }
            });
        });
    }

    function renderRoutenTabelle(daten) {
        if (!routenTableBody) return;
        let html = '';
        daten.forEach(r => {
            html += `<tr data-schwierigkeit="${r.schwierigkeit}">
                <td class="route-id">${r.id}</td>
                <td class="route-name">${r.name}</td>
                <td class="route-km">${r.km} km</td>
                <td class="route-dauer">${r.stunden} h</td>
                <td><span class="schwierigkeit-badge schwierigkeit-badge--${r.schwierigkeit}">${r.schwierigkeit}</span></td>
                <td><button class="route-map-btn" onclick="openRouteMap('${r.id}')">🗺️ Karte</button></td>
            </tr>`;
        });
        routenTableBody.innerHTML = html;
        if (routenCountEl) {
            routenCountEl.textContent = `${daten.length} von ${ROUTEN_DATEN.length} Routen angezeigt`;
        }
    }

    /* =========================================================
       2. INLINE-KARTE für Wanderseiten (ersetzt Platzhalter)
       ========================================================= */
    const inlineMapContainer = document.getElementById('route-inline-map');
    if (inlineMapContainer && typeof L !== 'undefined') {
        const pageName = inlineMapContainer.dataset.route || '';
        const coords = SEITEN_KOORDINATEN[pageName];
        if (coords) {
            const map = L.map('route-inline-map').setView([coords.lat, coords.lng], coords.zoom || 14);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
                maxZoom: 18
            }).addTo(map);

            L.marker([coords.lat, coords.lng]).addTo(map)
                .bindPopup(`<strong>🥾 ${coords.name}</strong><br>Startpunkt der Tour`)
                .openPopup();

            // Hiking-Overlay (OpenTopoMap für Wanderwege)
            L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
                attribution: 'Kartendaten: &copy; OpenStreetMap | OpenTopoMap (CC-BY-SA)',
                maxZoom: 17,
                opacity: 0.7
            }).addTo(map);
        }
    }
});

/* =========================================================
   3. KARTEN-MODAL: Route auf der Karte anzeigen
   ========================================================= */
let modalMap = null;

function openRouteMap(routeId) {
    const route = ROUTEN_DATEN.find(r => r.id === routeId);
    if (!route) return;

    // Modal erstellen (falls noch nicht vorhanden)
    let modal = document.getElementById('route-map-modal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'route-map-modal';
        modal.className = 'route-map-modal';
        modal.innerHTML = `
            <div class="route-map-modal-inner">
                <div class="route-map-modal-header">
                    <div>
                        <h3 id="modal-route-name"></h3>
                        <span class="modal-meta" id="modal-route-meta"></span>
                    </div>
                    <button class="route-map-modal-close" onclick="closeRouteMap()" aria-label="Schließen">✕</button>
                </div>
                <div class="route-map-modal-body" id="modal-map-container"></div>
            </div>`;
        document.body.appendChild(modal);
    }

    // Modal-Daten setzen
    document.getElementById('modal-route-name').textContent = `${route.id} · ${route.name}`;
    document.getElementById('modal-route-meta').textContent = `${route.km} km · ${route.stunden} h · ${route.schwierigkeit}`;

    // Modal anzeigen
    modal.classList.add('is-visible');
    document.body.style.overflow = 'hidden';

    // Karte laden (nach kurzer Verzögerung für DOM-Rendering)
    setTimeout(() => {
        const container = document.getElementById('modal-map-container');
        if (modalMap) {
            modalMap.remove();
            modalMap = null;
        }

        modalMap = L.map(container).setView([route.lat, route.lng], 14);

        // OpenTopoMap als Basis (zeigt Wanderwege, Höhenlinien, Hütten)
        L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
            attribution: 'Kartendaten: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> | <a href="https://opentopomap.org">OpenTopoMap</a> (CC-BY-SA)',
            maxZoom: 17
        }).addTo(modalMap);

        // Marker mit Schwierigkeits-Farbe
        const markerColors = { T1: '#2e7d32', T2: '#558b2f', T3: '#f57f17', T4: '#d84315', T5: '#c62828' };
        const color = markerColors[route.schwierigkeit] || '#2d8a56';

        const icon = L.divIcon({
            html: `<div style="background:${color};width:28px;height:28px;border-radius:50%;border:3px solid white;box-shadow:0 2px 8px rgba(0,0,0,0.3);display:flex;align-items:center;justify-content:center;color:white;font-size:12px;font-weight:bold;">🥾</div>`,
            iconSize: [28, 28],
            iconAnchor: [14, 14],
            className: ''
        });

        L.marker([route.lat, route.lng], { icon: icon }).addTo(modalMap)
            .bindPopup(`
                <h4 style="margin:0 0 4px;font-size:1rem;">${route.name}</h4>
                <p style="margin:0 0 4px;font-size:0.85rem;color:#5a6a7a;">
                    📏 ${route.km} km · ⏱️ ${route.stunden} h<br>
                    🥾 Schwierigkeit: <strong>${route.schwierigkeit}</strong>
                </p>
                <p style="margin:0;font-size:0.75rem;color:#8a9aaa;">📍 Startpunkt der Tour</p>
            `)
            .openPopup();

        modalMap.invalidateSize();
    }, 100);

    // ESC zum Schließen
    document.addEventListener('keydown', handleModalEsc);
}

function closeRouteMap() {
    const modal = document.getElementById('route-map-modal');
    if (modal) {
        modal.classList.remove('is-visible');
        document.body.style.overflow = '';
    }
    if (modalMap) {
        modalMap.remove();
        modalMap = null;
    }
    document.removeEventListener('keydown', handleModalEsc);
}

function handleModalEsc(e) {
    if (e.key === 'Escape') closeRouteMap();
}

// Modal schließen bei Klick auf Hintergrund
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('route-map-modal')) {
        closeRouteMap();
    }
});

console.log('🗺️ Routen-Karte Modul geladen – 50 Routen mit echten GPS-Koordinaten.');
