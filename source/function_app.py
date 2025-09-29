import azure.functions as func
import logging
import os

# Set up logging on info level
logging.basicConfig(level=logging.INFO)

MANAGER_URL = os.environ["MANAGER_URL"]
MANAGER_LOGIN = os.environ["MANAGER_LOGIN"]
MANAGER_PASS = os.environ["MANAGER_PASS"]
SMTP_SERVER = os.environ["SMTP_SERVER"]
EMAIL_SENDER = os.environ["EMAIL_SENDER"]
EMAIL_SENDER_PASSWORD = os.environ["EMAIL_SENDER_PASSWORD"]
EMAIL_RECEIVER = os.environ["EMAIL_RECEIVER"]

app = func.FunctionApp()


# route parameter is changed: api/{functionname} to api/req
# https://functionAppName.azurewebsites.net/api/req?user=YourName
@app.function_name(name="HttpTrigger-basic")
@app.route(route="req", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logging.info("AZ-FUNC HttpTrigger-basic started.")
    user = req.params.get("user")
    return f"Hello, {user}!"


@app.function_name(name="ConfigGenerator")
@app.route(route="req", auth_level=func.AuthLevel.ANONYMOUS)
def conf_gen(req: func.HttpRequest) -> str:
    logging.info("AZ-FUNC ConfigGenerator started.")
    site_id = req.params.get("site_id")
    attachment_name = "ciscosdwan.cfg"
    email_subject = f"Bootstrap config for {site_id}"
    email_body = f"""\
    Subject: Bootstrap config for {site_id}.

    Do not respond to this email.
    Please make sure that attached file name is: ciscosdwan.cfg.
    If so, please copy the file to a USB drive and plug it into the router.
    """

    return f"Hello, site ID is: {site_id}!"