param(
    [string]$RootDir = "C:\Users\User\Desktop\alpen-experte",
    [string]$BaseUrl = "https://www.alpenexperte.de"
)

$files = Get-Content "$RootDir\_all_html_files.txt"

# Remove archive/ and alpenaustausch/ from sitemap
$files = $files | Where-Object { $_ -notmatch '\\archive\\' -and $_ -notmatch '\\alpenaustausch\\' }

$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine('<?xml version="1.0" encoding="UTF-8"?>')
[void]$sb.AppendLine('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
[void]$sb.AppendLine('        xmlns:xhtml="http://www.w3.org/1999/xhtml">')
[void]$sb.AppendLine()

function Get-PriorityAndFreq($path) {
    $p = $path.Replace($RootDir, '').Replace('\', '/')
    
    if ($p -eq '/index.html') { return @('1.0', 'weekly') }
    if ($p -match '/impressum\.html|/datenschutz\.html|/haftungsausschluss\.html') { return @('0.3', 'yearly') }
    
    if ($p -match '^/region/[^/]+/index\.html$' -or $p -match '^/region/index\.html$') { return @('0.9', 'weekly') }
    
    if ($p -match '^/content/[^/]+/index\.html$') { return @('0.8', 'weekly') }
    
    if ($p -match '^/content/[^/]+/[^/]+/index\.html$') {
        if ($p -match '/huetten/|/winter/|/wandern/') { return @('0.8', 'monthly') }
        return @('0.7', 'monthly')
    }
    
    if ($p -match '/wandern/[^/]+\.html$') {
        if ($p -match 'rotwand\.html$|taubenstein\.html$') { return @('0.9', 'weekly') }
        if ($p -match 'hw-') { return @('0.8', 'monthly') }
        return @('0.7', 'monthly')
    }
    if ($p -match '/mtb/[^/]+\.html$') {
        if ($p -match 'drei-seen-runde|spitzingsee-runde') { return @('0.8', 'weekly') }
        return @('0.7', 'monthly')
    }
    if ($p -match '/klettern/[^/]+\.html$') {
        if ($p -match 'ross-buchstein|brecherspitz') { return @('0.8', 'weekly') }
        return @('0.7', 'monthly')
    }
    if ($p -match '/winter/[^/]+\.html$' -and $p -notmatch '/schneeschuh/|/skitouren/|/skigebiet/|/langlauf/') {
        return @('0.7', 'monthly')
    }
    if ($p -match '/winter/(schneeschuh|skitouren|skigebiet|langlauf)/[^/]+\.html$') { return @('0.6', 'monthly') }
    
    if ($p -match '/nordic-walking/[^/]+\.html$') { return @('0.6', 'monthly') }
    if ($p -match '/praxis/') { return @('0.7', 'monthly') }
    if ($p -match '/regional/') { return @('0.7', 'monthly') }
    if ($p -match '/fauna/|/almkultur/|/sicherheit/|/ausruestung/|/fitness/|/fehlkauf-vermeidung/|/layering/|/tech/|/sternenhimmel/|/karte/') { return @('0.6', 'monthly') }
    
    return @('0.5', 'monthly')
}

$categories = @{}
$processed = @{}
$files | ForEach-Object {
    $rel = $_.Replace($RootDir, '').Replace('\', '/')
    
    if ($rel -match '^/region/') { $cat = 'REGION-HUBS' }
    elseif ($rel -match '^/content/ausruestung/') { $cat = 'AUSRUESTUNG' }
    elseif ($rel -match '^/content/praxis/') { $cat = 'PRAXIS' }
    elseif ($rel -match '^/content/regional/') { $cat = 'REGIONAL_CONTENT' }
    elseif ($rel -match '^/content/sicherheit/') { $cat = 'SICHERHEIT' }
    elseif ($rel -match '^/content/fitness/') { $cat = 'FITNESS' }
    elseif ($rel -match '^/content/fauna/') { $cat = 'FAUNA_FLORA' }
    elseif ($rel -match '^/content/mtb/') { $cat = 'MTB' }
    elseif ($rel -match '^/content/winter/') { $cat = 'WINTER' }
    elseif ($rel -match '^/content/tech/') { $cat = 'TECH' }
    elseif ($rel -match '^/content/layering/') { $cat = 'LAYERING' }
    elseif ($rel -match '^/content/fehlkauf-vermeidung/') { $cat = 'FEHLKAUF_VERMEIDUNG' }
    elseif ($rel -match '^/content/huetten/') { $cat = 'HUETTEN' }
    elseif ($rel -match '^/content/karte/') { $cat = 'KARTE' }
    elseif ($rel -match '^/content/klettern/') { $cat = 'KLETTERN' }
    elseif ($rel -match '^/content/almkultur/') { $cat = 'ALMKULTUR' }
    elseif ($rel -match '^/content/nordic-walking/') { $cat = 'NORDIC_WALKING' }
    elseif ($rel -match '^/content/wandern/') { $cat = 'WANDERN' }
    elseif ($rel -match '^/content/sternenhimmel/') { $cat = 'STERNENHIMMEL' }
    elseif ($rel -match '^/content/') { $cat = 'SONSTIGE_CONTENT' }
    else { $cat = 'SONSTIGE' }
    
    if (-not $categories.ContainsKey($cat)) { $categories[$cat] = @() }
    $categories[$cat] += $rel
}

$catDisplay = @{
    'REGION-HUBS' = 'REGION-HUBS'
    'AUSRUESTUNG' = 'AUSRUESTUNG'
    'PRAXIS' = 'PRAXIS'
    'REGIONAL_CONTENT' = 'REGIONAL (CONTENT)'
    'SICHERHEIT' = 'SICHERHEIT'
    'FITNESS' = 'FITNESS'
    'FAUNA_FLORA' = 'FAUNA & FLORA'
    'ALMKULTUR' = 'ALMKULTUR'
    'KARTE' = 'KARTE'
    'STERNENHIMMEL' = 'STERNENHIMMEL'
    'WANDERN' = 'WANDERN'
    'MTB' = 'MTB'
    'KLETTERN' = 'KLETTERN'
    'NORDIC_WALKING' = 'NORDIC WALKING'
    'HUETTEN' = 'HUETTEN (HUB)'
    'WINTER' = 'WINTER'
    'LAYERING' = 'LAYERING'
    'FEHLKAUF_VERMEIDUNG' = 'FEHLKAUF-VERMEIDUNG'
    'TECH' = 'TECH'
    'SONSTIGE_CONTENT' = 'SONSTIGE CONTENT'
    'SONSTIGE' = 'SONSTIGE'
}

$catOrder = @(
    'REGION-HUBS', 'AUSRUESTUNG', 'PRAXIS', 'REGIONAL_CONTENT',
    'SICHERHEIT', 'FITNESS', 'FAUNA_FLORA', 'ALMKULTUR',
    'KARTE', 'STERNENHIMMEL', 'WANDERN', 'MTB', 'KLETTERN',
    'NORDIC_WALKING', 'HUETTEN', 'WINTER', 'LAYERING',
    'FEHLKAUF_VERMEIDUNG', 'TECH', 'SONSTIGE_CONTENT', 'SONSTIGE'
)

$total = 0
foreach ($cat in $catOrder) {
    if ($categories.ContainsKey($cat) -and $categories[$cat].Count -gt 0) {
        $disp = if ($catDisplay.ContainsKey($cat)) { $catDisplay[$cat] } else { $cat }
        [void]$sb.AppendLine("    <!-- ===== $disp ===== -->")
        [void]$sb.AppendLine()
        
        $sorted = $categories[$cat] | Sort-Object
        foreach ($relPath in $sorted) {
            $fullPath = $RootDir + $relPath.Replace('/', '\')
            $loc = "$BaseUrl$relPath"
            $paf = Get-PriorityAndFreq $fullPath
            $priority = $paf[0]
            $changefreq = $paf[1]
            
            [void]$sb.AppendLine("    <url>")
            [void]$sb.AppendLine("        <loc>$loc</loc>")
            [void]$sb.AppendLine("        <lastmod>2026-06-01</lastmod>")
            [void]$sb.AppendLine("        <changefreq>$changefreq</changefreq>")
            [void]$sb.AppendLine("        <priority>$priority</priority>")
            [void]$sb.AppendLine("    </url>")
        }
        [void]$sb.AppendLine()
        $total += $categories[$cat].Count
    }
}

[void]$sb.AppendLine("</urlset>")
$sb.ToString() | Out-File -FilePath "$RootDir\sitemap.xml" -Encoding UTF8
Write-Host "Sitemap generated with $total entries"
