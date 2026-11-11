export default async function handler(req, res) {
    if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
    try {
        const { message } = req.body;
        if (!message) return res.status(400).json({ error: 'Message required' });
        
        const q = message.toLowerCase();
        let reply = "Servus! Als dein digitaler Bergführer für das Mangfallgebirge (Spitzingsee, Tegernsee, Rotwand) helfe ich dir bei Touren, Hütten und Ausrüstung.";
        let productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Amazon Outdoor Bestseller</strong><span>Stiefel, Rucksäcke & Stöcke</span></div><a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Entdecken →</a></div>`;

        if (q.includes('regen') || q.includes('kinder')) {
            reply = "Bei Regen oder mit Kindern empfehlen wir den leichten Weg zur Oberen Firstalm oder den Gasthof Terofal. Dazu passende Hardshell-Jacken:";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Wasserdichte Hardshells</strong><span>Atmungsaktiv & sturmerprobt</span></div><a href="https://www.amazon.de/s?k=hardshell+jacke+wasserdicht&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Prüfen →</a></div>`;
        } else if (q.includes('urwahn') || q.includes('bike') || q.includes('gravel')) {
            reply = "Für Gravel und E-Bikes rund um Schliersee und Valepp empfehlen wir Urwahn und Lucky Bike:";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Urwahn Platzhirsch E-Gravel</strong><span>Edler Stahlrahmen</span></div><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Ansehen →</a></div>`;
        } else if (q.includes('klettern') || q.includes('helm')) {
            reply = "Für Klettersteige am Brecherspitz brauchst du ein EN 958 Klettersteigset und einen Helm:";
            productHtml = `<div class="ai-product-suggestion"><div class="ai-product-info"><strong>Amazon Kletterausrüstung</strong><span>EN 958 Sets & Helme</span></div><a href="https://www.amazon.de/s?k=klettersteigset+kletterausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow" class="ai-product-link">Prüfen →</a></div>`;
        }
        return res.status(200).json({ reply, productHtml });
    } catch (err) {
        return res.status(500).json({ error: err.message });
    }
}
