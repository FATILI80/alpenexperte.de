# Add loading="lazy" to all below-the-fold images across all HTML files
# Skips: header logo (first <img>) and hero images

$root = "C:\Users\User\Desktop\alpen-experte"
$files = Get-Content "$root\_all_html_files.txt"

$totalFixed = 0
$totalSkipped = 0

foreach ($file in $files) {
    if (-not (Test-Path $file)) { continue }
    
    $content = Get-Content $file -Raw
    $original = $content
    
    # Match all <img tags without loading="lazy"
    # But skip the first img in the file (usually the header logo - above the fold)
    $imgMatches = [regex]::Matches($content, '<img[^>]*>')
    $firstImgSkipped = $false
    
    $fixed = $false
    foreach ($m in $imgMatches) {
        $tag = $m.Value
        
        # Skip if already has loading="lazy"
        if ($tag -match 'loading="lazy"') { continue }
        
        # Skip the first img tag in the file (header logo - above the fold)
        if (-not $firstImgSkipped) {
            $firstImgSkipped = $true
            $totalSkipped++
            continue
        }
        
        # Skip hero images
        if ($tag -match 'hero-panorama') {
            $totalSkipped++
            continue
        }
        
        # Add loading="lazy" before the closing >
        $newTag = $tag -replace '>$', ' loading="lazy" />'
        $newTag = $newTag -replace '\s+/>$', ' loading="lazy" />'
        
        # Handle self-closing tags
        if ($tag -match '/>$') {
            $newTag = $tag -replace '\s*/>', ' loading="lazy" />'
        } elseif ($tag -match '>$') {
            $newTag = $tag -replace '>$', ' loading="lazy">'
        }
        
        $content = $content -replace [regex]::Escape($tag), $newTag
        $fixed = $true
        $totalFixed++
    }
    
    if ($fixed) {
        Set-Content $file $content -Encoding UTF8 -NoNewline
        Write-Host "Fixed: $($file.Substring($root.Length+1))"
    }
}

Write-Host "`nTotal images fixed: $totalFixed"
Write-Host "Total skipped (first img + hero): $totalSkipped"
