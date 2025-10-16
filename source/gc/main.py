import functions_framework
# import sys
# sys.path.append("../source")  # setting path to source folder
from ipify import get_public_ip

ipify_url = "https://api.ipify.org"


# HTTP handler function
@functions_framework.http
def hello_world(request):
    path = request.path
    if path == '/check':
        return "Check Done!"
    elif path == '/ip':
        public_ip = get_public_ip(ipify_url)
        return f"Your public IP is {public_ip}."
    else:
        return "Hello World!"

