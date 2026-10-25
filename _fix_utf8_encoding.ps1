# Fix Double-Encoded UTF-8 (Mojibake) Across All HTML Files
# This script reverses the corruption at the BYTE level.
# Longer patterns MUST come before shorter ones to avoid partial matches.

$encoding = [System.Text.UTF8Encoding]::new($false)

# Byte-level fix mapping: corrupted sequence -> correct UTF-8 sequence
# Order matters: longer patterns first to prevent partial matches
$fixes = @(
    # Em-dash -- (12 corrupted bytes -> 3 correct bytes)
    @{Corrupt = [byte[]]@(0xC3,0xA2,0xE2,0x82,0xAC,0xE2,0x80,0x9C); Correct = [byte[]]@(0xE2,0x80,0x93); Desc = 'emdash'},
    
    # Euro sign EUR (9 corrupted bytes -> 3 correct bytes)
    @{Corrupt = [byte[]]@(0xC3,0xA2,0xE2,0x80,0x9A,0xC2,0xAC); Correct = [byte[]]@(0xE2,0x82,0xAC); Desc = 'euro'},
    
    # German umlauts (6 corrupted bytes -> 2 correct bytes)
    @{Corrupt = [byte[]]@(0xC3,0x83,0xC2,0xBC); Correct = [byte[]]@(0xC3,0xBC); Desc = 'ue'},
    @{Corrupt = [byte[]]@(0xC3,0x83,0xC2,0xB6); Correct = [byte[]]@(0xC3,0xB6); Desc = 'oe'},
    @{Corrupt = [byte[]]@(0xC3,0x83,0xC2,0xA4); Correct = [byte[]]@(0xC3,0xA4); Desc = 'ae'},
    
    # Sharp s (szlig)
    @{Corrupt = [byte[]]@(0xC3,0x83,0xC5,0xB8); Correct = [byte[]]@(0xC3,0x9F); Desc = 'szlig'},
    
    # Capital umlauts
    @{Corrupt = [byte[]]@(0xC3,0x83,0xE2,0x80,0x9E); Correct = [byte[]]@(0xC3,0x84); Desc = 'Ae'},
    @{Corrupt = [byte[]]@(0xC3,0x83,0xE2,0x80,0x93); Correct = [byte[]]@(0xC3,0x96); Desc = 'Oe'},
    @{Corrupt = [byte[]]@(0xC3,0x83,0xC5,0x93); Correct = [byte[]]@(0xC3,0x9C); Desc = 'Ue'}
)

# Count stats
$totalFixed = 0
$totalFiles = 0
$fixCounts = @{}
foreach ($fix in $fixes) { $fixCounts[$fix.Desc] = 0 }

# Find all HTML files (exclude archive and alpenaustausch)
$files = Get-ChildItem -Path "c:\Users\User\Desktop\alpen-experte" -Recurse -Filter "*.html" | Where-Object { 
    $_.FullName -notmatch '\\archive\\' -and $_.FullName -notmatch '\\alpenaustausch\\' 
}

$fileCount = ($files | Measure-Object).Count
Write-Host "Scanning $fileCount HTML files..."

foreach ($file in $files) {
    try {
        $bytes = [System.IO.File]::ReadAllBytes($file.FullName)
        $originalLength = $bytes.Length
        $fileFixed = 0
        $fileChanges = @{}
        
        foreach ($fix in $fixes) {
            $corrupt = $fix.Corrupt
            $correct = $fix.Correct
            $desc = $fix.Desc
            $occurrences = 0
            
            # Find all occurrences
            $i = 0
            while ($i -le $bytes.Length - $corrupt.Length) {
                $match = $true
                for ($j = 0; $j -lt $corrupt.Length; $j++) {
                    if ($bytes[$i + $j] -ne $corrupt[$j]) {
                        $match = $false
                        break
                    }
                }
                if ($match) {
                    $occurrences++
                    $before = $bytes[0..($i-1)]
                    $after = $bytes[($i+$corrupt.Length)..($bytes.Length-1)]
                    $bytes = $before + $correct + $after
                    $i += $correct.Length
                } else {
                    $i++
                }
            }
            
            if ($occurrences -gt 0) {
                $fileFixed += $occurrences
                $totalFixed += $occurrences
                $fixCounts[$desc] += $occurrences
                $fileChanges[$desc] = $occurrences
            }
        }
        
        if ($fileFixed -gt 0) {
            [System.IO.File]::WriteAllBytes($file.FullName, $bytes)
            $changes = ($fileChanges.GetEnumerator() | ForEach-Object { "$($_.Value)x $($_.Key)" }) -join ', '
            Write-Host "OK $($file.Name): $fileFixed fixes ($changes)"
            $totalFiles++
        }
    } catch {
        Write-Host "ERR $($file.Name): $_"
    }
}

Write-Host "`n=== SUMMARY ==="
Write-Host "Files fixed: $totalFiles / $fileCount scanned"
Write-Host "Total fixes applied: $totalFixed"
Write-Host "`nFix breakdown:"
foreach ($fix in $fixes) {
    $count = $fixCounts[$fix.Desc]
    if ($count -gt 0) {
        Write-Host "  $($fix.Desc): $count"
    }
}
Write-Host "Done."
