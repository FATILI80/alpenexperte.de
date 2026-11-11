/**
 * ALPENEXPERTE.DE — Real Generative AI AlpenChat Widget
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
                    <h4>🏔️ Alpenexperte KI-Assistent (Echte KI)</h4>
                    <button class="alpen-chat-close" id="alpenChatClose">✕</button>
                </div>
                <div class="alpen-chat-messages" id="alpenChatMessages">
                    <div class="alpen-msg bot">Servus! Ich bin deine echte generative KI für das Mangfallgebirge. Frag mich über absolut alles (Touren, Wetter, Ausrüstung, Weltgeschehen...)!</div>
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

        async function handleSend() {
            const t = input.value.trim();
            if (!t) return;
            addMessage(t, 'user');
            input.value = '';

            const lid = 'loading-' + Date.now();
            const ldiv = document.createElement('div');
            ldiv.className = 'alpen-msg bot';
            ldiv.id = lid;
            ldiv.innerHTML = '<em>Generiere echte KI-Antwort...</em>';
            msgs.appendChild(ldiv);
            msgs.scrollTop = msgs.scrollHeight;

            try {
                // Try serverless function first, fallback directly to public free LLM API if serverless fails
                let reply = "";
                let productHtml = `<div class="alpen-product-card"><strong>📦 Amazon Outdoor Shop</strong><br><a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow">Ausrüstung ansehen →</a></div>`;

                try {
                    const res = await fetch('/api/chat', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ message: t })
                    });
                    if (res.ok) {
                        const data = await res.json();
                        reply = data.reply;
                        if (data.productHtml) productHtml = data.productHtml;
                    }
                } catch(err) {}

                if (!reply) {
                    const prompt = `Du bist ein alpiner Bergführer für Alpenexperte.de. Antworte auf Deutsch auf: ${t}`;
                    const directRes = await fetch(`https://text.pollinations.ai/${encodeURIComponent(prompt)}`);
                    if (directRes.ok) {
                        reply = await directRes.text();
                    } else {
                        reply = "Servus! Als dein digitaler Bergführer helfe ich dir bei allen Touren und Fragen rund um den Spitzingsee weiter.";
                    }
                }

                const el = document.getElementById(lid);
                if (el) el.remove();
                addMessage(reply, 'bot', productHtml);

            } catch (e) {
                const el = document.getElementById(lid);
                if (el) el.remove();
                addMessage("Servus! Ich stehe dir jederzeit für Touren, Hütten und Ausrüstung zur Seite. Was möchtest du wissen?", 'bot', `<div class="alpen-product-card"><strong>Lucky Bike & Amazon</strong><br><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow">Entdecken →</a></div>`);
            }
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
