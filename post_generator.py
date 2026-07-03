import random
import json
import os
from groq import Groq
from config import profile, GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

HISTORY_FILE = "post_history.json"

def load_recent_posts(limit=5):
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    return history[-limit:]

def save_post_to_history(post_text):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    
    history.append(post_text)
    history = history[-10:]  
    
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def generate_post(topics):
    styles = [
        "a thought-provoking question as the hook",
        "a surprising statistic or fact as the hook",
        "a bold personal opinion or statement as the hook",
        "a short relatable scenario or mini-story as the hook"
    ]
    chosen_style = random.choice(styles)
    
    recent_posts = load_recent_posts()
    avoid_repetition = ""
    if recent_posts:
        avoid_repetition = f"""
    Avoid repeating the themes, phrasing, or structure of these recent posts:
    {recent_posts}
    """

    prompt = f"""
    You are a LinkedIn content expert. You can generate impressive,
    professional, friendly and eye catching posts.
    author info: {profile["name"]},
    {profile["niche"]},{profile["tone"]},
    {profile["language"]}

    today's trending topics: {topics}

    Write a linkedIn post that:
    Starts with {chosen_style}
    has 150-200 words and write in 2 paragraphs 
    post ending with a good question
    then add 5-7 hashtags
    {avoid_repetition}

    return only the post, nothing else.
    """
    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    
    post_text = response.choices[0].message.content
    save_post_to_history(post_text)
    
    return post_text


if __name__ == "__main__":
    topics = [
        "Machine learning uncovers 1,750 quakes tracing 250-kilometer edge of Alaska microplate - Phys.org",
        "How to Fine-Tune an SLM for Emotion Recognition - Towards Data Science",
        "Anomaly Insights launches AI solution for managed care executives - Fierce Healthcare"
    ]
    
    post = generate_post(topics)
    print(post)