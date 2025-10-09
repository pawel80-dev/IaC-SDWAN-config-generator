import functions_framework
from ipify import get_public_ip

ipify_url = "https://api.ipify.org"


# HTTP handler function
@functions_framework.http
def hello_get(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page.
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """
    if request.args.get == 'ip':
        public_ip = get_public_ip(ipify_url)
        return f"Your public IP is {public_ip}."
    else:
        return "Hello World!"
