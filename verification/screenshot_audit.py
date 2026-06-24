import os
import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        file_path = os.path.abspath("index.html")
        await page.goto(f"file://{file_path}")

        # Test skip to content visibility on focus
        await page.keyboard.press("Tab")
        # Depending on browser behavior, we might need a few more tabs to reach it
        # but as first child it should be first.

        await page.screenshot(path="verification/focus_skip_link.png")

        # Open coupon accordion to see the cards
        await page.click("summary:has-text('Kuponok')")
        await asyncio.sleep(0.5)
        await page.screenshot(path="verification/coupon_cards.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
