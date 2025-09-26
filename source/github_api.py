import requests
import logging
import json

# Logging on the INFO level
logging.basicConfig(level=logging.INFO)

# Github fine-grained personal access token
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#personal-access-tokens-classic
# Github API
# https://docs.github.com/en/rest?apiVersion=2022-11-28

GH_PAT_TOKEN = ""
GH_ORGANIZATION = ""
GH_OWNER = ""
GH_REPO = ""
GH_PATH = ""
GH_API_URL = ""
GH_API_TEST_URL = "https://api.github.com/octocat"


def github_basic_get_call(url: str, token: str) -> None:
    headers={
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
        }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        logging.info(f"Github API error code: {response.status_code}")
        return None
    else:
        logging.info(f"Github API drawing\n: {response.text}")
        logging.info(f"Github API status code: {response.status_code}")
        return None


def github_repo_data(url: str, token: str, owner: str, repo: str) -> None:
    api = f"/repos/{owner}/{repo}"
    headers={
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "Accept": "application/vnd.github+json"
        }
    response = requests.get(url+api, headers=headers)
    if response.status_code != 200:
        logging.info(f"Github repo error code: {response.status_code} {response.text}")
        return None
    else:
        # Pretty print JSON for better readability
        logging.info(f"Github repo: {repo} data:\n {json.dumps(response.json(), indent=4)}")
        return None
    

def github_repo_file_data(url: str, token: str, owner: str, repo: str, path: str) -> json:
    api = f"/repos/{owner}/{repo}/contents/{path}"
    headers={
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        # "Accept": "application/vnd.github+json",
        # "Accept": "application/vnd.github.object+json",
        "Accept": "application/vnd.github.raw+json"
        }
    response = requests.get(url+api, headers=headers)
    if response.status_code != 200:
        logging.info(f"Github repo file error code: {response.status_code} {response.text}")
        return None
    else:
        # Pretty print JSON for better readability
        # logging.info(f"Github repo: {repo} file data:\n {json.dumps(response.json(), indent=4)}")
        logging.info(f"Github repo: {repo} file data:\n {response.text}")
        return response.text


if __name__ == "__main__":
    # github_basic_get_call(GH_API_TEST_URL, GH_PAT_TOKEN)
    # github_repo_data(GH_API_URL, GH_PAT_TOKEN, GH_OWNER, GH_REPO)
    github_repo_file_data(GH_API_URL, GH_PAT_TOKEN, GH_OWNER, GH_REPO, GH_PATH)
