import logging
import os
import azure.functions as func
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
from manager_api import manager_jsession_id, manager_token, manager_logout,\
                        manager_bootstrap_gen, manager_device_list, find_device
from email_api import email_with_attachment

# Set up logging on info level
logging.basicConfig(level=logging.INFO)

app = func.FunctionApp()


# route parameter is changed: api/{functionname} to api/get
# https://functionAppName.azurewebsites.net/api/get?user=YourName
@app.function_name(name="HttpTrigger-basic")
@app.route(route="get", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logging.info("AZ-FUNC HttpTrigger-basic started.")
    user = req.params.get("user")
    return f"Hello, {user}!"


# https://functionAppName.azurewebsites.net/api/cfg?site_id=YourSiteID
@app.function_name(name="ConfigGenerator")
@app.route(route="cfg", auth_level=func.AuthLevel.ANONYMOUS)
def conf_gen(req: func.HttpRequest) -> str:
    logging.info("AZ-FUNC ConfigGenerator started.")
    MANAGER_LOGIN = os.environ["MANAGER_LOGIN"]
    MANAGER_PASS = os.environ["MANAGER_PASS"]
    MANAGER_URL = os.environ["MANAGER_URL"]
    SMTP_SERVER = os.environ["SMTP_SERVER"]
    EMAIL_SENDER = os.environ["EMAIL_SENDER"]
    EMAIL_SENDER_PASSWORD = os.environ["EMAIL_SENDER_PASSWORD"]
    EMAIL_RECEIVER = os.environ["EMAIL_RECEIVER"]
    KEY_VAULT_URL = os.environ["KEY_VAULT_URL"]
    MI_CLIENT_ID = os.environ["MI_CLIENT_ID"]
    # credential = ManagedIdentityCredential(client_id=MI_CLIENT_ID)
    # client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)
    # MANAGER_LOGIN = client.get_secret("MANAGER-LOGIN").value
    # MANAGER_PASS = client.get_secret("MANAGER-PASS").value
    site_id = req.params.get("site_id")
    if site_id != "ABC" and site_id != "None":
        attachment_name = "ciscosdwan.cfg"
        email_subject = f"Bootstrap config for {site_id}"
        email_body = f"""\
        Subject: Bootstrap config for {site_id}.

        Do not respond to this email.
        Please make sure that attached file name is: ciscosdwan.cfg.
        If so, please copy the file to a USB drive and plug it into the router.
        """

        session_id = manager_jsession_id(MANAGER_URL, MANAGER_LOGIN, MANAGER_PASS)
        token = manager_token(MANAGER_URL, session_id)
        device_list = manager_device_list(MANAGER_URL, session_id, token)
        device_uuid = find_device(device_list, site_id)
        attachment_bootstrap_cfg = manager_bootstrap_gen(MANAGER_URL, session_id, token, device_uuid)
        email_with_attachment(SMTP_SERVER, EMAIL_SENDER, EMAIL_SENDER_PASSWORD, 
                              email_subject, email_body, attachment_name, attachment_bootstrap_cfg, 
                              EMAIL_RECEIVER)
        manager_logout(MANAGER_URL, session_id)

        return f"Hello, site ID is: {site_id}, config successfuly created!"

    else:
        return f"TEST, site ID is: {site_id}, config was not created!"