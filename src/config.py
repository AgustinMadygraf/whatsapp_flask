"""
Path: src/config.py
"""

import os

class Config:
    " Configuración de la aplicación Flask y WhatsApp Business API "
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

    # WhatsApp Business Cloud API
    WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN", "default_token")
    WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID", "default_phone_id")
    WABA_ID = os.getenv("WABA_ID", "default_waba_id")

    # Token para verificar webhooks
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "default_verify_token")
