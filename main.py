from flask import Flask, request
from kucoin.client import Client

# Claves API de KuCoin (¡NO compartas esto con nadie!)
API_KEY = "68180bed61d419000171fae6"
API_SECRET = "b18ed605-c693-4b32-ab9c-cd49413e0cbf"
API_PASSPHRASE = "1085041052Yoimer"

client = Client(API_KEY, API_SECRET, API_PASSPHRASE)

# === APP FLASK PARA RECIBIR ALERTAS ===
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Alerta recibida:", data)

    if data['evento'] == "compra" and data['par'] == "BTC-USDT":
        try:
            # Ajusta el tamaño según tu capital disponible
            cantidad = 0.0001  # por ejemplo: 0.0001 BTC

            orden = client.create_market_order(
                symbol='BTC-USDT',
                side='buy',
                size=cantidad
            )

            print("✅ Orden ejecutada:", orden)
            return {"mensaje": "Compra ejecutada correctamente"}

        except Exception as e:
            print("❌ Error al ejecutar la orden:", e)
            return {"error": str(e)}

    return {"mensaje": "Par o evento no reconocido"}
