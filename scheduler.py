import schedule
import time
from scraper import get_trending_topics
from post_generator import generate_post
from linkedIn_poster import post_to_linkedin
from config import profile

def job():
    topics = get_trending_topics()
    post = generate_post(topics)
    post_to_linkedin(post)
    print("Daily post done!")

schedule.every().day.at(profile["post_time"]).do(job)

while True:
    schedule.run_pending()
    time.sleep(60)