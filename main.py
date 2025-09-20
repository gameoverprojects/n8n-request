import requests
import time
import logging

url = "https://n8n-epka.onrender.com"   # replace with your URL
timeout = 20                       # seconds before a single request times out
retry_delay = 50                   # wait time between retries (seconds)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def send_request_until_success(url: str):
    while True:
        try:
            logging.info(f"Sending GET request -> {url}")
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()  # raise error for 4xx/5xx
            logging.info(f"Success! Status code: {resp.status_code}")
            break   # stop once successful
        except Exception as e:
            logging.warning(f"Request failed: {e}")
            logging.info(f"Retrying in {retry_delay}s...")
            time.sleep(retry_delay)

if __name__ == "__main__":
    send_request_until_success(url)
