from fastapi import FastAPI
from ipify import get_public_ip
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI!"}


@app.get("/ipcheck")
def ip_check():
    ipify_url = "https://api.ipify.org"
    public_ip = get_public_ip(ipify_url)
    return {"public_ip": public_ip}


@app.get("/user/")
# http://127.0.0.1/user/?name=John
# user_name could be string or None, default value is None
def read_item(name: str | None = None):
    if name:
        return {"message": f"Hello, {name}!"}
    elif name == "":
        return {"message": "Hello, empty user!"}
    elif name is None:
        return {"message": "Hello, None user!"}
    else:
        return {"message": "Hello..."}


@app.get("/cfg/")
# http://127.0.0.1/cfg/?site_id=YourSiteID
# site_id could be string or None, default value is None
def read_item(site_id: str | None = None):
    MANAGER_URL = os.environ["MANAGER_URL"]
    return {"message": f"Manager URL: {MANAGER_URL}"}


# https://functionAppName.azurewebsites.net/api/cfg?site_id=YourSiteID
# @app.function_name(name="ConfigGenerator")
# @app.route(route="cfg", auth_level=func.AuthLevel.ANONYMOUS)
# def conf_gen(req: func.HttpRequest) -> str:
#     logging.info("AZ-FUNC ConfigGenerator started.")
#     MANAGER_LOGIN = os.environ["MANAGER_LOGIN"]
#     MANAGER_PASS = os.environ["MANAGER_PASS"]
#     MANAGER_URL = os.environ["MANAGER_URL"]
#     SMTP_SERVER = os.environ["SMTP_SERVER"]
#     EMAIL_SENDER = os.environ["EMAIL_SENDER"]
#     EMAIL_SENDER_PASSWORD = os.environ["EMAIL_SENDER_PASSWORD"]
#     EMAIL_RECEIVER = os.environ["EMAIL_RECEIVER"]
#     KEY_VAULT_URL = os.environ["KEY_VAULT_URL"]
#     MI_CLIENT_ID = os.environ["MI_CLIENT_ID"]
#     # credential = ManagedIdentityCredential(client_id=MI_CLIENT_ID)
#     # client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)
#     # MANAGER_LOGIN = client.get_secret("MANAGER-LOGIN").value
#     # MANAGER_PASS = client.get_secret("MANAGER-PASS").value
#     site_id = req.params.get("site_id")
#     if site_id != "ABC" and site_id != "None":
#         attachment_name = "ciscosdwan.cfg"
#         email_subject = f"Bootstrap config for {site_id}"
#         email_body = f"""\
#         Subject: Bootstrap config for {site_id}.

#         Do not respond to this email.
#         Please make sure that attached file name is: ciscosdwan.cfg.
#         If so, please copy the file to a USB drive and plug it into the router.
#         """

#         session_id = manager_jsession_id(MANAGER_URL, MANAGER_LOGIN, MANAGER_PASS)
#         token = manager_token(MANAGER_URL, session_id)
#         device_list = manager_device_list(MANAGER_URL, session_id, token)
#         device_uuid = find_device(device_list, site_id)
#         attachment_bootstrap_cfg = manager_bootstrap_gen(MANAGER_URL, session_id, token, device_uuid)
#         email_with_attachment(SMTP_SERVER, EMAIL_SENDER, EMAIL_SENDER_PASSWORD, 
#                               email_subject, email_body, attachment_name, attachment_bootstrap_cfg, 
#                               EMAIL_RECEIVER)
#         manager_logout(MANAGER_URL, session_id)

#         return f"Hello, site ID is: {site_id}, config successfuly created!"

#     else:
#         return f"TEST, site ID is: {site_id}, config was not created!"