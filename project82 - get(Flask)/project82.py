from flask import Flask, request

app = Flask(__name__)


@app.route('/language', methods=["GET"])
def index():
    
    data = request.args.get("lang", "").lower()
    if data == "spanish":
        return "Hola como estas."
    elif data == "english":
        return "Hi how are you?"
    
    return "Hi how are you?"

@app.route('/', methods=["GET"])
def main():
    return "Hi how are you?"

app.run(host='0.0.0.0', port=81)
