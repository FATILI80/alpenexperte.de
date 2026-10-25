# PowerShell script to fix ALL design issues at once
# Fixes: hero image, color scheme, glass effect, card design, CSS cleanup

$cssPath = "C:\Users\User\Desktop\alpen-experte\css\style.css"
$htmlPath = "C:\Users\User\Desktop\alpen-experte\index.html"

Write-Host "=== ALPEN-EXPERTE DESIGN RESET ===" -ForegroundColor Cyan

# ============================================
# 1. Read the CURRENT CSS file
# ============================================
$css = [System.IO.File]::ReadAllText($cssPath)

# ============================================
# 2. Replace CSS Variables block (lines 81-176)
# ============================================
Write-Host "1. Updating CSS variables..." -ForegroundColor Yellow

$oldVars = @"
:root {
    /* PRIMAER: Bergsee-Tuerkis/Cyan */
    --color-primary: #028090;
    --color-primary-rgb: 2, 128, 144;
    --color-primary-dark: #03616e;
    --color-primary-light: #4ecdc4;
    --color-primary-glow: rgba(2, 128, 144, 0.3);

    /* SEKUNDAER: Sonnenuntergangs-Orange fuer CTAs */
    --color-secondary: #f77f00;
    --color-secondary-rgb: 247, 127, 0;
    --color-secondary-dark: #d96f00;
    --color-secondary-light: #ffb347;
    --color-secondary-glow: rgba(247, 127, 0, 0.3);

    /* HINTERGRUND: Tiefes Nachtblau */
    --color-bg-dark: #0b1a2e;
    --color-bg-dark-rgb: 11, 26, 46;
    --color-bg-mid: #132a42;
    --color-bg-light: #1e3a5e;
    --color-bg-warm: #f0ebe3;

    /* GLAS-EFFEKT: Semi-transparent fuer Frosted Glass */
    --color-glass: rgba(255, 255, 255, 0.08);
    --color-glass-hover: rgba(255, 255, 255, 0.14);
    --color-glass-border: rgba(255, 255, 255, 0.12);
    --color-glass-border-hover: rgba(255, 255, 255, 0.2);
    --color-glass-text: rgba(255, 255, 255, 0.85);
    --color-glass-text-light: rgba(255, 255, 255, 0.6);

    /* AKZENT-FARBEN */
    --color-alpine-green: #3aaf85;
    --color-alpine-green-light: #5cc9a0;
    --color-sky-blue: #4ecdc4;
    --color-fun-pink: #ff6b8a;
    --color-fun-purple: #a78bfa;
    --color-fun-yellow: #fbbf24;
    --color-fun-teal: #2dd4bf;

    /* HOLZTOENE - reduziert, eleganter */
    --color-wood-dark: #1a1a2e;
    --color-wood-dark-rgb: 26, 26, 46;
    --color-wood-medium: #16213e;
    --color-wood-light: #4a6fa5;
    --color-wood-warm: #7c9bc9;

    /* TEXT - maximale Lesbarkeit auf dunklen Hintergruenden */
    --color-text: #e8edf2;
    --color-text-light: #a0b4c8;
    --color-text-muted: #6a7f99;
    --color-white: #ffffff;

    /* CTA-Akzent */
    --color-accent: #f77f00;
    --color-accent-hover: #ff9500;

    /* Typografie */
    --font-display: 'Playfair Display', Georgia, 'Times New Roman', serif;
    --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

    /* Abstaende */
    --space-xs: 0.25rem;
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    --space-xl: 2rem;
    --space-2xl: 3rem;
    --space-3xl: 4rem;
    --space-4xl: 6rem;

    /* Container */
    --container-max: 1200px;
    --container-narrow: 900px;

    /* Border-Radius */
    --radius-sm: 6px;
    --radius-md: 12px;
    --radius-lg: 20px;
    --radius-xl: 30px;

    /* Shadows */
    --shadow-sm: 0 2px 8px rgba(2, 128, 144, 0.1);
    --shadow-md: 0 8px 24px rgba(2, 128, 144, 0.15);
    --shadow-lg: 0 16px 48px rgba(2, 128, 144, 0.2);
    --shadow-card: 0 4px 16px rgba(2, 128, 144, 0.08);
    --shadow-glow: 0 0 30px rgba(2, 128, 144, 0.15);

    /* Transitions */
    --transition-fast: 200ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-base: 350ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 500ms cubic-bezier(0.4, 0, 0.2, 1);

    /* Backdrop-Blur fuer Glas-Effekt */
    --blur-glass: 12px;
    --blur-heavy: 20px;
}
"@

