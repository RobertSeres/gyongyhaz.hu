import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # Open the local index.html file
        file_path = "file://" + os.path.abspath("index.html")
        await page.goto(file_path)

        # Prevent the newsletter from appearing to avoid interception
        await page.evaluate("localStorage.setItem('newsletterClosed', 'true')")
        await page.evaluate("localStorage.setItem('reviewPopupClosed', 'true')")
        await page.reload()

        # 1. Verify ARIA labels for close buttons (check in DOM even if hidden)
        newsletter_close = page.locator('#newsletter-modal button[aria-label="Bezárás"]')
        newsletter_exists = await newsletter_close.count() > 0
        print(f"Newsletter close button ARIA label exists in DOM: {newsletter_exists}")

        coupon_close = page.locator('#coupon-modal-1 button[aria-label="Bezárás"]')
        coupon_exists = await coupon_close.count() > 0
        print(f"Coupon modal close button ARIA label exists in DOM: {coupon_exists}")

        # 2. Verify footer form functionality
        footer = page.locator('footer')
        footer_email_input = footer.locator('#footer-email')
        footer_submit_btn = footer.locator('button[type="submit"]')

        await footer_email_input.fill('test@example.com')
        # Scroll to footer
        await footer.scroll_into_view_if_needed()
        await footer_submit_btn.click()

        # Check loading state
        spinner = footer_submit_btn.locator('.loading-spinner:not(.hidden)')
        # It might be very fast, but let's check count
        has_spinner = await spinner.count() > 0
        print(f"Loading spinner detected: {has_spinner}")

        # Wait for success message
        success_msg = footer.locator('#footer-success-msg')
        await success_msg.wait_for(state="visible", timeout=5000)
        print("Success message displayed.")

        # Take a screenshot
        await page.screenshot(path="verification/ux_final_verification.png")
        print("Screenshot saved to verification/ux_final_verification.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
