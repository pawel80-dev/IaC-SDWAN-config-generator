import functions_framework
# import sys
# sys.path.append("../source")  # setting path to source folder
from ipify import get_public_ip

ipify_url = "https://api.ipify.org"


# HTTP handler function (Flask based)
# https://tedboy.github.io/flask/generated/generated/flask.Request.html
@functions_framework.http
def basic_http(request):
    path = request.path
    user = request.args.get("user")
    site_id = request.args.get("site_id")

    if path == "/ipcheck":
        public_ip = get_public_ip(ipify_url)
        return f"Your public IP is {public_ip}."
    
    if path == "/get" and user:
        return f"Hello, {user}!"

    if path == "/cfg" and (site_id == "ABC" or site_id == "None"):
        return f"TEST, site ID is: {site_id}, config was not created!"
    
    else:
        return "Hello World!"
