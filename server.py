from flask import Flask, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAAPOM5FJjzABALnc3PZBf6CVQgkPvWGuVY8hMaqHZCdmeQc3WRhUwa9uaCGpEBdhSXCd6QHR08ahHICNNMSduy2ZCKgPMAuh8zetXvb0ZCjHERgenWPYQeRlFZAQPVZAeETQrFxMPHhCEsoZCj8HvzoCgUJkGK8qr4ZD"


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']


@app.route('/', methods=['POST', 'GET'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
