import requests
from flask import Flask, jsonify

app = Flask(__name__)
API = "7a4389fffc281ad23e73f8a5"


@app.route("/", methods=['GET'])
def home():
    return "<h1>Welcome to the quick currency conversion.</h1>"


@app.route("/convert/<currency_from>/<currency_to>/<amount>")
def convert(currency_from, currency_to, amount):
    try:
        response = requests.get(f"https://v6.exchangerate-api.com/v6/{API}/latest/USD")
        data = response.json()
        if 200 > response.status_code or response.status_code > 299:
            return jsonify({"error": "currency details not accessible"})
        all_currencies = data["conversion_rates"]
        if currency_to not in all_currencies or currency_from not in all_currencies:
            return jsonify({"error": "currency details either incorrect or inaccessible"})
        price_in_usd = data["conversion_rates"][currency_from]
    except:
        return "<h1>invalid currency input</h1>"
    else:
        new_amount = (int(amount)/int(price_in_usd))*(int(all_currencies[currency_to]))
        return jsonify({"from": currency_from,
                        "to": currency_to,
                        "amount": amount,
                        "calculated_amount": new_amount})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    