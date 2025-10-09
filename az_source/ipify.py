import requests
import logging
from urllib3.exceptions import InsecureRequestWarning

# Logging on the INFO level
logging.basicConfig(level=logging.INFO)

# Suppress certificate warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

ipify_url = "https://api.ipify.org"


def get_public_ip(url: str) -> None:
    response = requests.get(url, verify=False)
    if response.status_code != 200:
        logging.info(f"Error fetching public IP: {response.status_code}")
        return None
    else:
        logging.info(f"Public IP Address: {response.text}")
        return None


if __name__ == "__main__":
    get_public_ip(ipify_url)
