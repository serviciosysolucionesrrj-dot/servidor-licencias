from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Aquí agregas las licencias permitidas
LICENCIAS = {
    "48d61a14105b4d4d5299e182afcd772aeff18a8245e6faeeb54e452f6f7f0c56": {
        "expira": "2026-12-31",
        "activa": True
    }
}

@app.route("/validar", methods=["POST"])
def validar():

    data = request.json
    hardware_id = data.get("hardware_id")

    if hardware_id in LICENCIAS:

        licencia = LICENCIAS[hardware_id]

        if not licencia["activa"]:
            return jsonify({"valida": False})

        hoy = datetime.now().date()
        expira = datetime.strptime(licencia["expira"], "%Y-%m-%d").date()

        if hoy <= expira:
            return jsonify({"valida": True})
        else:
            return jsonify({"valida": False})

    return jsonify({"valida": False})

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


