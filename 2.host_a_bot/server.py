from flask import Flask, request
import toml
from pyprojroot import here
import os
import requests


app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
# ingest secret variables
config_vars = toml.load(os.path.join(here(), ".ignore_me", "secrets.toml"))


verify_token = config_vars["fb_messenger"]["VERIFY_TOKEN"]
page_access_token = config_vars["fb_messenger"]["PAGE_ACCESS_TOKEN"]


def get_bot_response(message):
    """This is just a dummy function, returning a variation of what
    the user said. Replace this function with one connected to chatbot."""
    return "This is a dummy response to '{}'".format(message)


def verify_webhook(req):
    if req.args.get("hub.verify_token") == verify_token:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"

def respond(sender, message):
    """Formulate a response to the user and
    pass it on to a function that sends it."""
    response = get_bot_response(message)
    send_message(sender, response)


def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))


@app.route("/webhook")
def listen(req=request):
    """This is the main function flask uses to
    listen at the `/` endpoint"""
    if req.method == 'GET':
        return verify_webhook(req=req)

    if req.method == 'POST':
        payload = req.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text)

        return "ok"


def send_message(recipient_id, text):
    """Send a response to Facebook"""
    payload = {
        'message': {
            'text': text
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': page_access_token
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json=payload
    )

    return response.json()