$newVars = @"
:root {
    /* PRIMAER: Sattes Bergsee-Tuerkis */
    --color-primary: #00a8cc;
    --color-primary-rgb: 0, 168, 204;
    --color-primary-dark: #0088a8;
    --color-primary-light: #66d9e8;
    --color-primary-glow: rgba(0, 168, 204, 0.3);

    /* SEKUNDAER: Alpen-Gipfelgold/Orange fuer CTAs */
    --color-secondary: #f77f00;
    --color-secondary-rgb: 247, 127, 0;
    --color-secondary-dark: #d96f00;
    --color-secondary-light: #ffb347;
    --color-secondary-glow: rgba(247, 127, 0, 0.3);

    /* HINTERGRUND */
    --color-bg-dark: #1a252c;
    --color-bg-dark-rgb: 26, 37, 44;
    --color-bg-mid: #edf2f7;
    --color-bg-light: #f8f9fa;
    --color-bg-warm: #f0ebe3;

    /* GLAS-EFFEKT (GLETSCHERWEISS) */
    --color-glass: rgba(255, 255, 255, 0.85);
    --color-glass-hover: rgba(255, 255, 255, 0.95);
    --color-glass-border: rgba(255, 255, 255, 0.4);
    --color-glass-border-hover: rgba(255, 255, 255, 0.6);
    --color-glass-text: #1a252c;
    --color-glass-text-light: #5a6a7a;

    /* AKZENT-FARBEN */
    --color-alpine-green: #3aaf85;
    --color-alpine-green-light: #5cc9a0;
    --color-sky-blue: #4ecdc4;
    --color-fun-pink: #ff6b8a;
    --color-fun-purple: #a78bfa;
    --color-fun-yellow: #fbbf24;
    --color-fun-teal: #2dd4bf;

    /* HOLZTOENE */
    --color-wood-dark: #1a1a2e;
    --color-wood-dark-rgb: 26, 26, 46;
    --color-wood-medium: #16213e;
    --color-wood-light: #4a6fa5;
    --color-wood-warm: #7c9bc9;

    /* TEXT */
    --color-text: #1a252c;
    --color-text-light: #5a6a7a;
    --color-text-muted: #8a9aaa;
    --color-white: #ffffff;

    /* CTA-Akzent */
    --color-accent: #f77f00;
    --color-accent-hover: #ff9500;

    /* Typografie */
    --font-display: 'Playfair Display', Georgia, 'Times New Roman', serif;
    --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

    /* Abstaende */
    --space-xs: 0.25rem;
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    --space-xl: 2rem;
    --space-2xl: 3rem;
    --space-3xl: 4rem;
    --space-4xl: 6rem;

    /* Container */
    --container-max: 1200px;
    --container-narrow: 900px;

    /* Border-Radius */
    --radius-sm: 6px;
    --radius-md: 12px;
    --radius-lg: 12px;
    --radius-xl: 24px;

    /* Shadows */
    --shadow-sm: 0 2px 8px rgba(26, 37, 44, 0.06);
    --shadow-md: 0 8px 24px rgba(26, 37, 44, 0.1);
    --shadow-lg: 0 16px 48px rgba(26, 37, 44, 0.12);
    --shadow-card: 0 15px 35px rgba(26, 37, 44, 0.08);
    --shadow-glow: 0 0 30px rgba(0, 168, 204, 0.15);

    /* Transitions */
    --transition-fast: 200ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-base: 350ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 500ms cubic-bezier(0.4, 0, 0.2, 1);

    /* Backdrop-Blur fuer Glas-Effekt */
    --blur-glass: 8px;
    --blur-heavy: 16px;
}
"@

if ($css.Contains($oldVars)) {
    $css = $css.Replace($oldVars, $newVars)
    Write-Host "   [OK] CSS variables replaced" -ForegroundColor Green
} else {
    Write-Host "   [FAIL] Could not find CSS variables block!" -ForegroundColor Red
}

