"""
Automated Screenshot Generator for PHP 8.5 Contest Submission
Generates all required screenshots at different screen sizes using Playwright.

Requirements:
    pip install playwright pillow
    playwright install chromium

Usage:
    python scripts/generate_screenshots.py
"""

import os
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
HTML_FILE = PROJECT_ROOT / "src" / "index.html"
OUTPUT_DIR = PROJECT_ROOT / "images"

# Screen sizes (width, height)
VIEWPORTS = {
    "mobile": {"width": 375, "height": 667, "device": "iPhone SE"},
    "tablet": {"width": 768, "height": 1024, "device": "iPad"},
    "desktop": {"width": 1280, "height": 800, "device": "Laptop"},
    "desktop_full": {"width": 1920, "height": 1080, "device": "Desktop 1080p"}
}

# Screenshot specifications
SCREENSHOTS = {
    "mobile": [
        {"name": "mobile-full-page", "fullpage": True, "description": "Complete mobile page view"},
        {"name": "mobile-hero", "selector": ".hero", "description": "Hero section with PHP 8.5 badge"},
        {"name": "mobile-foundation", "selector": ".foundation-banner", "description": "PHP Foundation banner"},
        {"name": "mobile-features", "selector": ".features", "description": "Feature cards stacked"},
        {"name": "mobile-whats-new", "selector": ".whats-new", "description": "What's New section"},
        {"name": "mobile-conferences", "selector": ".conferences", "description": "Upcoming conferences"},
        {"name": "mobile-social", "selector": ".footer__social", "description": "Social media links"},
        {"name": "mobile-footer", "selector": ".footer", "description": "Complete footer"}
    ],
    "tablet": [
        {"name": "tablet-full-page", "fullpage": True, "description": "Complete tablet page view"},
        {"name": "tablet-hero", "selector": ".hero", "description": "Hero section"},
        {"name": "tablet-features", "selector": ".features", "description": "Feature cards (2 columns)"},
        {"name": "tablet-conferences", "selector": ".conferences", "description": "Conference cards"},
        {"name": "tablet-footer", "selector": ".footer", "description": "Footer layout"}
    ],
    "desktop": [
        {"name": "desktop-full-page", "fullpage": True, "description": "Complete desktop page view"},
        {"name": "desktop-hero", "selector": ".hero", "description": "Hero section full width"},
        {"name": "desktop-foundation", "selector": ".foundation-banner", "description": "Foundation banner"},
        {"name": "desktop-features", "selector": ".features", "description": "Feature cards (3 columns)"},
        {"name": "desktop-whats-new", "selector": ".whats-new", "description": "What's New highlights"},
        {"name": "desktop-conferences", "selector": ".conferences", "description": "Conference grid"},
        {"name": "desktop-special-thanks", "selector": ".special-thanks", "description": "Special Thanks section"},
        {"name": "desktop-footer", "selector": ".footer", "description": "Complete footer"}
    ],
    "hover-states": [
        {"name": "hover-download-button", "selector": ".btn--primary", "hover": True, "description": "Primary CTA button hover"},
        {"name": "hover-feature-card", "selector": ".feature-card:first-child", "hover": True, "description": "Feature card hover elevation"},
        {"name": "hover-social-link", "selector": ".footer__social-link:first-child", "hover": True, "description": "Social link glassmorphism effect"},
        {"name": "hover-donate-button", "selector": ".btn--donate", "hover": True, "description": "Donate button hover"},
        {"name": "hover-conference-card", "selector": ".conference-card:first-child", "hover": True, "description": "Conference card hover"}
    ]
}


async def capture_screenshot(page, spec, output_path, viewport_name="desktop"):
    """Capture a single screenshot based on specification."""
    try:
        # Wait for page to be fully loaded
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(0.5)  # Additional wait for animations
        
        # Handle full-page screenshots
        if spec.get("fullpage"):
            await page.screenshot(path=output_path, full_page=True)
            print(f"  ✅ {spec['name']}.png (full page)")
            return
        
        # Handle hover states
        if spec.get("hover"):
            element = await page.query_selector(spec["selector"])
            if element:
                await element.hover()
                await asyncio.sleep(0.3)  # Wait for hover animation
        
        # Capture screenshot
        if spec.get("full_page"):
            await page.screenshot(path=output_path, full_page=True)
        else:
            element = await page.query_selector(spec["selector"])
            if element:
                await element.screenshot(path=output_path)
            else:
                print(f"  ⚠️  Element not found: {spec['selector']}")
                return False
        
        # Get file size
        size_kb = os.path.getsize(output_path) / 1024
        print(f"  ✅ {output_path.name} ({size_kb:.1f} KB)")
        return True
        
    except Exception as e:
        print(f"  ❌ Error capturing {spec['name']}: {str(e)}")
        return False


