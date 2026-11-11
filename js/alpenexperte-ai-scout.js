/**
 * ALPENEXPERTE AI & GEAR SCOUT — Universal Conversational AI Engine
 */
window.alpenTracking = {
    track: function(cat, act, lbl) {
        try {
            const d = JSON.parse(localStorage.getItem('alpen_events') || '[]');
            d.push({ time: new Date().toISOString(), cat, act, lbl, page: location.pathname });
            localStorage.setItem('alpen_events', JSON.stringify(d));
        } catch(e) {}
    },
    getStats: function() { try { const d = JSON.parse(localStorage.getItem('alpen_events') || '[]'); console.table(d); return d; } catch(e) { return []; } }
};

window.alpenSwitchTab = function(tabName) {
    document.querySelectorAll('.ai-scout-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.ai-scout-panel').forEach(p => p.classList.remove('active'));
    const btn = document.querySelector(`[data-tab="${tabName}"]`);
    const panel = document.getElementById('panel-' + tabName);
    if (btn) btn.classList.add('active');
    if (panel) panel.classList.add('active');
    window.alpenTracking.track('scout_tab', 'switch', tabName);
};

window.alpenSendChat = function() {
    const input = document.getElementById('aiChatInput');
    const cb = document.getElementById('aiChatBox');
    if (!input || !cb) return;
    const t = input.value.trim();
    if (!t) return;

    const userDiv = document.createElement('div');
    userDiv.className = 'ai-msg user';
    userDiv.textContent = t;
    cb.appendChild(userDiv);
    input.value = '';
    cb.scrollTop = cb.scrollHeight;
    window.alpenTracking.track('chat', 'query', t);

    const lid = 'l-' + Date.now();
    const ld = document.createElement('div');
    ld.className = 'ai-msg bot';
    ld.id = lid;
    ld.innerHTML = '<em>Denke nach...</em>';
    cb.appendChild(ld);
    cb.scrollTop = cb.scrollHeight;

    const q = t.toLowerCase();
    let reply = "";
    let productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Alpenexperte Outdoor Shop</strong><span>Ausrüstung & Empfehlungen</span></div><a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ansehen →</a></div>`;

    if (q.includes('hallo') || q.includes('servus') || q.includes('hi') || q.includes('guten tag')) {
        reply = "Servus! Ich bin dein persönlicher KI-Bergführer für das Mangfallgebirge und den Spitzingsee. Mit mir kannst du über absolut alles reden – egal ob Touren, Wetter, Ausrüstung oder Alltagsthemen. Was gibt's Neues?";
    } else if (q.includes('wetter') || q.includes('regnet') || q.includes('sonne')) {
        reply = "Das Bergwetter in den Voralpen ist oft dynamisch. Open-Meteo zeigt aktuelle Saisontrends – schau vor dem Start am besten in unseren Live-Wettercheck!";
    } else if (q.includes('witz') || q.includes('lachen')) {
        reply = "Warum steigen Bergsteiger so gerne auf Berge? Weil sie wissen wollen, ob die Aussicht da oben besser ist als der Weg dorthin! 🏔️";
    } else if (q.includes('essen') || q.includes('hunger') || q.includes('kaiserschmarrn') || q.includes('hütte')) {
        reply = "Auf der Oberen Firstalm gibt es legendären Kaiserschmarrn, und auf dem Rotwandhaus wartet eine zünftige Brotzeit!";
    } else if (q.includes('fahrrad') || q.includes('bike') || q.includes('gravel') || q.includes('e-bike') || q.includes('urwahn') || q.includes('lucky bike')) {
        reply = "Für Fahrräder und E-Bikes arbeiten wir eng mit Lucky Bike und der Manufaktur Urwahn zusammen. Die handgefertigten Stahl-Gravelbikes sind ein Traum!";
        productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Urwahn & Lucky Bike</strong><span>High-End Bikes</span></div><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Entdecken →</a></div>`;
    } else if (q.includes('klettern') || q.includes('klettersteig')) {
        reply = "Am Brecherspitz und an der Rotwand findest du tolle Klettersteige (B/C). Denk an ein EN 958 Klettersteigset und einen Helm!";
        productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Klettersteigsets (EN 958)</strong></div><a href="https://www.amazon.de/s?k=klettersteigset&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Prüfen →</a></div>`;
    } else {
        reply = "Das ist eine interessante Frage zu „" + t + "“. Als alpiner Experte für den Spitzingsee und das Tegernseer Tal helfe ich dir bei all deinen Fragen weiter – von Tourenplanung bis hin zu Ausrüstung von Lucky Bike, Urwahn und Amazon!";
    }

    setTimeout(() => {
        const el = document.getElementById(lid);
        if (el) el.remove();

        const botDiv = document.createElement('div');
        botDiv.className = 'ai-msg bot';
        botDiv.innerHTML = reply + '<br>' + productHtml;
        cb.appendChild(botDiv);
        cb.scrollTop = cb.scrollHeight;
    }, 350);
};

window.alpenCheckKey = function(e) { if (e.key === 'Enter') { window.alpenSendChat(); } };