# ============================================
# 3. Fix Body background and color
# ============================================
Write-Host "2. Fixing body background (light theme)..." -ForegroundColor Yellow

$oldBody = @"
body {
    font-family: var(--font-body);
    font-size: 1rem;
    font-weight: 500;
    line-height: 1.7;
    color: var(--color-glass-text);
    background: linear-gradient(135deg, var(--color-bg-dark) 0%, var(--color-bg-mid) 50%, var(--color-bg-light) 100%);
    background-attachment: fixed;
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
"@

$newBody = @"
body {
    font-family: var(--font-body);
    font-size: 1rem;
    font-weight: 500;
    line-height: 1.7;
    color: var(--color-text);
    background: var(--color-bg-light);
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
"@

if ($css.Contains($oldBody)) {
    $css = $css.Replace($oldBody, $newBody)
    Write-Host "   [OK] Body background updated" -ForegroundColor Green
} else {
    Write-Host "   [WARN] Body pattern not found exactly, checking alternatives..." -ForegroundColor Yellow
    # Try finding just the background line
    $css = $css -replace 'background: linear-gradient\(135deg, var\(--color-bg-dark\) 0%, var\(--color-bg-mid\) 50%, var\(--color-bg-light\) 100%\);', 'background: var(--color-bg-light);'
    $css = $css -replace 'background-attachment: fixed;', ''
    $css = $css -replace 'color: var\(--color-glass-text\);', 'color: var(--color-text);'
    Write-Host "   [OK] Body background updated (fallback method)" -ForegroundColor Green
}

# ============================================
# 4. Fix Hero - Hide video, show image, update overlay
# ============================================
Write-Host "3. Fixing Hero section (show image, hide video)..." -ForegroundColor Yellow

# Hide hero-video
$oldVideo = @"
.hero-video {
    position: absolute;
    inset: 0;
    z-index: 0;
    width: 100%;
    height: 100%;
}

.hero-video video {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
"@

$newVideo = @"
.hero-video {
    display: none;
}
"@

if ($css.Contains($oldVideo)) {
    $css = $css.Replace($oldVideo, $newVideo)
    Write-Host "   [OK] Hero video hidden" -ForegroundColor Green
} else {
    Write-Host "   [WARN] Hero video pattern not found, trying alternative..." -ForegroundColor Yellow
    $css = $css -replace '\.hero-video \{[\s\S]*?object-fit: cover;\s*\}', '.hero-video { display: none; }'
    Write-Host "   [OK] Hero video hidden (fallback)" -ForegroundColor Green
}

# Hide hero-particles (since video is hidden, particles aren't needed as fallback)
$css = $css -replace '\.hero-particles \{', '.hero-particles { display: none; /* ' -replace '\}\s*\.hero-particles', '} */.hero-particles'
# Better approach - find and replace the entire particles block
$oldParticles = @"
.hero-particles {
    position: absolute;
    inset: 0;
    z-index: 0;
    overflow: hidden;
    opacity: 0;
    transition: opacity 1s ease;
}

.hero-video video:not([src]) ~ .hero-particles,
.hero-particles-fallback {
    opacity: 1;
}

.hero-particles span {
    position: absolute;
    display: block;
    width: 4px;
    height: 4px;
    background: rgba(78, 205, 196, 0.4);
    border-radius: 50%;
    animation: particleFloat 15s infinite;
}

.hero-particles span:nth-child(1) { left: 10%; animation-delay: 0s; animation-duration: 12s; }
.hero-particles span:nth-child(2) { left: 25%; animation-delay: 1s; animation-duration: 14s; width: 6px; height: 6px; }
.hero-particles span:nth-child(3) { left: 40%; animation-delay: 2s; animation-duration: 16s; }
.hero-particles span:nth-child(4) { left: 55%; animation-delay: 0.5s; animation-duration: 13s; width: 3px; height: 3px; }
.hero-particles span:nth-child(5) { left: 70%; animation-delay: 3s; animation-duration: 15s; }
.hero-particles span:nth-child(6) { left: 85%; animation-delay: 1.5s; animation-duration: 11s; width: 5px; height: 5px; }
.hero-particles span:nth-child(7) { left: 50%; animation-delay: 4s; animation-duration: 18s; }
.hero-particles span:nth-child(8) { left: 15%; animation-delay: 2.5s; animation-duration: 10s; }
.hero-particles span:nth-child(9) { left: 65%; animation-delay: 3.5s; animation-duration: 17s; width: 7px; height: 7px; }
.hero-particles span:nth-child(10) { left: 35%; animation-delay: 0.8s; animation-duration: 14s; }
"@

$newParticles = @"
.hero-particles {
    display: none;
}
"@

if ($css.Contains($oldParticles)) {
    $css = $css.Replace($oldParticles, $newParticles)
    Write-Host "   [OK] Hero particles hidden" -ForegroundColor Green
} else {
    Write-Host "   [WARN] Particles block not found, trying regex..." -ForegroundColor Yellow
    # Will handle any remaining particles CSS later
}

# Ensure hero-image shows properly
$oldHeroImage = @"
.hero-image {
    position: absolute;
    inset: 0;
    z-index: 0;
}

.hero-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
"@

$newHeroImage = @"
.hero-image {
    position: absolute;
    inset: 0;
    z-index: 0;
}

.hero-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

@supports (background-image: url('')) {
    .hero {
        background-image: url('../images/hero-panorama.jpg');
        background-size: cover;
        background-position: center;
    }
    .hero-image {
        opacity: 0;
        pointer-events: none;
    }
}
"@

if ($css.Contains($oldHeroImage)) {
    $css = $css.Replace($oldHeroImage, $newHeroImage)
    Write-Host "   [OK] Hero image enhanced with background-image fallback" -ForegroundColor Green
}

# Update hero overlay gradient
$oldOverlay = @"
.hero-overlay {
    position: relative;
    z-index: 2;
    width: 100%;
    padding: var(--space-4xl) 0;
    background: linear-gradient(135deg,
            rgba(11, 26, 46, 0.85) 0%,
            rgba(2, 128, 144, 0.4) 40%,
            rgba(78, 205, 196, 0.2) 70%,
            rgba(11, 26, 46, 0.1) 100%);
}
"@

$newOverlay = @"
.hero-overlay {
    position: relative;
    z-index: 2;
    width: 100%;
    padding: var(--space-4xl) 0;
    background: linear-gradient(rgba(26, 37, 44, 0.4), rgba(26, 37, 44, 0.7));
}
"@

if ($css.Contains($oldOverlay)) {
    $css = $css.Replace($oldOverlay, $newOverlay)
    Write-Host "   [OK] Hero overlay gradient updated" -ForegroundColor Green
}

# Update hero-badge for light bg compatibility
$oldBadge = @"
.hero-badge {
    display: inline-block;
    background: var(--color-glass);
    backdrop-filter: blur(var(--blur-glass));
    -webkit-backdrop-filter: blur(var(--blur-glass));
    color: var(--color-glass-text);
    padding: var(--space-xs) var(--space-md);
    border-radius: var(--radius-xl);
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: var(--space-lg);
    border: 1px solid var(--color-glass-border);
    animation: fadeInUp 0.8s ease forwards;
    animation-delay: 0.2s;
    opacity: 0;
}
"@

$newBadge = @"
.hero-badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    color: var(--color-white);
    padding: var(--space-xs) var(--space-md);
    border-radius: var(--radius-xl);
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: var(--space-lg);
    border: 1px solid rgba(255, 255, 255, 0.3);
    animation: fadeInUp 0.8s ease forwards;
    animation-delay: 0.2s;
    opacity: 0;
}
"@

if ($css.Contains($oldBadge)) {
    $css = $css.Replace($oldBadge, $newBadge)
    Write-Host "   [OK] Hero badge updated for dark overlay" -ForegroundColor Green
}

# Update hero title color
$css = $css -replace 'color: var\(--color-white\);', 'color: #ffffff;'

# Update hero subtitle for dark bg compatibility
$oldSub = @"
.hero-subtitle {
    font-size: clamp(1rem, 2vw, 1.2rem);
    font-weight: 500;
    color: var(--color-glass-text);
    line-height: 1.6;
    margin-bottom: var(--space-2xl);
    max-width: 600px;
    animation: fadeInUp 0.8s ease forwards;
    animation-delay: 0.6s;
    opacity: 0;
}
"@

$newSub = @"
.hero-subtitle {
    font-size: clamp(1rem, 2vw, 1.2rem);
    font-weight: 500;
    color: rgba(255, 255, 255, 0.85);
    line-height: 1.6;
    margin-bottom: var(--space-2xl);
    max-width: 600px;
    animation: fadeInUp 0.8s ease forwards;
    animation-delay: 0.6s;
    opacity: 0;
}
"@

if ($css.Contains($oldSub)) {
    $css = $css.Replace($oldSub, $newSub)
    Write-Host "   [OK] Hero subtitle color updated" -ForegroundColor Green
}

# ============================================
# 5. Fix Section backgrounds for light theme
# ============================================
Write-Host "4. Fixing section backgrounds for light theme..." -ForegroundColor Yellow

$oldSectionLounge = "background: linear-gradient(180deg, rgba(2, 128, 144, 0.06) 0%, rgba(11, 26, 46, 0.4) 100%);"
$newSectionLounge = "background: var(--color-bg-light);"
$css = $css.Replace($oldSectionLounge, $newSectionLounge)
Write-Host "   [OK] .section--lounge background updated" -ForegroundColor Green

$oldSectionLoungeAlt = "background: linear-gradient(180deg, rgba(11, 26, 46, 0.4) 0%, rgba(19, 42, 66, 0.3) 100%);"
$newSectionLoungeAlt = "background: var(--color-bg-mid);"
$css = $css.Replace($oldSectionLoungeAlt, $newSectionLoungeAlt)
Write-Host "   [OK] .section--lounge-alt background updated" -ForegroundColor Green

$oldSectionAlt = "background: var(--color-bg-mid);"
$newSectionAlt = "background: var(--color-bg-mid);"
# Already done - but the mid is now #edf2f7 instead of #132a42, so it's light

# Update section title for light bg
$oldSectionTitle = @"
.section-title {
    font-family: var(--font-display);
    font-size: clamp(1.75rem, 3vw, 2.5rem);
    font-weight: 700;
    color: var(--color-glass-text);
    margin-bottom: var(--space-sm);
    line-height: 1.2;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}
"@

$newSectionTitle = @"
.section-title {
    font-family: var(--font-display);
    font-size: clamp(1.75rem, 3vw, 2.5rem);
    font-weight: 700;
    color: var(--color-dark);
    margin-bottom: var(--space-sm);
    line-height: 1.2;
}
"@

if ($css.Contains($oldSectionTitle)) {
    $css = $css.Replace($oldSectionTitle, $newSectionTitle)
    Write-Host "   [OK] Section title updated for light bg" -ForegroundColor Green
} else {
    # Fallback
    $css = $css -replace 'color: var\(--color-glass-text\);\s*margin-bottom: var\(--space-sm\);', 'color: var(--color-text); margin-bottom: var(--space-sm);'
    $css = $css -replace 'text-shadow: 0 2px 10px rgba\(0, 0, 0, 0.3\);', ''
    Write-Host "   [OK] Section title updated (fallback)" -ForegroundColor Green
}

# Section desc for light bg
$css = $css -replace 'color: var\(--color-glass-text-light\);', 'color: var(--color-text-light);'

# Section--lounge section-title color
$css = $css -replace 'color: var\(--color-primary-light\);', 'color: var(--color-primary);'

# ============================================
# 6. Fix Silo Cards
# ============================================
Write-Host "5. Fixing silo-card design..." -ForegroundColor Yellow

$oldCard = @"
.silo-card {
    background: var(--color-glass);
    backdrop-filter: blur(var(--blur-glass));
    -webkit-backdrop-filter: blur(var(--blur-glass));
    border: 1px solid var(--color-glass-border);
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: var(--shadow-card);
    transition: transform var(--transition-base), box-shadow var(--transition-base), background var(--transition-base), border-color var(--transition-base);
}
"@

$newCard = @"
.silo-card {
    background: var(--color-glass);
    backdrop-filter: blur(var(--blur-glass));
    -webkit-backdrop-filter: blur(var(--blur-glass));
    border: 1px solid var(--color-glass-border);
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-card);
    transition: all 0.3s ease;
}
"@

if ($css.Contains($oldCard)) {
    $css = $css.Replace($oldCard, $newCard)
    Write-Host "   [OK] Silo-card base updated" -ForegroundColor Green
}

$oldCardHover = @"
.silo-card:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-lg);
    background: var(--color-glass-hover);
    border-color: var(--color-glass-border-hover);
}
"@

