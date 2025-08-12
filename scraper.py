import os
import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_URL = "https://support.optisigns.com"
API_URL = f"{BASE_URL}/api/v2/help_center/en-us/articles.json"
OUTPUT_DIR = "data"
LIMIT = 30

def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)

def clean_html(html):
    """Remove unwanted HTML elements such as nav, footer, ads, etc."""
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all(["nav", "footer", "aside", "script", "style"]):
        tag.decompose()

    return str(soup)

def scrape_articles(limit=LIMIT):
    print("Fetching articles from Zendesk API...")
    response = requests.get(API_URL)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    articles = response.json().get("articles", [])[:limit]
    print(f"Found {len(articles)} articles.")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    added, updated, skipped = [], [], []

    for article in articles:
        title = article["title"]
        article_id = article["id"]
        html_body = article["body"]

        cleaned_html = clean_html(html_body)

        markdown_content = md(
            cleaned_html,
            heading_style="ATX",   # Use # for headings
            bullets="*",
            code_language=None,
            strip=["nav", "footer", "aside", "script", "style"]
        )

        # Add title and original URL at the top
        markdown = f"# {title}\n\n(Original link: {BASE_URL}/hc/en-us/articles/{article_id})\n\n{markdown_content}"

        filename = slugify(title) + ".md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                existing = f.read()
            if existing.strip() == markdown.strip():
                skipped.append(filepath)
                continue
            else:
                updated.append(filepath)
        else:
            added.append(filepath)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

    for path in added:
        print(f"Added: {os.path.basename(path)}")
    for path in updated:
        print(f"Updated: {os.path.basename(path)}")
    for path in skipped:
        print(f"Skipped: {os.path.basename(path)}")

    print(f"\nSummary: {len(added)} added | {len(updated)} updated | {len(skipped)} skipped")
    return added + updated

