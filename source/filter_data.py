from github_api import github_repo_file_data
import logging

# Logging on the INFO level
logging.basicConfig(level=logging.INFO)


GH_PAT_TOKEN = ""
GH_OWNER = ""
GH_REPO = ""
GH_PATH = ""
GH_API_URL = ""


def main() -> None:
    conf_data = github_repo_file_data(GH_API_URL, GH_PAT_TOKEN, GH_OWNER, GH_REPO, GH_PATH)
    logging.info(conf_data)


if __name__ == "__main__":
    main()