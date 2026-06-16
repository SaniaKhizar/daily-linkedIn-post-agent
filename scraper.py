from gnews import GNews

def get_trending_topics():
    google_news = GNews(language='en', max_results=5)
    
    titles = []
    
    queries = ["artificial intelligence", "machine learning"]
    
    for query in queries:
        results = google_news.get_news(query)
        for article in results:
            titles.append(article['title'])
    
    return titles

if __name__ == "__main__":
    topics = get_trending_topics()
    print(f"Total topics found: {len(topics)}")
    for i, title in enumerate(topics, 1):
        print(f"{i}. {title}")

