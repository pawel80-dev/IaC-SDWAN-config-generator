import functions_framework
# import sys
# sys.path.append("../source")  # setting path to source folder
from ipify import get_public_ip

ipify_url = "https://api.ipify.org"


# HTTP handler function (Flask based)
# https://tedboy.github.io/flask/generated/generated/flask.Request.html
@functions_framework.http
def hello_world(request):
    path = request.path
    user = request.args.get("user")
    if path == "/ipcheck":
        public_ip = get_public_ip(ipify_url)
        return f"Your public IP is {public_ip}."
    if path == "/get" and user:
        return f"Hello, {user}!"
    else:
        return "Hello World!"
