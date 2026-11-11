document.addEventListener('DOMContentLoaded', function() {
    const w = document.getElementById('alpenexperte-calculator');
    if (!w) return;
    w.innerHTML = `
        <div class="calc-wrapper"><div class="calc-card"><div class="calc-header">
        <h3 class="calc-title">⚡ Interaktiver Touren- & Konditionsrechner</h3>
        <p class="calc-subtitle">Berechne Belastung, Kalorien und Hardware-Empfehlungen.</p></div>
        <div class="calc-body"><div class="calc-inputs">
        <div class="calc-field"><label class="calc-label">Sportart:</label>
        <select id="calcSport" class="calc-select"><option value="wandern">🥾 Wandern</option><option value="gravel">🚴 Gravel</option><option value="mtb">⚡ MTB</option><option value="klettern">🧗 Klettern</option></select></div>
        <div class="calc-field"><label class="calc-label">Gewicht: <span id="weightVal">75</span> kg</label><input type="range" id="calcWeight" class="calc-input" min="45" max="130" value="75"></div>
        <div class="calc-field"><label class="calc-label">Strecke: <span id="distVal">12</span> km</label><input type="range" id="calcDist" class="calc-input" min="2" max="60" value="12"></div>
        <div class="calc-field"><label class="calc-label">Höhenmeter: <span id="elevVal">800</span> m</label><input type="range" id="calcElev" class="calc-input" min="0" max="2500" value="800" step="50"></div></div>
        <div class="calc-results"><div class="calc-metrics-grid">
        <div class="calc-metric-box"><div class="calc-metric-title">Dauer</div><div class="calc-metric-value" id="resTime">3h 45m</div></div>
        <div class="calc-metric-box"><div class="calc-metric-title">Kalorien</div><div class="calc-metric-value" id="resCals">850 kcal</div></div>
        <div class="calc-metric-box"><div class="calc-metric-title">Wasser</div><div class="calc-metric-value" id="resWater">2.4 L</div></div>
        <div class="calc-metric-box"><div class="calc-metric-title">Score</div><div class="calc-metric-value" id="resScore">Moderat</div></div></div>
        <div class="calc-hardware-box"><div class="calc-hardware-title" id="hwTitle">🚴 Partner</div>
        <div class="calc-hardware-text" id="hwText">Passendes Equipment.</div>
        <a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" class="calc-btn-link" id="hwLink">Lucky Bike →</a></div></div></div></div></div>`;

    const se = document.getElementById('calcSport'), we = document.getElementById('calcWeight'), de = document.getElementById('calcDist'), ee = document.getElementById('calcElev');
    const wv = document.getElementById('weightVal'), dv = document.getElementById('distVal'), ev = document.getElementById('elevVal');
    const rt = document.getElementById('resTime'), rc = document.getElementById('resCals'), rw = document.getElementById('resWater'), rs = document.getElementById('resScore');
    const ht = document.getElementById('hwTitle'), hx = document.getElementById('hwText'), hl = document.getElementById('hwLink');

    function calc() {
        const s = se.value, w = parseFloat(we.value), d = parseFloat(de.value), h = parseFloat(ee.value);
        wv.textContent = w; dv.textContent = d; ev.textContent = h;
        let met = 5.5, sh = 4.0, sv = 400;
        if (s === 'gravel') { met = 8.0; sh = 16.0; sv = 500; }
        else if (s === 'mtb') { met = 8.0; sh = 12.0; sv = 600; }
        else if (s === 'klettern') { met = 7.0; sh = 2.5; sv = 300; }

        const th = Math.max(d / sh, h / sv) + 0.5 * Math.min(d / sh, h / sv);
        const hrs = Math.floor(th), mins = Math.round((th - hrs) * 60);
        const cals = Math.round((met * 3.5 * w / 200) * (th * 60));
        const water = (th * 0.5 + (h / 500) * 0.3).toFixed(1);

        rt.textContent = `${hrs}h ${mins}m`; rc.textContent = `${cals} kcal`; rw.textContent = `${water} L`;
        rs.textContent = th > 4 || h > 1000 ? "Schwer" : "Moderat";

        if (s === 'gravel') {
            ht.textContent = "⚡ Urwahn Gravel"; hx.textContent = "Edle Stahl-Gravelbikes."; hl.href = "https://www.awin1.com/cread.php?awinmid=68034&awinaffid=3134996&clickref=Calc&ued=https%3A%2F%2Falpenexperte.de"; hl.textContent = "Urwahn ansehen →";
        } else if (s === 'mtb') {
            ht.textContent = "🚵 Lucky Bike Fullys"; hx.textContent = "Top E-Mountainbikes."; hl.href = "https://www.lucky-bike.de/?ref=bb8ozi"; hl.textContent = "Lucky Bike ansehen →";
        } else if (s === 'klettern') {
            ht.textContent = "🧗 Amazon Kletter-Gear"; hx.textContent = "EN 958 Klettersteigsets."; hl.href = "https://www.amazon.de/s?k=klettersteigset&tag=bb8ozi-21"; hl.textContent = "Amazon ansehen →";
        } else {
            ht.textContent = "🥾 Amazon Stöcke"; hx.textContent = "Karbon-Stöcke entlasten."; hl.href = "https://www.amazon.de/s?k=karbon+wanderstoecke&tag=bb8ozi-21"; hl.textContent = "Amazon ansehen →";
        }
    }
    se.addEventListener('change', calc); we.addEventListener('input', calc); de.addEventListener('input', calc); ee.addEventListener('input', calc);
    calc();
});