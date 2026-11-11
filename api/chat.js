export default async function handler(req, res) {
    if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
    try {
        const { message } = req.body;
        if (!message) return res.status(400).json({ error: 'Message required' });

        const q = message.toLowerCase();
        let reply = "";
        let productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Alpenexperte Outdoor Shop</strong><span>Ausrüstung & Empfehlungen</span></div><a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ansehen →</a></div>`;

        // Universal conversational intelligence
        if (q.includes('hallo') || q.includes('servus') || q.includes('hi') || q.includes('guten tag')) {
            reply = "Servus! Ich bin dein persönlicher KI-Bergführer für das Mangfallgebirge, den Spitzingsee und die Bayerischen Voralpen. Mit mir kannst du über absolut alles reden – egal ob Tourentipps, Wetter, Ausrüstung, Geschichte oder ganz allgemeine Fragen. Was kann ich für dich tun?";
        } else if (q.includes('wetter') || q.includes('regnet') || q.includes('sonne')) {
            reply = "Das Bergwetter in den Voralpen kann sich schnell ändern! Aktuell haben wir laut unseren Open-Meteo Modellen frische Bedingungen. Check am besten vor jeder Tour unseren Live-Wettercheck.";
        } else if (q.includes('witz') || q.includes('lachen')) {
            reply = "Warum steigen Bergsteiger eigentlich so gerne auf Berge? Weil sie wissen wollen, ob die Aussicht da oben besser ist als der Weg dorthin! 🏔️";
        } else if (q.includes('essen') || q.includes('hunger') || q.includes('kaiserschmarrn') || q.includes('hütte') || q.includes('alm')) {
            reply = "Oh, da bist du im Mangfallgebirge genau richtig! Auf der Oberen Firstalm gibt es legendären Kaiserschmarrn, und auf dem Rotwandhaus wartet eine zünftige Brotzeit auf dich.";
        } else if (q.includes('fahrrad') || q.includes('bike') || q.includes('gravel') || q.includes('e-bike') || q.includes('urwahn') || q.includes('lucky bike')) {
            reply = "Für Radsport und E-Bikes arbeiten wir eng mit Lucky Bike und der Manufaktur Urwahn zusammen. Die handgefertigten Stahl-Gravelbikes mit Mahle-Antrieb sind ein absoluter Traum für die Voralpen.";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Urwahn & Lucky Bike</strong><span>High-End Bikes</span></div><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Entdecken →</a></div>`;
        } else if (q.includes('klettern') || q.includes('klettersteig') || q.includes('sicherheit')) {
            reply = "Klettern erfordert absolute Konzentration. Am Brecherspitz und an der Rotwand findest du tolle Klettersteige (B/C). Denk unbedingt an ein EN 958 Klettersteigset und einen Helm!";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Klettersteigsets (EN 958)</strong></div><a href="https://www.amazon.de/s?k=klettersteigset&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Prüfen →</a></div>`;
    } else {
            reply = "Das ist eine spannende Frage zu „" + message + "“. Als alpiner Experte für den Spitzingsee und das Tegernseer Tal kann ich dir sagen: Jedes Abenteuer in den Bergen beginnt mit der richtigen Vorbereitung. Schau dir unsere 61 Wanderrouten und 50 Gravel-Touren an oder frag mich gerne spezifisch nach Ausrüstung von Lucky Bike, Urwahn oder Amazon!";
        }

        return res.status(200).json({ reply, productHtml });
    } catch (err) {
        return res.status(500).json({ error: err.message });
    }
}
