import requests

# Put your URL directly here
url = "https://n8n-epka.onrender.com"   # replace with your URL

try:
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    print(f"Success! Status code: {resp.status_code}")
except Exception as e:
    print(f"Request failed: {e}")
