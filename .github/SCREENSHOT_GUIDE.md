# 📸 Screenshot Guide for Contest Submission

## Quick Reference

**You need**: 3-5 high-quality screenshots showing desktop + mobile views  
**Format**: PNG (best quality)  
**Resolution**: 1280x720 minimum (retina/2x recommended)  
**File size**: <500KB per image (optimize if needed)

---

## Screenshot Tools

### macOS
```bash
# Full screenshot: Cmd + Shift + 3
# Selected area: Cmd + Shift + 4 (then drag)
# Window capture: Cmd + Shift + 4, then press Space, click window
```

### Windows
```bash
# Snipping Tool: Win + Shift + S (select area)
# Full screenshot: Win + PrtScn (saves to Pictures/Screenshots)
```

### Browser DevTools (Any OS)
```
1. Open page in Chrome/Firefox
2. Press F12 (DevTools)
3. Click device toolbar icon (top-left)
4. Select viewport size (375px, 768px, 1280px)
5. Right-click page → "Capture screenshot"
```

---

## Required Screenshots

### 1️⃣ Desktop Hero Section (REQUIRED)
**Purpose**: Show full hero section with PHP logo, badge, CTAs, and Foundation banner

**Setup**:
- Viewport: 1280px width (or wider)
- Browser: Chrome (recommended for consistency)
- Zoom: 100%
- Capture: From top of page to bottom of Foundation banner

