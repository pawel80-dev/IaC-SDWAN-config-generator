import azure.functions as func
import logging

# Set up logging on info level
logging.basicConfig(level=logging.INFO)

app = func.FunctionApp()


@app.function_name(name="HttpTrigger-basic")
@app.route(route="req")
def main(req: func.HttpRequest) -> str:
    logging.info("AZ-FUNC HttpTrigger-basic started.")
    user = req.params.get("user")
    return f"Hello, {user}!"
