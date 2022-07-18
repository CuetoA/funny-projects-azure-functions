import logging
import json
import azure.functions as func
from . import myTest as mt


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.params.get('data')
    if not data:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            data = req_body.get('data')


    if data:
        try:
            message = mt.sendingWhatsapp(data)
        except:
            message = f"Hello, {data} there again"

        return func.HttpResponse(message)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