**Checklist**:
- [ ] PHP logo visible (external from php.net)
- [ ] "Version 8.5" badge with glassmorphism
- [ ] Gradient purple background (#777BB3 → #4F5B93)
- [ ] Both CTAs visible (Download + Release Notes)
- [ ] Foundation banner with purple borders
- [ ] "Donate 💜" button prominent

**File name**: `screenshot-desktop-hero.png`

---

### 2️⃣ Mobile View (REQUIRED)
**Purpose**: Demonstrate mobile-first responsive design

**Setup**:
- Viewport: 375px × 667px (iPhone SE)
- Browser DevTools device mode
- Capture: Hero + Foundation + first 2 feature cards

**Checklist**:
- [ ] Stacked layout (single column)
- [ ] CTAs full-width
- [ ] Text readable (no overflow)
- [ ] Touch targets 44px minimum
- [ ] Foundation banner stacked text/buttons

**File name**: `screenshot-mobile-view.png`

---

### 3️⃣ Feature Cards Grid (REQUIRED)
**Purpose**: Showcase interactive card design with hover effects

**Setup**:
- Viewport: 1280px width
- Capture: All 6 feature cards section
- **Bonus**: Use DevTools to force :hover state on one card

**Checklist**:
- [ ] All 6 cards visible (Property Hooks, PDO, Performance, APIs, Types, Security)
- [ ] Gradient icon badges (PH, PD, ⚡, 🔧, TS, 🔒)
- [ ] One card with hover state (lifted shadow)
- [ ] Grid layout clear (3 columns on desktop)
- [ ] Card borders visible (#E0E0E0)

**File name**: `screenshot-feature-cards.png`

---

### 4️⃣ Social Media Section with Hover (RECOMMENDED)
**Purpose**: Highlight premium glassmorphism design on social buttons

**Setup**:
- Viewport: 1280px width
- Scroll to footer
- **Important**: Use DevTools to force :hover on one social button
  1. Right-click social button → Inspect
  2. In Styles panel, click `:hov` toggle
  3. Check `:hover` checkbox

**Checklist**:
- [ ] All 3 social buttons visible (Twitter, Mastodon, LinkedIn)
- [ ] One button hovered: gradient overlay (#777BB3 → #4F5B93)
- [ ] White text on purple gradient (hover state)
- [ ] Scale/lift animation visible
- [ ] Glassmorphism effect on non-hovered buttons

**File name**: `screenshot-social-hover.png`

---

### 5️⃣ Foundation Banner Close-Up (OPTIONAL)
**Purpose**: Show php.net-inspired community section

**Setup**:
- Viewport: 1280px width
- Crop to just Foundation banner section

**Checklist**:
- [ ] "The PHP Foundation" title
- [ ] Description text visible
- [ ] "Learn More" button (white bg, purple text)
- [ ] "Donate 💜" button (purple bg, white text, shadow)
- [ ] Purple top/bottom borders (3px)
- [ ] Gray gradient background (#F7F7F9 → #E8E8F0)

**File name**: `screenshot-foundation-banner.png`

---

## How to Force Hover States (DevTools)

Many hover effects are subtle—here's how to capture them:

### Method 1: Element State Toggle
```
1. Right-click element → Inspect
2. In Styles panel (right side), click ":hov" button
3. Check ":hover" checkbox
4. Element now shows hover styles
5. Take screenshot
```

### Method 2: Console Trick
```javascript
// Add class to simulate hover
document.querySelector('.footer__social-link').classList.add('hover-state');

// Then in CSS, add:
// .footer__social-link.hover-state { /* copy hover styles */ }
```

### Method 3: Mouse Position (Fastest)
```
1. Open DevTools screenshot tool (Cmd/Ctrl+Shift+P → "Capture node screenshot")
2. Hover over element with mouse
3. Press keyboard shortcut while hovering
4. Screenshot captures hover state
```

---

## Image Optimization (If Files Too Large)

### Online Tools
- [TinyPNG](https://tinypng.com/) — Lossy compression (best quality/size ratio)
- [Squoosh](https://squoosh.app/) — Advanced controls (Google tool)
- [ImageOptim](https://imageoptim.com/mac) — macOS app (lossless + lossy)

### Command Line
```bash
# macOS/Linux with ImageMagick
convert screenshot.png -quality 85 -resize 1280x screenshot-optimized.png

# With pngquant (best for PNGs)
pngquant --quality=80-95 screenshot.png --output screenshot-optimized.png
```

### Target Sizes
- Desktop screenshots: <400KB each
- Mobile screenshots: <200KB each
- Total for 5 images: <1.5MB

---

## Viewport Presets (Browser DevTools)

### Recommended Test Sizes

| Device | Width | Height | Notes |
|--------|-------|--------|-------|
| iPhone SE | 375px | 667px | Smallest modern mobile |
| iPhone 12/13 | 390px | 844px | Common iOS size |
| iPad | 768px | 1024px | Tablet portrait |
| Desktop (Small) | 1280px | 720px | Minimum desktop |
| Desktop (Large) | 1920px | 1080px | Full HD |
| 4K | 3840px | 2160px | Edge case testing |

---

## Screenshot Composition Tips

### Do ✅
- Use consistent browser chrome (Chrome recommended)
- Capture at 100% zoom (no browser zoom in/out)
- Show cursor if highlighting interactive element
- Include enough context (hero + banner together, not separate)
- Use high-DPI/retina screenshots (2x resolution looks sharper)

### Don't ❌
- Mix browsers (all Chrome or all Firefox)
- Crop too tight (leave breathing room)
- Capture during load (wait for fonts/images)
- Include browser bookmarks bar (clean UI)
- Use dark mode (unless showcasing dark theme)

---

## Accessibility Screenshot (Bonus Points)

### Skip Link Focus State
**Purpose**: Prove keyboard navigation works

**Setup**:
1. Open page in browser
2. Press Tab (don't use mouse)
3. Skip link appears at top-left
4. Take screenshot showing blue focus outline

**File name**: `screenshot-accessibility-skip-link.png`

### High Contrast Mode (Windows)
**Purpose**: Show design works in accessibility modes

**Setup**:
1. Windows: Settings → Accessibility → Contrast themes → Select "Aquatic"
2. Open page
3. Take screenshot

**File name**: `screenshot-high-contrast.png`

---

## Final Checklist Before Upload

- [ ] 3-5 screenshots ready (PNG format)
- [ ] All images <500KB each
- [ ] Retina/2x resolution (2560x1440 or higher)
- [ ] No personal info visible (bookmarks, browser extensions)
- [ ] Consistent browser UI across all screenshots
- [ ] Hover states captured correctly
- [ ] Mobile + desktop views included
- [ ] File names descriptive (screenshot-desktop-hero.png, not IMG_1234.png)

---

## Where to Upload for GitHub Issue

### Option 1: GitHub Issue Attachments (Easiest)
```
1. Create GitHub issue (don't submit yet)
2. Drag & drop PNG files into comment box
3. GitHub auto-uploads and generates ![](url)
4. Preview before submitting
```

### Option 2: GitHub Repository (Permanent)
```bash
# Create screenshots folder
mkdir screenshots
cd screenshots

# Copy your screenshot files here
cp ~/Desktop/screenshot-*.png .

# Commit to repo
git add screenshots/
git commit -m "Add contest submission screenshots"
git push

# Link in issue: https://github.com/user/repo/blob/main/screenshots/screenshot-desktop-hero.png
```

### Option 3: External Host (Imgur, etc.)
```
1. Upload to Imgur.com (anonymous, free)
2. Copy direct image URL (ends with .png)
3. Paste in GitHub issue markdown: ![Description](https://i.imgur.com/abc123.png)
```

---

## Example Issue Markdown

```markdown
## Screenshots

### Desktop Hero Section
![Desktop Hero](https://github.com/user/repo/blob/main/screenshots/screenshot-desktop-hero.png)

### Mobile View
![Mobile View](https://github.com/user/repo/blob/main/screenshots/screenshot-mobile-view.png)

### Feature Cards with Hover
![Feature Cards](https://github.com/user/repo/blob/main/screenshots/screenshot-feature-cards.png)

### Social Media Hover Effect
![Social Media Hover](https://github.com/user/repo/blob/main/screenshots/screenshot-social-hover.png)

### PHP Foundation Banner
![Foundation Banner](https://github.com/user/repo/blob/main/screenshots/screenshot-foundation-banner.png)
```

---

## Time Estimate

- **Taking screenshots**: 15 minutes
- **Optimizing images**: 5 minutes
- **Uploading to GitHub**: 5 minutes
- **Total**: ~25 minutes

---

## Need Help?

If screenshots look blurry or pixelated:
1. Check browser zoom is 100% (Cmd/Ctrl+0)
2. Use retina/2x display if available
3. Save as PNG (not JPG — JPG adds compression artifacts)
4. Use DevTools screenshot (Cmd+Shift+P → "Capture screenshot")

If hover states won't capture:
1. Use DevTools :hov toggle (see Method 1 above)
2. Or use video screen recording, pause on hover, screenshot video frame

If file sizes too large:
1. Run through TinyPNG.com (can reduce 50-70% with no visible quality loss)
2. Or resize to exactly 1280px width (don't go larger than needed)

---

**Remember**: Judges care about design quality, not photo quality. Clean, clear screenshots showing your work are enough. Don't overthink it. 📸
