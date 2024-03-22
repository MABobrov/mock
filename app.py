
import uuid
import random
import logging
from flask import Flask, request, jsonify
import functools
from datetime import datetime

def log_request_response(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        request_data = request.json
        logging.info("Request time: %s", datetime.now())
        logging.info("Request endpoint: %s", request.url)
        logging.info("Request method: %s", request.method)
        logging.info("Request json:\n%s", request_data)

        response = fn(*args, **kwargs)
        response_data = response.get_json()

        logging.info("Response time: %s", datetime.now())
        logging.info("Response status code: %s", response.status_code)
        logging.info("Response json:\n%s", response_data)

        return response

    return wrapper
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("flask").setLevel(logging.DEBUG)

def generate_unique_token() -> str:
    return str(uuid.uuid4())

def generate_unique_kd_number() -> str:
    return "".join(random.choices("0123456789", k=10))
    
@app.route("/Services/WidgetTest/api/Widget/CreateApplication", methods=["POST"])
@log_request_response
def create_app():
    
    online_token = generate_unique_token()

    response = {
        "client": None,
        "onlineToken": online_token,
        "step": 0,
        "waitingStep": 1,
        "changeButton": None,
        "isNeedJuicySessionId": False,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }

    return jsonify(response)

@app.route("/Services/WidgetTest/api/Widget/SendFullApplication", methods=["POST"])
@log_request_response
def send_full():
    online_token = request.json["onlineToken"]

    response = {
        "client": None,
        "onlineToken": online_token,
        "step": 4,
        "waitingStep": 5,
        "changeButton": None,
        "isNeedJuicySessionId": False,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }
    return jsonify(response)
    

tokens_visited = {}
@app.route("/Services/WidgetTest/api/Widget/ApplicationBankInfo", methods=["POST"])
@log_request_response
def application_bank_info():
    data = request.json
    online_token = data["onlineToken"]

    if online_token not in tokens_visited:
        tokens_visited[online_token] = 0

    tokens_visited[online_token] += 1

    basic_response = {
        "onlineToken": online_token,
        "step": 4,
        "waitingStep": 5,
        "banksInfo": [
            {
                "bankId": 54,
                "status": 2 if tokens_visited[online_token] > 3 else 8,
                "statusDescription": "",
                "decisions": [
                    {
                        "decisionId": 0,
                        "offerId": 0,
                        "numberKD": "1335300708",
                        "productCode": "TEST",
                        "productName": "Денум Тест",
                        "sumCredit": 15000.0000,
                        "sumGoods": 15000.0000,
                        "term": 4,
                        "initPay": 0.0000,
                        "monthlyPayment": 4078.0000,
                        "selected": True,
                        "smsSigning": True,
                        "deliveryType": 0,
                        "amountSMSinform": 0.00,
                        "balanceCreditLine": 0.0000,
                        "isCreditLine": False
                    }
                ],
                "needScans": tokens_visited[online_token] == 1,
                "isSelectedApproval": False,
                "isBlocked": False,
                "isFakeDecision": False
            }
        ],
        "additionalInfo": True,
        "haveProblemWithProcessApp": False,
        "messageProblemWithProcessApp": None,
        "stepProblemWithProcessApp": None,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }

    return jsonify(basic_response)
    
@app.route("/Services/WidgetTest/api/Widget/CheckScans", methods=["POST"])
@log_request_response
def check_scans():

    online_token = request.json["onlineToken"]

    response = {
            "scans": [
                {
                    "sendStatus": 0,
                    "allowedExtensions": "jpeg;jpg;gif;png",
                    "maxFileSize": 1048576,
                    "isRequired": True,
                    "base64Data": None,
                    "documentType": 22,
                    "documentName": "Фотография",
                    "pageNumber": 1
                },
                {
                    "sendStatus": 0,
                    "allowedExtensions": "jpeg;jpg;gif;png",
                    "maxFileSize": 1048576,
                    "isRequired": True,
                    "base64Data": None,
                    "documentType": 44,
                    "documentName": "Паспорт 2-3",
                    "pageNumber": 1
                },
                {
                    "sendStatus": 0,
                    "allowedExtensions": "jpeg;jpg;gif;png",
                    "maxFileSize": 1048576,
                    "isRequired": True,
                    "base64Data": None,
                    "documentType": 45,
                    "documentName": "Паспорт регистрация",
                    "pageNumber": 1
                }
            ],
            "onlineToken": online_token,
            "step": 4,
            "waitingStep": 5,
            "changeButton": None,
            "isNeedJuicySessionId": False,
            "isSuccess": True,
            "error": None,
            "errorCode": None
        }
    return jsonify(response)


@app.route("/Services/WidgetTest/api/Widget/SaveScan", methods=["POST"])
@log_request_response
def save_scan():

    online_token = request.json["onlineToken"]

    response = {
        "onlineToken": online_token,
        "step": 4,
        "waitingStep": 5,
        "changeButton": None,
        "isNeedJuicySessionId": False,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }
    return jsonify(response)

@app.route("/Services/WidgetTest/api/Widget/SendScans", methods=["POST"])
@log_request_response
def send_scans():

    online_token = request.json["onlineToken"]

    response = {
        "onlineToken": online_token,
        "step": 4,
        "waitingStep": 5,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }
    return jsonify(response)




@app.route("/Services/WidgetTest/api/Widget/RepeatSendSmsCode", methods=["POST"])
@log_request_response
def repeat_send_sms_code():
    online_token = request.json["onlineToken"]
    
    data = {
        "countAccessSendSmsCode": 0,
        "onlineToken": online_token,
        "step": 5,
        "waitingStep": None,
        "changeButton": None,
        "isNeedJuicySessionId": False,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }
    return jsonify(data)

@app.route("/Services/WidgetTest/api/Widget/SetApplicationApproval", methods=["POST"])
@log_request_response
def set_application_approval():

    online_token = request.json["onlineToken"]
    data = {
        "documentLink": "https://testonline.fconnect.ru/Services/WidgetTest/api/WidgetDocument/GetBankDocumentsPackage?onlineToken="+online_token,
        "applicationClosingType": 2,
        "bankLink": None,
        "closeLink": None,
        "onlineToken": online_token,
        "step": 5,
        "waitingStep": None,
        "changeButton": None,
        "isNeedJuicySessionId": False,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }
    return jsonify(data)

@app.route("/Services/WidgetTest/api/Widget/SaveSmsCode", methods=["POST"])
@log_request_response
def save_sms_code():

    online_token = request.json["onlineToken"]

    data = {
        "isSaveSmsCodeSuccess": True,
        "countAccessSendSmsCode": 2,
        "countAccessCheckSmsCode": 2,
        "onlineToken": online_token,
        "step": 5,
        "waitingStep": None,
        "changeButton": None,
        "isNeedJuicySessionId": False,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }
    return jsonify(data)

@app.route("/Services/WidgetTest/api/Widget/CheckSmsCode", methods=["POST"])
@log_request_response
def check_sms_code():

    online_token = request.json["onlineToken"]
    
    data = {
        "statusSmsCode": 1,
        "onlineToken": online_token,
        "step": 6,
        "waitingStep": None,
        "changeButton": None,
        "isNeedJuicySessionId": False,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }
    return jsonify(data)


@app.route("/Services/WidgetTest/api/Widget/Cancellation", methods=["POST"])
@log_request_response
def cancellation_opty():

    online_token = request.json["onlineToken"]
    response = {
        "onlineToken": online_token,
        "step": 6,
        "waitingStep": None,
        "changeButton": None,
        "isNeedJuicySessionId": False,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }
   
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
