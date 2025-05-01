"""
Path: run.py
"""

from urllib.parse import urlparse
import os
from flask import Flask, request, abort
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
validator = RequestValidator(os.getenv("TWILIO_AUTH_TOKEN"))

def twilio_url():
    " Construct the Twilio URL from the request context."
    p = urlparse(request.url)
    proto = request.headers.get("X-Forwarded-Proto", request.scheme)
    host  = request.headers.get("X-Forwarded-Host", request.host)
    return f"{proto}://{host}{p.path}"

@app.route("/webhook/inbound", methods=["POST"])
def inbound():
    " Handle incoming messages from Twilio."
    signature = request.headers.get("X-Twilio-Signature", "")
    if not validator.validate(twilio_url(), request.form, signature):
        abort(403)

    body = request.form.get("Body", "").strip().lower()
    resp = MessagingResponse()
    resp.message("¡Hola, cooperativa! 👋" if "hola" in body else
                 "No entendí, enviá 'hola' para empezar.")
    return str(resp)

@app.route("/webhook/status", methods=["POST"])
def status():
    " Handle status callbacks from Twilio."
    print(f"[STATUS] {request.form.get('MessageSid')}: {request.form.get('MessageStatus')}")
    return ("", 204)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
