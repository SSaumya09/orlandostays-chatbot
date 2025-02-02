from playwright.sync_api import sync_playwright
import json

def scrape_website(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.inner_text("body")  # Extract main content
        browser.close()
    return content

# Example: Scrape main pages
pages = {
    # "homepage": scrape_website("https://myorlandostay.com/"),
    "aboutus": scrape_website("https://myorlandostay.com/Home/AboutUs"),
    "properties": scrape_website("https://myorlandostay.com/Home/Properties"),
    "attractions": scrape_website("https://myorlandostay.com/Home/AreaAttractions"),
    "contactus": scrape_website("https://myorlandostay.com/Home/ContactUs"),
}

# Save to JSON
with open("website_content.json", "w") as f:
    json.dump(pages, f, indent=4)

print("Website data scraped and saved!")
