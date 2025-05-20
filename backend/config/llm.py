import requests
import json
import re
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("GEM_API_KEY")  # Replace with your actual Gemini API key
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-04-17:generateContent?key={API_KEY}"

def clean_text(text):
    text = text.replace('\n', ' ').replace('\r', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def call_gemini_api(prompt_text):
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt_text}
                ]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Gemini API error {response.status_code}: {response.text}")
        return None
    
    resp_json = response.json()
    try:
        # Extract the generated text from response
        return resp_json["candidates"][0]["content"]
    except (KeyError, IndexError) as e:
        print("Error extracting content from Gemini response:", e)
        print(resp_json)
        return None

def summarize_articles(articles):
    combined_text = "\n\n".join([f"Article {i+1}:\n{clean_text(text)}" for i, text in enumerate(articles)])
    city="bangalore"
    prompt = f"""
You are a disaster analysis assistant tasked with summarizing multiple news articles about natural or urban disasters. Your job is to extract structured information **strictly** and **sensitively** for only **{city}**, with proper severity classification based on real-world impact.

=== 🔥 Severity Classification Criteria (Use Carefully) ===

- **Severe**:
  - **Only use this if** there is **official deployment of NDRF, Army, Air Force**, or equivalent international emergency services.
  - Requires large-scale evacuation, deaths, loss of infrastructure, or humanitarian crisis.
  - Use **ONLY when** such official rescue aid is mentioned.
  - Examples:
    - **Kerala Floods 2019**: Army + NDRF + relief camps + deaths.
    - **Turkey Earthquakes**: International rescue teams, thousands dead.
  - 🔐 If no national/international aid or military mentioned, DO NOT use "severe".

- **Moderate**:
  - Significant urban disruptions: multiple neighborhoods affected, waterlogging, power cuts, blocked roads.
  - **Handled locally** (e.g. BBMP, BMC, city helpline) with **no military involvement**.
  - **Do NOT mark Bengaluru seasonal floods as severe.** Example:
    - Bengaluru rains causing waterlogging in tech parks and traffic jams is "moderate".

- **Mild**:
  - Localized and temporary incidents. Minor inconvenience, quickly resolved.
  - No long-term damage or institutional involvement.

=== 🔍 Extract These in JSON Format ===

Return a valid JSON object:
{{
  "disaster_types": [],
  "overall_severity": null,
  "key_dates": [],
  "locations": [],
  "additional_info": null
}}

Use `null` or empty lists if data is missing.

=== 📄 Articles ===
\"\"\"{combined_text}\"\"\"
"""



    return call_gemini_api(prompt)

def main():
    import pandas as pd

    df = pd.read_csv("articles_with_text2.csv")
    all_texts = df["articleText"].dropna().tolist()

    if not all_texts:
        print("No article texts found in CSV!")
        return

    print(f"Processing {len(all_texts)} articles collectively...")
    raw_summary = summarize_articles(all_texts)

    print("=== Disaster Summary ===")
    if raw_summary:
        # Extract the JSON from the Markdown block (```json ... ```)
        try:
            text = raw_summary["parts"][0]["text"]
            json_start = text.find("{")
            json_end = text.rfind("}") + 1
            json_str = text[json_start:json_end]
            summary = json.loads(json_str)
        except Exception as e:
            print("❌ Failed to parse JSON from response:", e)
            print("Raw response was:", raw_summary)
            return

        print(json.dumps(summary, indent=2))

        with open("disaster_summary.json", "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        print("✅ Summary saved to disaster_summary.json")
    else:
        print("❌ Failed to get a summary.")


if __name__ == "__main__":
    main()
