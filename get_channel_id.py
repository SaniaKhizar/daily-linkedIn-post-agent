import requests
from config import BUFFER_API_KEY

url = "https://api.buffer.com"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BUFFER_API_KEY}"
}

# Step 1: run this first to get organization id
# org_query = """
# query GetOrganizations {
#   account {
#     organizations {
#       id
#     }
#   }
# }
# """

# response = requests.post(url, headers=headers, json={"query": org_query})
# print("Organization ID:", response.json())


# Step 2: run this after getting org id to fetch channel id
channel_query = """
query GetChannels {
  channels(input: { organizationId: "6a282ccd75a6cdfdac641724" }) {
    id
    name
    service
  }
}
"""

response = requests.post(url, headers=headers, json={"query": channel_query})
print("Channels:", response.json())