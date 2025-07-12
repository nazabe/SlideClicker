from flask import Flask, request, jsonify
import pyautogui

app = Flask(__name__)

# Mapa de comandos permitidos a teclas reales
KEY_MAP = {
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right"
}


@app.route('/press', methods=['GET'])
def press_key():
    key = request.args.get('key', '').lower()

    if key in KEY_MAP:
        pyautogui.press(KEY_MAP[key])
        return jsonify({"status": "ok", "message": f"Key '{key}' pressed."}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid key."}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Escucha en toda la red local
