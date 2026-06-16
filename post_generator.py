from groq import Groq
from config import profile, GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_post(topics):

    prompt= f"""
    You are a LinkedIn content expert. You can generate impressive,
    professional, friendly and eye catching posts.
    author info: {profile["name"]},
    {profile["niche"]},{profile["tone"]},
    {profile["language"]}

    today's trending topics: {topics}

    Write a linkedIn post that:
    Starts with a strong and eye catching hook
    has 150-200 words
    has 5-7 hashtags
    ends with a good question

    return only the post, nothing else.
    """
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=1000
    )
    
    return response.choices[0].message.content
   
    

if __name__ == "__main__":
    
    topics = [
        "Machine learning uncovers 1,750 quakes tracing 250-kilometer edge of Alaska microplate - Phys.org",
        "How to Fine-Tune an SLM for Emotion Recognition - Towards Data Science",
        "Anomaly Insights launches AI solution for managed care executives - Fierce Healthcare"
    ]
    
    post = generate_post(topics)
    print(post)