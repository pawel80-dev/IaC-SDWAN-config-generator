from github_api import github_repo_file_data
import logging

# Logging on the INFO level
logging.basicConfig(level=logging.INFO)

# SDWAN inteface - tunnel mapping
# https://lostintransit.se/2022/05/14/using-python-to-calculate-cisco-sd-wan-tunnel-numbers-part-1/?doing_wp_cron=1758563977.3016180992126464843750
# Loopback0                 - Tunnel14095000
# GigabitEthernet0/0/0      - Tunnel0
# GigabitEthernet0/0/1      - Tunnel1
# GigabitEthernet0/0/2      - Tunnel2
# GigabitEthernet0/1/0      - Tunnel10
# GigabitEthernet1/0/0      - Tunnel100
# TengigabitEthernet0/1/0   - Tunnel10000010


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