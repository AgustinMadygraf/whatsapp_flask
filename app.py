"""
Path: app.py
"""

from flask import Flask, request, jsonify, render_template
from src.whatsapp import send_whatsapp_message
from src.config import Config

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    " Página principal con el formulario para enviar mensajes "
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    " Maneja el envío de mensajes desde el formulario "
    phone = request.form.get("phone")
    if phone:
        response = send_whatsapp_message(phone, "hello_world")
        return jsonify(response), 200
    return "Número de teléfono no proporcionado", 400

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    " Webhook para recibir mensajes de WhatsApp y enviar respuestas automáticas"
    if request.method == "GET":
        # Verificación de token (challenge)
        if request.args.get("hub.verify_token") == Config.VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        return "Token inválido", 403

    data = request.json
    # Ejemplo: cuando llega un mensaje de texto
    try:
        entry = data["entry"][0]
        change = entry["changes"][0]["value"]
        messages = change.get("messages")
        if messages:
            sender = messages[0]["from"]
            # Envío de respuesta automática
            send_whatsapp_message(sender, "hello_world")
    except (KeyError, IndexError) as e:
        print("Error procesando webhook:", e)
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
