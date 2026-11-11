/**
 * ALPENEXPERTE AI & GEAR SCOUT — Robust Hybrid AI Engine
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
                            <input type="text" id="aiChatInput" class="ai-input" placeholder="z.B. E-Bike, Regen-Tipp, Rotwand, Klettern...">
                            <button id="aiChatSend" class="ai-btn">Fragen</button>
                        </div>
                    </div>
                    <div class="ai-scout-panel" id="panel-wizard">
                        <div id="wizardContent">
                            <h4 style="color:#fff;margin-top:0;">Schritt 1: Was ist dein Vorhaben?</h4>
                            <div class="wizard-options">
                                <button class="wizard-opt-btn" data-step="1" data-val="wandern">🥾 Wandern</button>
                                <button class="wizard-opt-btn" data-step="1" data-val="bike">🚴 Gravel & E-MTB</button>
                                <button class="wizard-opt-btn" data-step="1" data-val="klettern">🧗 Klettersteig</button>
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

    function getAI(query) {
        const q = query.toLowerCase();
        let reply = "Servus! Als dein digitaler Bergführer für das Mangfallgebirge helfe ich dir bei Touren, Hütten und Ausrüstung.";
        let productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Amazon Outdoor</strong><span>Stiefel & Rucksäcke</span></div><a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Entdecken →</a></div>`;

        if (q.includes('regen') || q.includes('kinder')) {
            reply = "Bei Regen oder mit Kindern empfehlen wir die Obere Firstalm. Passende Hardshell-Jacken:";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Wasserdichte Hardshells</strong></div><a href="https://www.amazon.de/s?k=hardshell+jacke+wasserdicht&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Prüfen →</a></div>`;
        } else if (q.includes('urwahn') || q.includes('bike') || q.includes('gravel')) {
            reply = "Für Gravel und E-Bikes empfehlen wir Urwahn und Lucky Bike:";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Urwahn E-Gravel</strong></div><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ansehen →</a></div>`;
        } else if (q.includes('klettern') || q.includes('klettersteig')) {
            reply = "Für Klettersteige am Brecherspitz brauchst du ein EN 958 Klettersteigset:";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Klettersteigsets</strong></div><a href="https://www.amazon.de/s?k=klettersteigset&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Prüfen →</a></div>`;
        }
        return { reply, productHtml };
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

        setTimeout(() => {
            document.getElementById(lid).remove();
            const res = getAI(t);
            addMsg(res.reply, 'bot', res.productHtml);
        }, 300);
    }

    cs.addEventListener('click', sendChat);
    ci.addEventListener('keypress', (e) => { if (e.key === 'Enter') sendChat(); });

    let wc = w.querySelector('#wizardContent');
    if (wc) {
        wc.addEventListener('click', (e) => {
            if (!e.target.classList.contains('wizard-opt-btn')) return;
            const val = e.target.dataset.val;
            if (val === 'wandern') {
                wc.innerHTML = `<h4 style="color:#fff;margin-top:0;">Wandern:</h4><p style="color:#f0ece2;">Rotwand (1.884 m).</p><div class="ai-product-suggestion"><div class="ai-product-info"><strong>Wanderstöcke</strong></div><a href="https://www.amazon.de/s?k=wanderstoecke&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ansehen →</a></div><br><button class="ai-btn" id="wRes">Neu</button>`;
            } else if (val === 'bike') {
                wc.innerHTML = `<h4 style="color:#fff;margin-top:0;">Bike:</h4><p style="color:#f0ece2;">Urwahn & Lucky Bike.</p><div class="ai-product-suggestion"><div class="ai-product-info"><strong>Lucky Bike</strong></div><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ansehen →</a></div><br><button class="ai-btn" id="wRes">Neu</button>`;
            } else {
                wc.innerHTML = `<h4 style="color:#fff;margin-top:0;">Klettern:</h4><p style="color:#f0ece2;">Brecherspitz-Klettersteig.</p><div class="ai-product-suggestion"><div class="ai-product-info"><strong>Klettersteigsets</strong></div><a href="https://www.amazon.de/s?k=klettersteigset&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Prüfen →</a></div><br><button class="ai-btn" id="wRes">Neu</button>`;
            }
            const rb = document.getElementById('wRes');
            if (rb) rb.addEventListener('click', () => location.reload());
        });
    }

    document.addEventListener('click', (e) => {
        const a = e.target.closest('a');
        if (a && (a.href.includes('lucky-bike.de') || a.href.includes('awin1.com') || a.href.includes('amazon.de'))) {
            window.alpenTracking.track('affiliate_click', 'outbound', a.href);
        }
    });
});
