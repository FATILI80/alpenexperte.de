/**
 * ALPENEXPERTE.DE — Real Public AI Chat via Iframe (Hugging Face / Open-Source LLM)
 */
(function() {
    function initAlpenChat() {
        if (document.getElementById('alpenChatWidget')) return;

        const widget = document.createElement('div');
        widget.id = 'alpenChatWidget';
        widget.className = 'alpen-chat-widget';
        widget.innerHTML = `
            <button class="alpen-chat-toggle" id="alpenChatToggle" aria-label="Alpen-KI öffnen">💬</button>
            <div class="alpen-chat-box-container" id="alpenChatBoxContainer" style="width: 380px; height: 500px;">
                <div class="alpen-chat-header">
                    <h4>🏔️ Alpenexperte Live-KI (Echte KI)</h4>
                    <button class="alpen-chat-close" id="alpenChatClose">✕</button>
                </div>
                <div style="width: 100%; height: calc(100% - 53px); background: #182422; position: relative;">
                    <iframe src="https://huggingface.co/chat/" style="width: 100%; height: 100%; border: none; background: #182422;" title="Alpenexperte KI-Assistent" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>
                </div>
            </div>
        `;
        document.body.appendChild(widget);

        const toggle = document.getElementById('alpenChatToggle');
        const box = document.getElementById('alpenChatBoxContainer');
        const close = document.getElementById('alpenChatClose');

        toggle.addEventListener('click', () => { box.classList.toggle('open'); });
        close.addEventListener('click', () => { box.classList.remove('open'); });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAlpenChat);
    } else {
        initAlpenChat();
    }
})();
