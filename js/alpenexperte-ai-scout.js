/**
 * ALPENEXPERTE AI & GEAR SCOUT — Bulletproof Global Event Architecture
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

    setTimeout(() => {
        const el = document.getElementById(lid);
        if (el) el.remove();

        const q = t.toLowerCase();
        let reply = "Servus! Als dein digitaler Bergführer für das Mangfallgebirge helfe ich dir bei Touren, Hütten und Ausrüstung.";
        let productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Amazon Outdoor Bestseller</strong><span>Stiefel & Rucksäcke</span></div><a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Entdecken →</a></div>`;

        if (q.includes('regen') || q.includes('kinder')) {
            reply = "Bei Regen oder mit Kindern empfehlen wir den leichten Weg zur Oberen Firstalm. Passende Hardshell-Jacken:";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Wasserdichte Hardshells</strong></div><a href="https://www.amazon.de/s?k=hardshell+jacke+wasserdicht&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Prüfen →</a></div>`;
        } else if (q.includes('urwahn') || q.includes('bike') || q.includes('gravel') || q.includes('fahrrad')) {
            reply = "Für Gravel und E-Bikes rund um Schliersee und Valepp empfehlen wir Urwahn und Lucky Bike:";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Urwahn E-Gravel & Lucky Bike</strong></div><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ansehen →</a></div>`;
        } else if (q.includes('klettern') || q.includes('klettersteig') || q.includes('helm')) {
            reply = "Für Klettersteige am Brecherspitz brauchst du ein EN 958 Klettersteigset und einen Helm:";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>EN 958 Klettersteigsets</strong></div><a href="https://www.amazon.de/s?k=klettersteigset&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Prüfen →</a></div>`;
        }

        const botDiv = document.createElement('div');
        botDiv.className = 'ai-msg bot';
        botDiv.innerHTML = reply + '<br>' + productHtml;
        cb.appendChild(botDiv);
        cb.scrollTop = cb.scrollHeight;
    }, 350);
};

window.alpenCheckKey = function(e) { if (e.key === 'Enter') { window.alpenSendChat(); } };

document.addEventListener('DOMContentLoaded', function() {
    const w = document.getElementById('alpenexperte-ai-scout');
    if (!w) return;

    w.innerHTML = `
        <div class="ai-scout-wrapper">
            <div class="ai-scout-card">
                <div class="ai-scout-header">
                    <h3 class="ai-scout-title">🏔️ Alpenexperte AI & Gear Scout</h3>
                    <div class="ai-scout-tabs">
                        <button class="ai-scout-tab active" data-tab="chat" onclick="window.alpenSwitchTab('chat')">💬 KI-Assistent</button>
                        <button class="ai-scout-tab" data-tab="wizard" onclick="window.alpenSwitchTab('wizard')">🧭 Gear Finder</button>
                    </div>
                </div>
                <div class="ai-scout-body">
                    <div class="ai-scout-panel active" id="panel-chat">
                        <div class="ai-chat-box" id="aiChatBox">
                            <div class="ai-msg bot">Servus! Frag mich nach Touren, Ausrüstung oder unseren Partnern Lucky Bike & Urwahn.</div>
                        </div>
                        <div class="ai-input-group">
                            <input type="text" id="aiChatInput" class="ai-input" placeholder="z.B. E-Bike, Regen-Tipp, Rotwand, Klettern..." onkeypress="window.alpenCheckKey(event)">
                            <button id="aiChatSend" class="ai-btn" onclick="window.alpenSendChat()">Fragen</button>
                        </div>
                    </div>
                    <div class="ai-scout-panel" id="panel-wizard">
                        <div id="wizardContent">
                            <h4 style="color:#fff;margin-top:0;">Wähle dein alpines Vorhaben:</h4>
                            <div class="wizard-options">
                                <button class="wizard-opt-btn" onclick="this.parentElement.innerHTML='<h4 style=\'color:#fff;\'>Wandern-Tipp:</h4><p style=\'color:#f0ece2;\'>Rotwand (1.884 m) & Obere Firstalm.</p><a href=\'https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21\' target=\'_blank\' rel=\'sponsored noopener nofollow\' class=\'ai-product-link\'>Ausrüstung ansehen →</a>'">🥾 Wandern</button>
                                <button class="wizard-opt-btn" onclick="this.parentElement.innerHTML='<h4 style=\'color:#fff;\'>Bike-Tipp:</h4><p style=\'color:#f0ece2;\'>Urwahn E-Gravel & Lucky Bike Fullys.</p><a href=\'https://www.lucky-bike.de/?ref=bb8ozi\' target=\'_blank\' rel=\'sponsored noopener nofollow\' class=\'ai-product-link\'>Lucky Bike ansehen →</a>'">🚴 Gravel & E-MTB</button>
                                <button class="wizard-opt-btn" onclick="this.parentElement.innerHTML='<h4 style=\'color:#fff;\'>Klettern-Tipp:</h4><p style=\'color:#f0ece2;\'>Brecherspitz-Klettersteig (B/C).</p><a href=\'https://www.amazon.de/s?k=klettersteigset&tag=bb8ozi-21\' target=\'_blank\' rel=\'sponsored noopener nofollow\' class=\'ai-product-link\'>Klettersteigsets prüfen →</a>'">🧗 Klettersteig</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    console.log("Bulletproof AI Scout successfully initialized.");
});
