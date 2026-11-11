/**
 * ALPENEXPERTE.DE — Brand New Clean AI Chat Widget
 */
(function() {
    function initAlpenChat() {
        if (document.getElementById('alpenChatWidget')) return;

        const widget = document.createElement('div');
        widget.id = 'alpenChatWidget';
        widget.className = 'alpen-chat-widget';
        widget.innerHTML = `
            <button class="alpen-chat-toggle" id="alpenChatToggle" aria-label="Alpen-KI öffnen">💬</button>
            <div class="alpen-chat-box-container" id="alpenChatBoxContainer">
                <div class="alpen-chat-header">
                    <h4>🏔️ Alpenexperte KI-Assistent</h4>
                    <button class="alpen-chat-close" id="alpenChatClose">✕</button>
                </div>
                <div class="alpen-chat-messages" id="alpenChatMessages">
                    <div class="alpen-msg bot">Servus! Ich bin dein alpiner KI-Assistent. Frag mich nach Touren, Ausrüstung, Wetter oder unseren Partnern Lucky Bike & Urwahn!</div>
                </div>
                <div class="alpen-chat-input-area">
                    <input type="text" class="alpen-chat-input" id="alpenChatInput" placeholder="Frag mich über alles...">
                    <button class="alpen-chat-send" id="alpenChatSend">Senden</button>
                </div>
            </div>
        `;
        document.body.appendChild(widget);

        const toggle = document.getElementById('alpenChatToggle');
        const box = document.getElementById('alpenChatBoxContainer');
        const close = document.getElementById('alpenChatClose');
        const send = document.getElementById('alpenChatSend');
        const input = document.getElementById('alpenChatInput');
        const msgs = document.getElementById('alpenChatMessages');

        toggle.addEventListener('click', () => { box.classList.toggle('open'); });
        close.addEventListener('click', () => { box.classList.remove('open'); });

        function addMessage(text, sender, productHtml = '') {
            const div = document.createElement('div');
            div.className = `alpen-msg ${sender}`;
            div.innerHTML = text + (productHtml ? '<br>' + productHtml : '');
            msgs.appendChild(div);
            msgs.scrollTop = msgs.scrollHeight;
        }

        function handleSend() {
            const t = input.value.trim();
            if (!t) return;
            addMessage(t, 'user');
            input.value = '';

            const lid = 'loading-' + Date.now();
            const ldiv = document.createElement('div');
            ldiv.className = 'alpen-msg bot';
            ldiv.id = lid;
            ldiv.innerHTML = '<em>Denke nach...</em>';
            msgs.appendChild(ldiv);
            msgs.scrollTop = msgs.scrollHeight;

            setTimeout(() => {
                const el = document.getElementById(lid);
                if (el) el.remove();

                const q = t.toLowerCase();
                let reply = "Das ist eine spannende Frage! Als alpiner Experte für das Mangfallgebirge und den Spitzingsee helfe ich dir bei allen Touren und Fragen weiter.";
                let productHtml = `<div class="alpen-product-card"><strong>📦 Amazon Outdoor Shop</strong><br><span>Entdecke Rucksäcke & Stiefel</span><br><a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow">Jetzt ansehen →</a></div>`;

                if (q.includes('hallo') || q.includes('servus') || q.includes('hi')) {
                    reply = "Servus! Wie kann ich dir heute bei deiner Tourenplanung in den Bayerischen Voralpen helfen?";
                } else if (q.includes('regen') || q.includes('schlechtwetter') || q.includes('kinder')) {
                    reply = "Bei Regen oder mit Kindern empfehlen wir den leichten Weg zur Oberen Firstalm oder den Gasthof Terofal.";
                    productHtml = `<div class="alpen-product-card"><strong>Wasserdichte Hardshells</strong><br><a href="https://www.amazon.de/s?k=hardshell+jacke+wasserdicht&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow">Prüfen →</a></div>`;
                } else if (q.includes('urwahn') || q.includes('bike') || q.includes('gravel') || q.includes('fahrrad')) {
                    reply = "Für Gravel und E-Bikes rund um Schliersee und Valepp empfehlen wir Urwahn und Lucky Bike!";
                    productHtml = `<div class="alpen-product-card"><strong>Urwahn E-Gravel & Lucky Bike</strong><br><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow">Ansehen →</a></div>`;
                } else if (q.includes('klettern') || q.includes('klettersteig')) {
                    reply = "Für Klettersteige am Brecherspitz brauchst du ein EN 958 Klettersteigset und einen Helm.";
                    productHtml = `<div class="alpen-product-card"><strong>Klettersteigsets (EN 958)</strong><br><a href="https://www.amazon.de/s?k=klettersteigset&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow">Prüfen →</a></div>`;
                }

                addMessage(reply, 'bot', productHtml);
            }, 350);
        }

        send.addEventListener('click', handleSend);
        input.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleSend(); });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAlpenChat);
    } else {
        initAlpenChat();
    }
})();
