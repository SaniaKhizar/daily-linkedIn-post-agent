import requests
from config import BUFFER_API_KEY

url = "https://api.buffer.com"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BUFFER_API_KEY}"
}

# Step 1: Pehle yeh run karo — Organization ID nikalne ke liye
org_query = """
query GetOrganizations {
  account {
    organizations {
      id
    }
  }
}
"""

org_response = requests.post(url, headers=headers, json={"query": org_query})
org_id = org_response.json()["data"]["account"]["organizations"][0]["id"]
print(f"Organization ID: {org_id}")

# Step 2: Upar se mila hua org_id automatically yahan use hoga
channel_query = """
query GetChannels($orgId:  OrganizationId!) {
  channels(input: { organizationId: $orgId }) {
    id
    name
    service
  }
}
"""

channel_response = requests.post(url, headers=headers, json={
    "query": channel_query,
    "variables": {"orgId": org_id}
})

print("\nYour Channels:")
print(channel_response.json())
for channel in channel_response.json()["data"]["channels"]:
    print(f"Service: {channel['service']} | Name: {channel['name']} | ID: {channel['id']}")