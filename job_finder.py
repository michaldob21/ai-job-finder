import feedparser
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

url = "https://pl.indeed.com/jobs?q=production+engineer&l=Kraków&format=rss"

feed = feedparser.parse(url)

print("\nAnaliza ofert pracy:\n")

for entry in feed.entries[:5]:

    description = entry.summary

    prompt = f"""
Oceń dopasowanie oferty pracy do studenta 4 roku Inżynierii Produkcji i Jakości AGH.

Oferta:
{description}

Oceń dopasowanie w skali 0–100 i podaj krótkie uzasadnienie.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    print("Stanowisko:", entry.title)
    print("Firma:", entry.author)
    print("Link:", entry.link)
    print("Ocena AI:", response.choices[0].message.content)
    print("-" * 50)