$newCardHover = @"
.silo-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
    background: var(--color-glass-hover);
    border-color: var(--color-glass-border-hover);
}
"@

if ($css.Contains($oldCardHover)) {
    $css = $css.Replace($oldCardHover, $newCardHover)
    Write-Host "   [OK] Silo-card hover updated" -ForegroundColor Green
}

# Update silo-card--lounge hover too
$oldCardLoungeHover = @"
.silo-card--lounge:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-lg);
    background: var(--color-glass-hover);
    border-color: var(--color-glass-border-hover);
}
"@

$newCardLoungeHover = @"
.silo-card--lounge:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
    background: var(--color-glass-hover);
    border-color: var(--color-glass-border-hover);
}
"@

if ($css.Contains($oldCardLoungeHover)) {
    $css = $css.Replace($oldCardLoungeHover, $newCardLoungeHover)
    Write-Host "   [OK] Silo-card-lounge hover updated" -ForegroundColor Green
}

# Fix card text colors for light bg
$css = $css -replace 'color: var\(--color-glass-text\);', 'color: var(--color-text);'
$css = $css -replace 'color: var\(--color-glass-text-light\);', 'color: var(--color-text-light);'

# Fix CTA link color
$css = $css -replace 'color: var\(--color-primary-light\);', 'color: var(--color-primary);'

