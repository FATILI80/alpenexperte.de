/**
 * ALPENEXPERTE AI & GEAR SCOUT — Interactive Frontend Widget
 */

document.addEventListener('DOMContentLoaded', function() {
    const wrapper = document.getElementById('alpenexperte-ai-scout');
    if (!wrapper) return;

    wrapper.innerHTML = `
        <div class="ai-scout-wrapper">
            <div class="ai-scout-card">
                <div class="ai-scout-header">
                    <h3 class="ai-scout-title">🏔️ Alpenexperte AI & Gear Scout</h3>
                    <div class="ai-scout-tabs">
                        <button class="ai-scout-tab active" data-tab="chat">💬 KI-Assistent</button>
                        <button class="ai-scout-tab" data-tab="wizard">🧭 Gear Finder</button>
                        <button class="ai-scout-tab" data-tab="search">🔍 Wissens-Suche</button>
                    </div>
                </div>
                <div class="ai-scout-body">
                    <!-- TAB 1: CHAT -->
                    <div class="ai-scout-panel active" id="panel-chat">
                        <div class="ai-chat-box" id="aiChatBox">
                            <div class="ai-msg bot">Servus! Ich bin dein alpiner KI-Assistent. Frag mich nach Touren, Ausrüstung, Klettersteigen oder unseren Partnern Lucky Bike & Urwahn. Wie kann ich dir heute helfen?</div>
                        </div>
                        <div class="ai-input-group">
                            <input type="text" id="aiChatInput" class="ai-input" placeholder="z.B. Welches E-Bike von Urwahn für die Valepp? Oder Tour am Spitzingsee?">
                            <button id="aiChatSend" class="ai-btn">Fragen</button>
                        </div>
                    </div>

                    <!-- TAB 2: WIZARD -->
                    <div class="ai-scout-panel" id="panel-wizard">
                        <div id="wizardContent">
                            <h4 style="color:#fff;margin-top:0;">Schritt 1 von 3: Was ist dein Vorhaben?</h4>
                            <div class="wizard-options">
                                <button class="wizard-opt-btn" data-step="1" data-val="wandern">🥾 Mehrtägige Bergtour / Wandern</button>
                                <button class="wizard-opt-btn" data-step="1" data-val="gravel">🚴 Gravel-Abenteuer & Bikepacking</button>
                                <button class="wizard-opt-btn" data-step="1" data-val="mtb">⚡ E-MTB & Trail-Tour</button>
                                <button class="wizard-opt-btn" data-step="1" data-val="klettern">🧗 Klettersteig & Alpines Gelände</button>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 3: SEARCH -->
                    <div class="ai-scout-panel" id="panel-search">
                        <div class="ai-input-group" style="margin-bottom:20px;">
                            <input type="text" id="aiSearchInput" class="ai-input" placeholder="Durchsuche alle Guides, Routen & Hardware...">
                            <button id="aiSearchBtn" class="ai-btn">Suchen</button>
                        </div>
                        <div id="aiSearchResults" style="color:#a3b1a3;font-size:0.9rem;">Tippe einen Begriff ein, um blitzschnell relevante Artikel und Partner-Angebote zu finden.</div>
                    </div>
                </div>
            </div>
        </div>
    `;

    const tabs = wrapper.querySelectorAll('.ai-scout-tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            wrapper.querySelectorAll('.ai-scout-panel').forEach(p => p.classList.remove('active'));
            wrapper.querySelector('#panel-' + tab.dataset.tab).classList.add('active');
        });
    });

    const chatBox = wrapper.querySelector('#aiChatBox');
    const chatInput = wrapper.querySelector('#aiChatInput');
    const chatSend = wrapper.querySelector('#aiChatSend');

    function appendMsg(text, sender, productHtml = '') {
        const div = document.createElement('div');
        div.className = `ai-msg ${sender}`;
        div.innerHTML = text + productHtml;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function handleChat() {
        const query = chatInput.value.trim().toLowerCase();
        if (!query) return;
        appendMsg(chatInput.value, 'user');
        chatInput.value = '';

        setTimeout(() => {
            let reply = "Das ist eine hervorragende Frage für deine Tour in den Bayerischen Voralpen!";
            let productHtml = "";

            if (query.includes('urwahn') || query.includes('gravel') || query.includes('rad') || query.includes('bike')) {
                reply = "Für Schotter und alpine Anstiege empfehlen wir dir das handgefertigte Urwahn Gravel-Bike mit integriertem Mahle-Antrieb oder die Top-Modelle von Lucky Bike.";
                productHtml = `
                    <div class="ai-product-suggestion">
                        <div class="ai-product-info">
                            <strong>Urwahn E-Gravel Bike</strong>
                            <span>Edler Stahlrahmen & Softride-Komfort</span>
                        </div>
                        <a href="https://www.awin1.com/cread.php?awinmid=68034&awinaffid=3134996&clickref=AIScout&ued=https%3A%2F%2Falpenexperte.de" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Entdecken →</a>
                    </div>
                `;
            } else if (query.includes('wandern') || query.includes('spitzingsee') || query.includes('rotwand') || query.includes('tour')) {
                reply = "Der Klassiker im Mangfallgebirge ist die Tour auf die Rotwand (1.884 m) oder der Weg zur Oberen Firstalm. Achte auf robuste Wanderschuhe mit Vibram-Sohle!";
                productHtml = `
                    <div class="ai-product-suggestion">
                        <div class="ai-product-info">
                            <strong>Amazon Outdoor Ausrüstung</strong>
                            <span>Wasserdichte Stiefel & Rucksäcke</span>
                        </div>
                        <a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ansehen →</a>
                    </div>
                `;
            } else if (query.includes('klettern') || query.includes('klettersteig') || query.includes('brecherspitz')) {
                reply = "Für Klettersteige wie am Brecherspitz benötigst du ein normgeprüftes Klettersteigset, einen Helm und feste Bergschuhe.";
                productHtml = `
                    <div class="ai-product-suggestion">
                        <div class="ai-product-info">
                            <strong>Lucky Bike Zubehör</strong>
                            <span>Sicherheits- & Outdoor-Hardware</span>
                        </div>
                        <a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Parcours prüfen →</a>
                    </div>
                `;
            } else {
                reply = "Schau dir am besten unsere detaillierten Guides an oder nutze unseren Guided Wizard, um genau die passende Hardware und Touren zu finden.";
            }

            appendMsg(reply, 'bot', productHtml);
        }, 500);
    }

    chatSend.addEventListener('click', handleChat);
    chatInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleChat(); });

    let wizardState = {};
    const wizardContent = wrapper.querySelector('#wizardContent');

    wizardContent.addEventListener('click', (e) => {
        if (!e.target.classList.contains('wizard-opt-btn')) return;
        const step = e.target.dataset.step;
        const val = e.target.dataset.val;

        if (step === "1") {
            wizardState.activity = val;
            wizardContent.innerHTML = `
                <h4 style="color:#fff;margin-top:0;">Schritt 2 von 3: Welches Terrain bevorzugst du?</h4>
                <div class="wizard-options">
                    <button class="wizard-opt-btn" data-step="2" data-val="leicht">🟢 Leichte Talsuche & Schotter</button>
                    <button class="wizard-opt-btn" data-step="2" data-val="mittel">🟡 Anspruchsvolle Almen & Trails</button>
                    <button class="wizard-opt-btn" data-step="2" data-val="schwer">🔴 Alpine Gratwege & Klettersteige</button>
                </div>
            `;
        } else if (step === "2") {
            wizardState.terrain = val;
            wizardContent.innerHTML = `
                <h4 style="color:#fff;margin-top:0;">Schritt 3 von 3: Was ist dein Hauptfokus?</h4>
                <div class="wizard-options">
                    <button class="wizard-opt-btn" data-step="3" data-val="hardware">⚡ High-End E-Bike / Hardware (Urwahn & Lucky Bike)</button>
                    <button class="wizard-opt-btn" data-step="3" data-val="touren">🗺️ Touren & Routenplanung (GPS & Hütten)</button>
                </div>
            `;
        } else if (step === "3") {
            wizardState.focus = val;
            let resultHtml = `<h4 style="color:#2ecc71;margin-top:0;">🎉 Deine maßgeschneiderte Empfehlung:</h4>`;
            if (wizardState.activity === 'gravel' || wizardState.activity === 'mtb' || wizardState.focus === 'hardware') {
                let resultName = wizardState.activity === 'gravel' ? "Urwahn E-Gravel Bike" : "Lucky Bike E-SUV Fully";
                let resultUrl = wizardState.activity === 'gravel' ? "https://www.awin1.com/cread.php?awinmid=68034&awinaffid=3134996&clickref=Wizard&ued=https%3A%2F%2Falpenexperte.de" : "https://www.lucky-bike.de/?ref=bb8ozi";
                resultHtml += `
                    <p style="color:#f0ece2;">Basierend auf deiner Auswahl (${wizardState.activity.toUpperCase()} / Terrain: ${wizardState.terrain}), empfehlen wir dir erstklassige Hardware:</p>
                    <div class="ai-product-suggestion">
                        <div class="ai-product-info">
                            <strong>${resultName}</strong>
                            <span>Perfekt abgestimmt auf die Voralpen</span>
                        </div>
                        <a href="${resultUrl}" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Zum Partner →</a>
                    </div>
                `;
            } else {
                resultHtml += `
                    <p style="color:#f0ece2;">Für dein Vorhaben (${wizardState.activity.toUpperCase()}) empfehlen wir dir unsere geprüften Touren-Guides und die passende Amazon Outdoor Ausrüstung.</p>
                    <div class="ai-product-suggestion">
                        <div class="ai-product-info">
                            <strong>Amazon Outdoor Bestseller</strong>
                            <span>Rucksäcke, Stiefel & Navigation</span>
                        </div>
                        <a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ausstattung ansehen →</a>
                    </div>
                `;
            }
            resultHtml += `<br><button class="ai-btn" id="wizardReset" style="margin-top:15px;">Neu starten</button>`;
            wizardContent.innerHTML = resultHtml;
            document.getElementById('wizardReset').addEventListener('click', () => { location.reload(); });
        }
    });

    const searchInput = wrapper.querySelector('#aiSearchInput');
    const searchBtn = wrapper.querySelector('#aiSearchBtn');
    const searchResults = wrapper.querySelector('#aiSearchResults');

    function handleSearch() {
        const q = searchInput.value.trim().toLowerCase();
        if (!q) return;
        searchResults.innerHTML = `
            <div style="background:rgba(255,255,255,0.05);padding:14px;border-radius:10px;margin-bottom:10px;">
                <strong style="color:#fff;">Ergebnisse für "${q}":</strong>
                <ul style="margin:8px 0 0;padding-left:20px;color:#f0ece2;line-height:1.6;">
                    <li><a href="/content/wandern/rotwand.html" style="color:#2ecc71;">Rotwand (1.884 m) – Der Königsgipfel</a></li>
                    <li><a href="/gravel.html" style="color:#2ecc71;">Gravel Biking im Mangfallgebirge (Urwahn & Lucky Bike)</a></li>
                    <li><a href="/content/huetten/alm-restaurants/index.html" style="color:#2ecc71;">Obere Firstalm – Kaiserschmarrn & Panorama</a></li>
                </ul>
            </div>
        `;
    }
    searchBtn.addEventListener('click', handleSearch);
    searchInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleSearch(); });
});
