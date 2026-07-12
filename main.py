from scraper import get_trending_topics
from post_generator import generate_post
from linkedIn_poster import post_to_linkedin

topics = get_trending_topics()
post = generate_post(topics)

print("Generated Post:")
print(post)

post = generate_post(topics)
if post:
    post_to_linkedin(post)