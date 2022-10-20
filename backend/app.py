import os, sys
import json
from flask import Flask, request
sys.path.append("..")
from config import Config
from texter import Texter


# Create app var from Flask package
server = Flask(__name__)
# Set path of current app dirname
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

config = Config()
texter = Texter(
    config.twilio_account_sid, 
    config.twilio_auth_token, 
    config.twilio_phone_number
)

print(config.twilio_auth_token)
# Troubleshooting route
@server.route('/')
def home_route():
    response = { "message": "welcome to the coldcall application" }
    res = server.response_class(response=json.dumps(response), status=200, mimetype='application/json')
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res

# Webhook route
@server.route('/reply', methods=['POST'])
def reply_route():
    try:
        message = request.form['Body']
        fro = request.form['From']
        city = request.form['FromCity']
        body = f"""
        From: {fro}
        City: {city}
        Message: {message}
        """
        texter.sendMessage(
            '+13162136004',
            body
        )
        res = server.response_class(response=json.dumps({'message': body}), status=200, mimetype='application/json') 
    except:
        res = server.response_class(response=json.dumps({'text': f'Error sending relayed message'}), status=200, mimetype='application/json')
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res

# Webhook route
@server.route('/voice', methods=['POST'])
def voice_route():
    try:
        fro = request.form['From']
        city = request.form['CallerCity']
        body = f"""
        Wholesale call!! 
        From: {fro}
        City: {city}
        """
        texter.sendMessage(
            '+13162136004',
            body
        )
        res = server.response_class(response=json.dumps({'message': body}), status=200, mimetype='application/json') 
    except:
        res = server.response_class(response=json.dumps({'text': f'Error sending relayed message'}), status=200, mimetype='application/json')
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res
    