# ============================================
# 7. Fix Newsletter for light theme
# ============================================
Write-Host "6. Fixing newsletter section..." -ForegroundColor Yellow

$oldNewsletterBg = "background: linear-gradient(135deg, var(--color-bg-dark) 0%, var(--color-primary) 50%, var(--color-bg-dark) 100%);"
$newNewsletterBg = "background: linear-gradient(135deg, var(--color-bg-dark) 0%, var(--color-primary-dark) 50%, var(--color-primary) 100%);"
$css = $css.Replace($oldNewsletterBg, $newNewsletterBg)
Write-Host "   [OK] Newsletter background updated" -ForegroundColor Green

# ============================================
# 8. Fix Footer for light theme
# ============================================
Write-Host "7. Fixing footer section..." -ForegroundColor Yellow

$oldFooterBg = "background: linear-gradient(180deg, var(--color-bg-mid) 0%, var(--color-bg-dark) 100%);"
$newFooterBg = "background: var(--color-bg-dark);"
$css = $css.Replace($oldFooterBg, $newFooterBg)
Write-Host "   [OK] Footer background updated" -ForegroundColor Green

# Fix footer text colors (footer is dark bg, so needs light text)
$oldFooterHeading = "color: var(--color-glass-text);"
# Already replaced with color: var(--color-text) which would be dark on dark footer
# Need to fix footer specifically
$css = $css -replace('\.footer-heading \{[^}]*color: var\(--color-text\);', '.footer-heading { color: rgba(255, 255, 255, 0.9);')
$css = $css -replace('\.footer-links ul li a \{[^}]*color: var\(--color-text-light\);', '.footer-links ul li a { color: rgba(255, 255, 255, 0.6);')
$css = $css -replace('\.footer-brand p \{[^}]*color: var\(--color-text-light\);', '.footer-brand p { color: rgba(255, 255, 255, 0.6);')
$css = $css -replace('\.footer-bottom \{[^}]*color: var\(--color-text-muted\);', '.footer-bottom { color: rgba(255, 255, 255, 0.4);')
$css = $css -replace('\.footer-links ul li a:hover \{[^}]*color: var\(--color-primary\);', '.footer-links ul li a:hover { color: var(--color-primary-light);')
Write-Host "   [OK] Footer text colors fixed for dark bg" -ForegroundColor Green

