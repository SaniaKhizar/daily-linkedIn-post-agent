import requests
from config import BUFFER_API_KEY

url = "https://api.buffer.com"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BUFFER_API_KEY}"
}
query = """
query GetChannels {
  channels(input: { organizationId: "6a282ccd75a6cdfdac641724" }) {
    id
    name
    service
  }
}
"""


response = requests.post(url, headers=headers, json={"query": query})
print(response.json())