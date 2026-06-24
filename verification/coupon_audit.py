import os
import asyncio
from playwright.async_api import async_playwright

async def audit():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        file_path = os.path.abspath("index.html")
        await page.goto(f"file://{file_path}")

        print("--- Coupon Keyboard Accessibility Audit ---")

        # Check for coupon cards
        coupon_cards = await page.query_selector_all("div[role='button'][aria-label*='bérlet']")
        print(f"Found {len(coupon_cards)} accessible coupon cards")

        for i, card in enumerate(coupon_cards):
            role = await card.get_attribute("role")
            tabindex = await card.get_attribute("tabindex")
            aria_label = await card.get_attribute("aria-label")
            onkeydown = await card.get_attribute("onkeydown")
            print(f"Card {i}: role={role}, tabindex={tabindex}, label={aria_label}")
            print(f"Card {i} onkeydown: {onkeydown[:50]}...")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(audit())
