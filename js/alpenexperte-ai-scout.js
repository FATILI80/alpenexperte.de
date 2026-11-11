/**
 * ALPENEXPERTE AI & GEAR SCOUT — Widget with API Chat & Tracking
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

document.addEventListener('DOMContentLoaded', function() {
    const w = document.getElementById('alpenexperte-ai-scout');
    if (!w) return;

    w.innerHTML = `
        <div class="ai-scout-wrapper">
            <div class="ai-scout-card">
                <div class="ai-scout-header">
                    <h3 class="ai-scout-title">🏔️ Alpenexperte AI & Gear Scout</h3>
                    <div class="ai-scout-tabs">
                        <button class="ai-scout-tab active" data-tab="chat">💬 KI-Assistent</button>
                        <button class="ai-scout-tab" data-tab="wizard">🧭 Gear Finder</button>
                    </div>
                </div>
                <div class="ai-scout-body">
                    <div class="ai-scout-panel active" id="panel-chat">
                        <div class="ai-chat-box" id="aiChatBox">
                            <div class="ai-msg bot">Servus! Frag mich nach Touren, Ausrüstung oder unseren Partnern Lucky Bike & Urwahn.</div>
                        </div>
                        <div class="ai-input-group">
                            <input type="text" id="aiChatInput" class="ai-input" placeholder="z.B. E-Bike, Regen-Tipp, Spitzingsee...">
                            <button id="aiChatSend" class="ai-btn">Fragen</button>
                        </div>
                    </div>
                    <div class="ai-scout-panel" id="panel-wizard">
                        <div id="wizardContent">
                            <h4 style="color:#fff;margin-top:0;">Schritt 1: Was ist dein Vorhaben?</h4>
                            <div class="wizard-options">
                                <button class="wizard-opt-btn" data-step="1" data-val="wandern">🥾 Wandern</button>
                                <button class="wizard-opt-btn" data-step="1" data-val="bike">🚴 Gravel & E-MTB</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;

    w.querySelectorAll('.ai-scout-tab').forEach(t => {
        t.addEventListener('click', () => {
            w.querySelectorAll('.ai-scout-tab').forEach(x => x.classList.remove('active'));
            w.querySelectorAll('.ai-scout-panel').forEach(p => p.classList.remove('active'));
            t.classList.add('active');
            document.getElementById('panel-' + t.dataset.tab).classList.add('active');
            window.alpenTracking.track('scout_tab', 'switch', t.dataset.tab);
        });
    });

    const cb = document.getElementById('aiChatBox');
    const ci = document.getElementById('aiChatInput');
    const cs = document.getElementById('aiChatSend');

    function addMsg(txt, sender, html = '') {
        const d = document.createElement('div');
        d.className = `ai-msg ${sender}`;
        d.innerHTML = txt + (html ? '<br>' + html : '');
        cb.appendChild(d);
        cb.scrollTop = cb.scrollHeight;
    }

    async function sendChat() {
        const t = ci.value.trim();
        if (!t) return;
        addMsg(t, 'user');
        ci.value = '';
        window.alpenTracking.track('chat', 'query', t);

        const lid = 'l-' + Date.now();
        const ld = document.createElement('div');
        ld.className = 'ai-msg bot'; ld.id = lid; ld.innerHTML = '<em>Denke nach...</em>';
        cb.appendChild(ld); cb.scrollTop = cb.scrollHeight;

        try {
            const res = await fetch('/api/chat', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ message: t }) });
            const d = await res.json();
            document.getElementById(lid).remove();
            addMsg(d.reply, 'bot', d.productHtml);
        } catch(e) {
            document.getElementById(lid).remove();
            addMsg("Servus! Schau dir unsere Routen und das Lucky Bike Sortiment an.", 'bot', `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Lucky Bike E-Bikes</strong></div><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ansehen →</a></div>`);
        }
    }

    cs.addEventListener('click', sendChat);
    ci.addEventListener('keypress', (e) => { if (e.key === 'Enter') sendChat(); });

    document.addEventListener('click', (e) => {
        const a = e.target.closest('a');
        if (a && (a.href.includes('lucky-bike.de') || a.href.includes('awin1.com') || a.href.includes('amazon.de'))) {
            window.alpenTracking.track('affiliate_click', 'outbound', a.href);
        }
    });
});
