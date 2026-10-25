/**
 * ALPEN-EXPERTE — Wildschutz-Karte (interaktiv, Leaflet/OpenStreetMap)
 * Wildruhezonen, Schongebiete & Lebensraumkorridore im Mangfallgebirge
 * 100% DSGVO-konform (kein API-Key, keine externen Tracker)
 */

const WILDSCHUTZ_DATEN = {
    center: { lat: 47.665, lng: 11.895 },
    zoom: 12,
    schongebiete: [
        {
            name: 'NSR Rotwand–Taubenstein',
            desc: 'Kernzone: Gämsen, Birkhühner, Rothirsche – ganzjährig geschützt',
            coords: [
                [47.635, 11.920],
                [47.640, 11.935],
                [47.650, 11.940],
                [47.660, 11.925],
                [47.655, 11.910],
                [47.645, 11.905],
                [47.635, 11.920]
            ],
            farbe: '#c62828',
            regel: '❌ Wege nicht verlassen – Ganzjahres-Schongebiet'
        },
        {
            name: 'Valepp–Wildtierkorridor',
            desc: 'Verbindungskorridor Rotwand–Spitzingsee: Rothirsch, Reh, Dachs',
            coords: [
                [47.648, 11.908],
                [47.652, 11.912],
                [47.658, 11.906],
                [47.662, 11.895],
                [47.658, 11.885],
                [47.650, 11.888],
                [47.645, 11.898],
                [47.648, 11.908]
            ],
            farbe: '#e65100',
            regel: '🟠 Ruhezone Nov.–Apr. – Skitouren nur auf markierten Wegen'
        },
        {
            name: 'Brecherspitz–Westflanke',
            desc: 'Birkhuhn-Balzgebiet (März–Mai) & Gämsen-Einstände',
            coords: [
                [47.670, 11.880],
                [47.672, 11.888],
                [47.665, 11.892],
                [47.660, 11.888],
                [47.662, 11.880],
                [47.668, 11.877],
                [47.670, 11.880]
            ],
            farbe: '#d84315',
            regel: '🔴 Balzzeit (März–Mai) – Absolute Ruhe, Hunde anleinen!'
        }
    ],
    marker: [
        { lat: 47.650, lng: 11.916, name: '🚫 Wildruhezone Rotwand', icon: '🛑', typ: 'ruhezone' },
        { lat: 47.660, lng: 11.888, name: '🐦 Birkhuhn-Balzplatz Brecherspitz', icon: '🐦', typ: 'balz' },
        { lat: 47.655, lng: 11.905, name: '🦊 Wildtierkorridor Valepp', icon: '🦊', typ: 'korridor' },
        { lat: 47.668, lng: 11.883, name: '🏔️ Aussichtspunkt Brecherspitz (1.683 m)', icon: '🏔️', typ: 'aussicht' },
        { lat: 47.642, lng: 11.935, name: '🥾 Einstieg Rotwand-Tour', icon: '🥾', typ: 'einstieg' },
        { lat: 47.675, lng: 11.875, name: '🌲 Schongebiet Spitzingsee-Ost', icon: '🌲', typ: 'schongebiet' }
    ],
    infos: [
        { icon: '🛑', text: 'Wildruhezone – Betreten verboten (ganzjährig)' },
        { icon: '🟠', text: 'Saisonale Ruhezone – Skitouren auf markierten Wegen' },
        { icon: '🐦', text: 'Birkhuhn-Balzgebiet (März–Mai) besondere Rücksicht' },
        { icon: '🦊', text: 'Wildtierkorridor – Lebensraum-Verbindung' },
        { icon: '🥾', text: 'Wanderweg-Einstieg / empfohlener Zustieg' }
    ]
};

document.addEventListener('DOMContentLoaded', () => {
    const mapContainer = document.getElementById('wildschutz-map');
    if (!mapContainer || typeof L === 'undefined') return;

    // === KARTE INITIALISIEREN ===
    const map = L.map('wildschutz-map', {
        center: [WILDSCHUTZ_DATEN.center.lat, WILDSCHUTZ_DATEN.center.lng],
        zoom: WILDSCHUTZ_DATEN.zoom,
        zoomControl: true,
        scrollWheelZoom: true
    });

    // OpenTopoMap als Basis (zeigt Höhenlinien, Wälder, Almen)
    L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://openstreetmap.org">OSM</a> | <a href="https://opentopomap.org">OpenTopoMap</a> (CC-BY-SA)',
        maxZoom: 17
    }).addTo(map);

    // === SCHONGEBIETE (Polygone) ===
    WILDSCHUTZ_DATEN.schongebiete.forEach(zone => {
        const polygon = L.polygon(zone.coords, {
            color: zone.farbe,
            weight: 2,
            opacity: 0.8,
            fillColor: zone.farbe,
            fillOpacity: 0.12
        }).addTo(map);

        polygon.bindPopup(`
            <div style="min-width:200px;">
                <h4 style="margin:0 0 4px;font-size:1rem;color:${zone.farbe};">🛡️ ${zone.name}</h4>
                <p style="margin:0 0 6px;font-size:0.85rem;color:#3a4a5a;">${zone.desc}</p>
                <p style="margin:0;font-size:0.85rem;font-weight:600;color:#c62828;">${zone.regel}</p>
            </div>
        `);
    });

    // === MARKER (Punkte) ===
    WILDSCHUTZ_DATEN.marker.forEach(pt => {
        const icon = L.divIcon({
            html: `<div style="background:rgba(198,40,40,0.9);width:32px;height:32px;border-radius:50%;border:3px solid white;box-shadow:0 2px 8px rgba(0,0,0,0.4);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;">${pt.icon}</div>`,
            iconSize: [32, 32],
            iconAnchor: [16, 16],
            className: ''
        });

        const marker = L.marker([pt.lat, pt.lng], { icon: icon }).addTo(map);
        marker.bindPopup(`<strong style="font-size:0.9rem;">${pt.name}</strong>`);
    });

    // === LEGENDE ===
    const legend = L.control({ position: 'bottomright' });
    legend.onAdd = () => {
        const div = L.DomUtil.create('div', 'wildschutz-legend');
        div.style.cssText = 'background:white;padding:12px 16px;border-radius:8px;box-shadow:0 2px 12px rgba(0,0,0,0.15);font-size:0.8rem;line-height:1.6;max-width:220px;';
        let html = '<strong style="display:block;margin-bottom:6px;color:#c62828;">🛡️ Legende</strong>';
        WILDSCHUTZ_DATEN.infos.forEach(info => {
            html += `<div style="display:flex;align-items:center;gap:6px;"><span>${info.icon}</span><span>${info.text}</span></div>`;
        });
        div.innerHTML = html;
        return div;
    };
    legend.addTo(map);

    console.log('🦌 Wildschutz-Karte geladen – ' + WILDSCHUTZ_DATEN.schongebiete.length + ' Schongebiete, ' + WILDSCHUTZ_DATEN.marker.length + ' Marker');
});
