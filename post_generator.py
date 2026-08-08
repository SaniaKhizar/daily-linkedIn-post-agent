import random
import json
import os
import time
import re
from openai import OpenAI
from config import profile, OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

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

def clean_post(text):
    # <think> tags remove karo
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)

    # Agar model ne planning/reasoning likhi to sirf actual post lo
    triggers = ["let's draft", "let's write", "word count", "we need to",
                "structure:", "hook (", "let's craft", "now count",
                "we'll", "i'll", "first example", "second example"]

    lower = text.lower()
    for trigger in triggers:
        if trigger in lower:
            paragraphs = [p.strip() for p in text.strip().split('\n\n') if p.strip()]
            text = '\n\n'.join(paragraphs[-3:])
            break

    return text.strip()

# Best models pehle — jo seedha post dete hain
FREE_MODELS = [
    "openai/gpt-oss-120b:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "google/gemma-4-31b-it:free",
    "google/gemma-4-26b-a4b-it:free"
]

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
    You are a LinkedIn content expert helping an AI and CS student create authentic, engaging posts.

    Author background:
    - Name: {profile["name"]}
    - Currently in 5th semester of Computer Science
    - Completed subjects: Programming fundamentals, OOP, Data Structures, Computer Architecture, Discrete Math, Linear Algebra, Calculus, Digital Logic Design, Database Systems
    - Currently learning: Machine Learning basics, AI fundamentals
    - Has basic understanding of: Deep Learning concepts
    - Just starting to explore: AI Automation, RAG (Retrieval Augmented Generation)
    - Passionate about Python and AI
    - Tone: {profile["tone"]}
    - Language: {profile["language"]}

    Today's trending AI/ML topics: {topics}

    Write a LinkedIn post that:
    - Starts with a powerful hook (first 2-3 lines must grab attention)
    - Reflects a genuine student learning journey — curiosity, discovery, questions
    - Connects the trending topic to something relatable from CS coursework or current learning
    - Has 150-200 words
    - Has 5-7 relevant hashtags at the end
    - Ends with a thought-provoking question
    - Uses {chosen_style}
    {avoid_repetition}

    STRICT RULES:
    - Do NOT use ** or * or any markdown formatting
    - Do NOT use <think> tags or show reasoning
    - Do NOT exaggerate skills — write honestly as someone still learning
    - Do NOT claim to have done research, projects, or work not mentioned above
    - Sound like a curious CS student, not an industry expert
    - Return only the post text, nothing else
    """

    for model in FREE_MODELS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a LinkedIn post writer. Output ONLY the final LinkedIn post text. No thinking. No planning. No word counts. No explanations. Just the post."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000
            )
            post_text = response.choices[0].message.content
            post_text = clean_post(post_text)
            save_post_to_history(post_text)
            print(f"Success with model: {model}")
            return post_text

        except Exception as e:
            print(f"{model} failed: {e}")
            time.sleep(10)
            continue
            
    print("All models failed!")
    return None


if __name__ == "__main__":
    topics = [
        "Machine learning uncovers 1,750 quakes",
        "How to Fine-Tune an SLM for Emotion Recognition",
        "AI solution for managed care executives"
    ]
    post = generate_post(topics)
    print(post)

