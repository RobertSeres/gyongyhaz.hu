import os
import asyncio
from playwright.async_api import async_playwright

async def audit():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Use absolute path for file:// protocol
        file_path = os.path.abspath("index.html")
        await page.goto(f"file://{file_path}")

        print("--- A11y Audit ---")

        # Check for <main> landmark
        main_exists = await page.query_selector("main")
        print(f"Main landmark exists: {bool(main_exists)}")

        # Check for skip to content link
        skip_link = await page.query_selector("a[href='#main-content']")
        print(f"Skip to content link exists: {bool(skip_link)}")

        # Check social media links for aria-labels
        social_links = await page.query_selector_all("footer a[target='_blank']")
        print(f"Found {len(social_links)} social media links in footer")
        for i, link in enumerate(social_links):
            label = await link.get_attribute("aria-label")
            href = await link.get_attribute("href")
            print(f"Social link {i} ({href}) aria-label: {label}")

        # Check footer newsletter
        newsletter_input = await page.query_selector("footer input[type='email']")
        if newsletter_input:
            label = await newsletter_input.get_attribute("aria-label")
            print(f"Footer newsletter input aria-label: {label}")
        else:
            print("Footer newsletter input not found")

        # Check close buttons for aria-labels
        close_buttons = await page.query_selector_all("button[onclick*='close']")
        print(f"Found {len(close_buttons)} close buttons")
        for i, btn in enumerate(close_buttons):
            label = await btn.get_attribute("aria-label")
            onclick = await btn.get_attribute("onclick")
            print(f"Close button {i} ({onclick}) aria-label: {label}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(audit())