async def generate_screenshots():
    """Generate all screenshots using Playwright."""
    
    # Verify HTML file exists
    if not HTML_FILE.exists():
        print(f"❌ HTML file not found: {HTML_FILE}")
        return
    
    # Create output directories
    for folder in ["mobile", "tablet", "desktop", "hover-states"]:
        (OUTPUT_DIR / folder).mkdir(parents=True, exist_ok=True)
    
    print("🚀 Starting screenshot generation...\n")
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        
        # Generate mobile screenshots
        print("📱 Mobile Screenshots (375px)")
        context = await browser.new_context(
            viewport={"width": VIEWPORTS["mobile"]["width"], "height": VIEWPORTS["mobile"]["height"]},
            device_scale_factor=2  # Retina display
        )
        page = await context.new_page()
        await page.goto(f"file://{HTML_FILE.absolute()}")
        
        for spec in SCREENSHOTS["mobile"]:
            output_path = OUTPUT_DIR / "mobile" / f"{spec['name']}.png"
            await capture_screenshot(page, spec, output_path, "mobile")
        
        await context.close()
        print()
        
        # Generate tablet screenshots
        print("📱 Tablet Screenshots (768px)")
        context = await browser.new_context(
            viewport={"width": VIEWPORTS["tablet"]["width"], "height": VIEWPORTS["tablet"]["height"]},
            device_scale_factor=2
        )
        page = await context.new_page()
        await page.goto(f"file://{HTML_FILE.absolute()}")
        
        for spec in SCREENSHOTS["tablet"]:
            output_path = OUTPUT_DIR / "tablet" / f"{spec['name']}.png"
            await capture_screenshot(page, spec, output_path, "tablet")
        
        await context.close()
        print()
        
        # Generate desktop screenshots
        print("🖥️  Desktop Screenshots (1280px)")
        context = await browser.new_context(
            viewport={"width": VIEWPORTS["desktop"]["width"], "height": VIEWPORTS["desktop"]["height"]},
            device_scale_factor=2
        )
        page = await context.new_page()
        await page.goto(f"file://{HTML_FILE.absolute()}")
        
        for spec in SCREENSHOTS["desktop"]:
            output_path = OUTPUT_DIR / "desktop" / f"{spec['name']}.png"
            await capture_screenshot(page, spec, output_path, "desktop")
        
        await context.close()
        print()
        
        # Generate hover state screenshots (at desktop size)
        print("✨ Hover State Screenshots (1280px)")
        context = await browser.new_context(
            viewport={"width": VIEWPORTS["desktop"]["width"], "height": VIEWPORTS["desktop"]["height"]},
            device_scale_factor=2
        )
        page = await context.new_page()
        await page.goto(f"file://{HTML_FILE.absolute()}")
        
        for spec in SCREENSHOTS["hover-states"]:
            output_path = OUTPUT_DIR / "hover-states" / f"{spec['name']}.png"
            await capture_screenshot(page, spec, output_path, "desktop")
        
        await context.close()
        print()
        
        await browser.close()
    
    print("✅ Screenshot generation complete!")
    print(f"\n📁 Screenshots saved to: {OUTPUT_DIR.absolute()}")
    print("\n📊 Summary:")
    
    # Count screenshots
    total_size = 0
    total_count = 0
    for folder in ["mobile", "tablet", "desktop", "hover-states"]:
        folder_path = OUTPUT_DIR / folder
        if folder_path.exists():
            files = list(folder_path.glob("*.png"))
            folder_size = sum(f.stat().st_size for f in files)
            total_size += folder_size
            total_count += len(files)
            print(f"  {folder}/: {len(files)} files ({folder_size / 1024:.1f} KB)")
    
    print(f"\n  Total: {total_count} screenshots ({total_size / 1024:.1f} KB)")
    print(f"\n💡 Next steps:")
    print(f"  1. Review screenshots in {OUTPUT_DIR.absolute()}")
    print(f"  2. Optimize with TinyPNG if needed (keep under 500KB each)")
    print(f"  3. Include in GitHub issue for contest submission")


if __name__ == "__main__":
    print("=" * 60)
    print("  PHP 8.5 Contest - Screenshot Generator")
    print("  Updated for new page structure with conferences section")
    print("=" * 60)
    print()
    
    asyncio.run(generate_screenshots())
