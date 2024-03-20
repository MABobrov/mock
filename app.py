import uuid
import random
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

def generate_unique_token() -> str:
    return str(uuid.uuid4())

def generate_unique_kd_number() -> str:
    return "".join(random.choices("0123456789", k=10))

@app.route("/Services/WidgetTest/api/Widget/Cancellation", methods=["POST"])
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
    logging.debug("\n\n %s \n\n", request.json)
    return jsonify(response)
    
    
@app.route("/Services/WidgetTest/api/Widget/ApplicationBankInfo", methods=["POST"])
def application_bank_info():

    online_token = request.json["onlineToken"]

    response = {
        "onlineToken": online_token,
        "step": 4,
        "waitingStep": 5,
        "banksInfo": [
            {
                "bankId": 54,
                "status": 8,
                "statusDescription": "",
                "decisions": [
                    {
                        "decisionId": 0,
                        "offerId": 0,
                        "numberKD": generate_unique_kd_number(),
                        "productCode": "TEST",
                        "productName": "Денум Тест",
                        "sumCredit": 15000.00,
                        "sumGoods": 15000.00,
                        "term": 4,
                        "initPay": 0.00,
                        "monthlyPayment": 4078.00,
                        "selected": True,
                        "smsSigning": True,
                        "deliveryType": 0,
                        "amountSMSinform": 0.00,
                        "balanceCreditLine": 0.00,
                        "isCreditLine": False
                    }],
                "needScans": True,
                "isSelectedApproval": False,
                "isBlocked": False,
                "isFakeDecision": False
            }],
        "additionalInfo": True,
        "haveProblemWithProcessApp": False,
        "messageProblemWithProcessApp": None,
        "stepProblemWithProcessApp": None,
        "isSuccess": True,
        "error": None,
        "errorCode": None
    }
    logging.debug("\n\n %s \n\n", request.json)
    return jsonify(response)

@app.route("/Services/WidgetTest/api/Widget/CheckScans", methods=["POST"])
def check_scans():
    logging.info("\n\n %s \n\n", request.json)
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
def save_scan():
    logging.info("\n\n %s \n\n", request.json)
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
def send_scans():
    logging.info("\n\n %s \n\n", request.json)
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

@app.route("/Services/WidgetTest/api/Widget/CreateApplication", methods=["POST"])
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
    logging.info("\n\n %s \n\n", request.json)
    return jsonify(response)

@app.route("/Services/WidgetTest/api/Widget/SendFullApplication", methods=["POST"])
def send_full():
    logging.info("\n\n %s \n\n", request.json)
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

@app.route("/Services/WidgetTest/api/Widget/RepeatSendSmsCode", methods=["POST"])
def repeat_send_sms_code():
    online_token = request.json["onlineToken"]
    logging.info("\n\n %s \n\n", request.json)
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
def set_application_approval():
    online_token = request.json["onlineToken"]
    logging.info("\n\n %s \n\n", request.json)
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
def save_sms_code():
    online_token = request.json["onlineToken"]
    logging.info("\n\n %s \n\n", request.json)
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
def check_sms_code():
    online_token = request.json["onlineToken"]
    logging.info("\n\n %s \n\n", request.json)
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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
