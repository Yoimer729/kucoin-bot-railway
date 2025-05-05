# main.py
from flask import Flask, request, jsonify
from kucoin.client import Trade
import os

app = Flask(__name__)

# Datos de autenticación desde las variables de entorno
API_KEY = os.environ.get("68180bed61d419000171fae6")
API_SECRET = os.environ.get("b18ed605-c693-4b32-ab9c-cd49413e0cbf")
API_PASSPHRASE = os.environ.get("1085041052Yoimer")

client = Trade(key=API_KEY, secret=API_SECRET, passphrase=API_PASSPHRASE)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Alerta recibida:", data)

    if data.get('evento') == 'compra' and data.get('par') == 'BTCUSDT':
        try:
            cantidad = 0.0001
            orden = client.create_market_order(symbol='BTC-USDT', side='buy', size=str(cantidad))
            print("✅ Orden ejecutada:", orden)
            return jsonify({"mensaje": "Compra ejecutada correctamente"})

        except Exception as e:
            print("❌ Error al ejecutar la orden:", str(e))
            return jsonify({"error": str(e)}), 500

    return jsonify({"mensaje": "Condiciones no cumplidas"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
