from flask import Flask, request
app = Flask(__name__)
VERIFY_TOKEN = "VILLA_ESPERANZA_2026_SECURE"

@app.route('/')
def home():
    return "Villa Esperanza Bot Vivo", 200

@app.route('/webhook', methods=['GET'])
def verify():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode == 'subscribe' and token == VERIFY_TOKEN:
        return challenge, 200
    return "Error", 403

@app.route('/webhook', methods=['POST'])
def incoming():
    data = request.get_json()
    print(data)
    return "ok", 200
