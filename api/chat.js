export default async function handler(req, res) {
    if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });
    try {
        const { message } = req.body;
        if (!message) return res.status(400).json({ error: 'Message required' });

        const systemPrompt = "Du bist der offizielle, extrem freundliche und kompetente alpine KI-Bergführer von Alpenexperte.de. Du kennst das Mangfallgebirge, den Spitzingsee, den Schliersee und den Tegernseer Tal in- und auswendig. Antworte auf Deutsch, lebendig, informativ und hilfsbereit auf JEDE Frage des Nutzers (egal ob zu Touren, Wetter, Ausrüstung oder allgemeinen Themen). Wenn nach Fahrrädern oder Ausrüstung gefragt wird, erwähne unsere Partner Lucky Bike oder Amazon (Tag: bb8ozi-21).";
        
        const fullPrompt = `${systemPrompt}\nNutzerfrage: ${message}`;
        
        const aiRes = await fetch(`https://text.pollinations.ai/${encodeURIComponent(fullPrompt)}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });

        let reply = "";
        if (aiRes.ok) {
            reply = await aiRes.text();
        } else {
            reply = "Servus! Als dein digitaler Bergführer helfe ich dir bei allen Fragen rund um das Mangfallgebirge weiter. Was möchtest du wissen?";
        }

        let productHtml = `<div class="alpen-product-card"><strong>📦 Amazon Outdoor Shop</strong><br><span>Ausrüstung für deine Tour</span><br><a href="https://www.amazon.de/s?k=alpen+ausruestung&tag=bb8ozi-21" target="_blank" rel="sponsored noopener nofollow">Jetzt ansehen →</a></div>`;
        const q = message.toLowerCase();
        if (q.includes('bike') || q.includes('rad') || q.includes('gravel') || q.includes('urwahn')) {
            productHtml = `<div class="alpen-product-card"><strong>🚴 Lucky Bike & Urwahn</strong><br><span>Gravel- & E-Bikes</span><br><a href="https://www.lucky-bike.de/?ref=bb8ozi" target="_blank" rel="sponsored noopener nofollow">Entdecken →</a></div>`;
        }

        return res.status(200).json({ reply, productHtml });
    } catch (err) {
        return res.status(500).json({ error: err.message });
    }
}
