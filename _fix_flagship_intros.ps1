# Fix Flagship Intros - Emotional Storytelling Rewrites
# Phase 6 — Flagship Check

$encoding = [System.Text.UTF8Encoding]::new($false) # no BOM

# --- Rotwand ---
$rotwandPath = "c:\Users\User\Desktop\alpen-experte\content\wandern\rotwand.html"
$rotwand = [System.IO.File]::ReadAllText($rotwandPath, $encoding)

$rotwandOld = @'
                    <p style="color: var(--color-text-light); margin-bottom: var(--space-md);">
                        Die Rotwand ist der bekannteste Gipfel im Mangfallgebirge und ein echter Klassiker unter den
                        Münchner Hausbergen. Der Zustieg ab Valepp ist die beliebteste Route – technisch anspruchsvoll
                        (T3), aber mit grandiosem Panorama.
                    </p>
'@

$rotwandNew = @'
                    <p style="color: var(--color-text-light); margin-bottom: var(--space-md);">
                        Wenn du auf dem Gipfel der Rotwand (1.884 m) stehst, hast du das Gefühl, die Welt liege dir zu Füßen. Der bekannteste Gipfel im Mangfallgebirge ist mehr als nur ein Münchner Hausberg – er ist der ungekrönte König der Voralpen. Der Zustieg ab Valepp ist die beliebteste Route: technisch anspruchsvoll (T3), aber mit einem Panorama belohnt, das dich für immer prägen wird.
                    </p>
'@

if ($rotwand.Contains($rotwandOld)) {
    $rotwand = $rotwand.Replace($rotwandOld, $rotwandNew)
    [System.IO.File]::WriteAllText($rotwandPath, $rotwand, $encoding)
    Write-Host "✅ Rotwand intro rewritten"
} else {
    Write-Host "⚠️ Rotwand: Pattern not found - checking raw content..."
    # Try with exact line matching
    $lines = $rotwand -split "`r`n"
    for ($i = 0; $i -lt $lines.Length; $i++) {
        if ($lines[$i] -match "Die Rotwand ist der bekannteste Gipfel") {
            Write-Host "Found at line $($i+1): $($lines[$i])"
            Write-Host "  Next: $($lines[$i+1])"
            Write-Host "  Next2: $($lines[$i+2])"
        }
    }
}

# --- Ross-Buchstein ---
$rossPath = "c:\Users\User\Desktop\alpen-experte\content\klettern\ross-buchstein.html"
$ross = [System.IO.File]::ReadAllText($rossPath, $encoding)

$rossOld = @'
                    <p style="color: var(--color-text-light); margin-bottom: var(--space-md);">Ross- und Buchstein sind die Königsdisziplin im Tegernseer Kletterrevier. Mit <strong>UIAA 6- bis 7</strong> und über 300 Höhenmetern Kletterei zählen die Südwände zu den anspruchsvollsten Touren im Mangfallgebirge. Hier ist nicht nur Technik, sondern auch Ausdauer gefragt.</p>
'@

$rossNew = @'
                    <p style="color: var(--color-text-light); margin-bottom: var(--space-md);">Stell dich unter die Südwand des Rossstein, den Kopf in den Nacken gelegt – und du spürst sofort: Hier fordert der Berg alles von dir. Ross- und Buchstein sind die Königsdisziplin im Tegernseer Kletterrevier. Mit <strong>UIAA 6- bis 7</strong> und über 300 Höhenmetern in kompaktem, griffigem Kalkstein zählen die Südwände zu den anspruchsvollsten Touren im Mangfallgebirge. Wer hier oben steht, hat nicht nur eine Route bezwungen – sondern ein Stück alpiner Geschichte geschrieben.</p>
'@

if ($ross.Contains($rossOld)) {
    $ross = $ross.Replace($rossOld, $rossNew)
    [System.IO.File]::WriteAllText($rossPath, $ross, $encoding)
    Write-Host "✅ Ross-Buchstein intro rewritten"
} else {
    Write-Host "⚠️ Ross-Buchstein: Pattern not found - checking raw content..."
    $lines = $ross -split "`r`n"
    for ($i = 0; $i -lt $lines.Length; $i++) {
        if ($lines[$i] -match "Ross- und Buchstein sind die") {
            Write-Host "Found at line $($i+1): $($lines[$i])"
        }
    }
}

Write-Host "`nDone."