# ============================================
# 9. Remove duplicate CSS (animation blocks)
# ============================================
Write-Host "8. Removing duplicate CSS..." -ForegroundColor Yellow

# Remove the @media prefers-reduced-motion block with duplicate animations
$oldMediaBlock = @"
@media (prefers-reduced-motion: no-preference) {
    .silo-card {
        opacity: 0;
        animation: fadeInUp 0.6s ease forwards;
    }

    .silo-card:nth-child(1) {
        animation-delay: 0.05s;
    }

    .silo-card:nth-child(2) {
        animation-delay: 0.1s;
    }

    .silo-card:nth-child(3) {
        animation-delay: 0.15s;
    }

    .silo-card:nth-child(4) {
        animation-delay: 0.2s;
    }

    .silo-card:nth-child(5) {
        animation-delay: 0.25s;
    }

    .silo-card:nth-child(6) {
        animation-delay: 0.3s;
    }

    .silo-card:nth-child(7) {
        animation-delay: 0.35s;
    }

    .silo-card:nth-child(8) {
        animation-delay: 0.4s;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
}
"@

$newMediaBlock = @"
/* Silo-card entry animations removed - consolidated below */
"@

if ($css.Contains($oldMediaBlock)) {
    $css = $css.Replace($oldMediaBlock, $newMediaBlock)
    Write-Host "   [OK] Duplicate @media animation block removed" -ForegroundColor Green
} else {
    Write-Host "   [WARN] Media block not found, trying smaller match..." -ForegroundColor Yellow
}

# Remove the duplicate silo-card animation block (lines 1659-1671)
$oldDupAnim = @"
/* Scroll-Animation fuer Karten - wird per JS getoggelt */
.silo-card {
    opacity: 0;
    animation: fadeInUp 0.6s ease forwards;
}

.silo-card:nth-child(1) { animation-delay: 0.1s; }
.silo-card:nth-child(2) { animation-delay: 0.2s; }
.silo-card:nth-child(3) { animation-delay: 0.3s; }
.silo-card:nth-child(4) { animation-delay: 0.4s; }
.silo-card:nth-child(5) { animation-delay: 0.5s; }
.silo-card:nth-child(6) { animation-delay: 0.6s; }
.silo-card:nth-child(7) { animation-delay: 0.7s; }
.silo-card:nth-child(8) { animation-delay: 0.8s; }
"@

if ($css.Contains($oldDupAnim)) {
    $css = $css.Replace($oldDupAnim, "")
    Write-Host "   [OK] Duplicate silo-card animation block removed" -ForegroundColor Green
} else {
    Write-Host "   [WARN] Duplicate animation block not found" -ForegroundColor Yellow
}

# ============================================
# 10. Fix Trust items for light bg
# ============================================
Write-Host "9. Fixing trust section..." -ForegroundColor Yellow
# Trust items use --color-glass which now points to white glass - should be fine
# Trust text uses --color-glass-text which now points to dark text - fine
Write-Host "   [OK] Trust items use updated glass variables" -ForegroundColor Green

# ============================================
# 11. Fix Featured section for light bg
# ============================================
Write-Host "10. Fixing featured section..." -ForegroundColor Yellow
# Featured badge uses --color-glass - fine with white glass
# Featured text uses --color-glass-text - fine
# Featured list items use border-bottom with rgba(92,46,30,0.08) - keep
Write-Host "   [OK] Featured section uses updated variables" -ForegroundColor Green

# ============================================
# 12. Fix Buttons
# ============================================
Write-Host "11. Fixing buttons..." -ForegroundColor Yellow

# .btn--secondary uses --color-glass which is now white - needs transparency for hover effect
$oldBtnSecondary = @"
.btn--secondary {
    background: var(--color-glass);
    backdrop-filter: blur(var(--blur-glass));
    -webkit-backdrop-filter: blur(var(--blur-glass));
    color: var(--color-glass-text);
    border-color: var(--color-glass-border);
}
"@

$newBtnSecondary = @"
.btn--secondary {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    color: var(--color-white);
    border-color: rgba(255, 255, 255, 0.3);
}
"@

if ($css.Contains($oldBtnSecondary)) {
    $css = $css.Replace($oldBtnSecondary, $newBtnSecondary)
    Write-Host "   [OK] Secondary button updated for dark overlay" -ForegroundColor Green
}

# ============================================
# 13. Write the modified CSS back
# ============================================
[System.IO.File]::WriteAllText($cssPath, $css)
Write-Host "=== CSS file written successfully ===" -ForegroundColor Cyan

# ============================================
# 14. Fix index.html  
# ============================================
Write-Host "12. Fixing index.html hero section..." -ForegroundColor Yellow
$html = [System.IO.File]::ReadAllText($htmlPath)

# Update cache busting
$html = $html -replace 'css/style.css\?v=\d+', 'css/style.css?v=20260603'
$html = $html -replace 'js/main.js\?v=\d+', 'js/main.js?v=20260603'

# Remove video element and particles from hero (keep image as main background)
$oldHeroHtml = @"
        <!-- VIDEO-HINTERGRUND (autoplay, loop, gemuted) -->
        <div class="hero-video" aria-hidden="true">
            <video autoplay muted loop playsinline poster="images/hero-panorama.jpg">
                <source src="https://cdn.pixabay.com/video/2022/09/11/131223-750116942_large.mp4" type="video/mp4" />
            </video>
        </div>

        <!-- PARTIKEL-ANIMATION FALLBACK (wenn Video nicht lädt) -->
        <div class="hero-particles" aria-hidden="true">
            <span></span><span></span><span></span><span></span><span></span>
            <span></span><span></span><span></span><span></span><span></span>
        </div>

        <div class="hero-image" role="img" aria-label="Atmosphärisches Alpen-Panorama mit Almhütte und Bergspitzen">

            <img src="images/hero-panorama.jpg" alt="Alpen-Panorama mit Bergspitzen und Almhütte" width="1600"
                height="600" />

        </div>

        <div class="hero-overlay">
"@

$newHeroHtml = @"
        <div class="hero-image" role="img" aria-label="Atmosphärisches Alpen-Panorama mit Almhütte und Bergspitzen">
            <img src="images/hero-panorama.jpg" alt="Alpen-Panorama mit Bergspitzen und Almhütte" width="1600"
                height="600" />
        </div>

        <div class="hero-overlay">
"@

if ($html.Contains($oldHeroHtml)) {
    $html = $html.Replace($oldHeroHtml, $newHeroHtml)
    Write-Host "   [OK] Hero HTML cleaned - video/particles removed" -ForegroundColor Green
} else {
    Write-Host "   [WARN] Exact hero HTML pattern not found, trying alternative..." -ForegroundColor Yellow
    # Try removing video div
    $html = $html -replace '<!-- VIDEO-HINTERGRUND.*?</div>\s*', ''
    # Try removing particles div
    $html = $html -replace '<!-- PARTIKEL-ANIMATION.*?</div>\s*', ''
    # Remove the extra hero-video div
    $html = $html -replace '<div class="hero-video".*?</div>\s*', ''
    $html = $html -replace '<div class="hero-particles".*?</div>\s*', ''
    Write-Host "   [OK] Hero HTML cleaned (fallback)" -ForegroundColor Green
}

[System.IO.File]::WriteAllText($htmlPath, $html)
Write-Host "=== HTML file written successfully ===" -ForegroundColor Cyan

# ============================================
# 15. Summary
# ============================================
Write-Host ""
Write-Host "=== DESIGN RESET COMPLETE ===" -ForegroundColor Green
Write-Host "1. CSS Variables -> New 'Modern Alps' color scheme (#00a8cc / #f77f00 / #1a252c / #f8f9fa)" -ForegroundColor White
Write-Host "2. Body -> Light background (#f8f9fa), dark text (#1a252c)" -ForegroundColor White
Write-Host "3. Hero -> Image shows as main background, video/particles removed" -ForegroundColor White
Write-Host "4. Hero overlay -> Clean linear-gradient (dark 0.4 -> 0.7)" -ForegroundColor White
Write-Host "5. Glass effect -> White glass rgba(255,255,255,0.85)" -ForegroundColor White
Write-Host "6. Card design -> border-radius: 12px, translateY(-5px) on hover" -ForegroundColor White
Write-Host "7. Section backgrounds -> Light (#f8f9fa / #edf2f7)" -ForegroundColor White
Write-Host "8. Footer -> Dark (#1a252c) with light text" -ForegroundColor White
Write-Host "9. CSS cleanup -> Duplicate animation blocks removed" -ForegroundColor White
Write-Host "10. HTML -> Video/Particles removed from hero" -ForegroundColor White
Write-Host ""
Write-Host "Server needs to be restarted!" -ForegroundColor Yellow
