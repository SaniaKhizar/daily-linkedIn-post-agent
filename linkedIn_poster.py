import requests
from config import BUFFER_API_KEY, CHANNEL_ID

def post_to_linkedin(post_content):
    url = "https://api.buffer.com"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BUFFER_API_KEY}"
    }
    
    query = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post {
            id
            text
          }
        }
        ... on MutationError {
          message
        }
      }
    }
    """
    
    variables = {
        "input": {
            "text": post_content,
            "channelId": CHANNEL_ID,
            "schedulingType": "automatic",
            "mode": "shareNow"
        }
    }
    
    response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
    print(response.json())