import requests
import pandas as pd
from bs4 import BeautifulSoup
from newspaper import Article
import time

API_KEY = "15ba1fdbb76f49ab7b2e39e98f4b0b52ec796c8f"
SEARCH_QUERY = "delhi air pollution may 2025"
NUM_RESULTS = 10

def search_images(query, api_key, num_results=10):
    url = "https://google.serper.dev/images"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    body = {
        "q": query
    }

    response = requests.post(url, json=body, headers=headers)
    if response.status_code != 200:
        print(f"❌ Error: {response.status_code} - {response.text}")
        return []

    images = response.json().get("images", [])
    return images[:num_results]

def extract_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text.strip()
        if text:
            return text
    except Exception as e:
        print(f"[Newspaper Error] {url}: {e}")

    # Fallback: simple BeautifulSoup text extraction
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, "html.parser")

        # Extract all paragraph texts joined
        paragraphs = soup.find_all("p")
        text = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        return text if text else ""
    except Exception as e:
        print(f"[BS4 Fallback Error] {url}: {e}")

    return ""

def extract_image_data(images):
    data = []
    for img in images:
        source_url = img.get("link") or img.get("sourceUrl")
        article_text = extract_article_text(source_url) if source_url else ""

        data.append({
            "title": img.get("title"),
            "imageUrl": img.get("imageUrl"),
            "thumbnailUrl": img.get("thumbnailUrl"),
            "sourceUrl": source_url,
            "sourceName": img.get("sourceName"),
            "height": img.get("height"),
            "width": img.get("width"),
            "domain": img.get("domain"),
            "description": img.get("description") or "",
            "articleText": article_text
        })
        time.sleep(1)  # avoid hammering servers
    return data

images = search_images(SEARCH_QUERY, API_KEY, NUM_RESULTS)
image_data = extract_image_data(images)

df = pd.DataFrame(image_data)
df.to_csv("articles_with_text2.csv", index=False, encoding='utf-8')
print("✅ Saved detailed image search results with full article text to 'search_images_with_full_article_text.csv'")
