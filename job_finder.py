import feedparser

# RSS feed z ofertami pracy
url = "https://pl.indeed.com/jobs?q=production+engineer&l=Kraków&format=rss"

feed = feedparser.parse(url)

print("Nowe oferty pracy:\n")

for entry in feed.entries[:10]:
    print("Stanowisko:", entry.title)
    print("Firma:", entry.author)
    print("Link:", entry.link)
    print("-" * 40)
