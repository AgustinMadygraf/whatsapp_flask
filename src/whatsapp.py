"""
Path: whatsapp.py
"""

import requests
from src.config import Config

ACCESS_TOKEN    = Config.WHATSAPP_TOKEN
PHONE_NUMBER_ID = Config.WHATSAPP_PHONE_ID

def send_whatsapp_message(to, template_name, lang="en_US"):
    " Envío de mensajes de WhatsApp utilizando la API de WhatsApp Business "
    url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type":  "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {"code": lang}
        }
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    if resp.status_code != 200:
        print("Error al enviar mensaje:", resp.status_code, resp.text)
    return resp.json()
