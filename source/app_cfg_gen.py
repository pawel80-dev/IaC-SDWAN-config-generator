import os
import sys
from manager_api import manager_jsession_id, manager_token, manager_logout,\
                        manager_bootstrap_gen, manager_device_list, find_device
from email_api import email_with_attachment


MANAGER_URL = os.environ["MANAGER_URL"]
MANAGER_LOGIN = os.environ["MANAGER_LOGIN"]
MANAGER_PASS = os.environ["MANAGER_PASS"]
SMTP_SERVER = os.environ["SMTP_SERVER"]
EMAIL_SENDER = os.environ["EMAIL_SENDER"]
EMAIL_SENDER_PASSWORD = os.environ["EMAIL_SENDER_PASSWORD"]
EMAIL_RECEIVER = os.environ["EMAIL_RECEIVER"]
# EMAIL_CC_RECEIVER = ""
# site_id = ""
site_id = sys.argv[1]
attachment_name = "ciscosdwan.cfg"
email_subject = f"Bootstrap config for {site_id}"
email_body = f"""\
Subject: Bootstrap config for {site_id}.

Do not respond to this email.
Please make sure that attached file name is: ciscosdwan.cfg.
If so, please copy the file to a USB drive and plug it into the router.
"""


def main() -> None:
    # manager_connectivity_test(manager_url)
    session_id = manager_jsession_id(MANAGER_URL, MANAGER_LOGIN, MANAGER_PASS)
    token = manager_token(MANAGER_URL, session_id)
    device_list = manager_device_list(MANAGER_URL, session_id, token)
    device_uuid = find_device(device_list, site_id)
    attachment_bootstrap_cfg = manager_bootstrap_gen(MANAGER_URL, session_id, token, device_uuid)
    email_with_attachment(SMTP_SERVER, EMAIL_SENDER, EMAIL_SENDER_PASSWORD, 
                          email_subject, email_body, attachment_name, attachment_bootstrap_cfg, 
                          EMAIL_RECEIVER)
    manager_logout(MANAGER_URL, session_id)


if __name__ == "__main__":
    main()