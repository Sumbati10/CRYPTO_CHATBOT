from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message'].lower()

    # Basic logic
    if "sustainable" in user_input:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        response = f"{best} is the most eco-friendly choice! 🌱 Sustainability score: {crypto_db[best]['sustainability_score']}/10"
    elif "trending" in user_input or "growth" in user_input:
        trending = [k for k, v in crypto_db.items() if v["price_trend"] == "rising"]
        response = f"{', '.join(trending)} are on the rise! 🚀 Great for long-term growth."
    elif "profit" in user_input:
        profitable = [k for k, v in crypto_db.items() if v["price_trend"] == "rising" and v["market_cap"] == "high"]
        response = f"High potential: {', '.join(profitable)} 📈"
    else:
        response = "Try asking me about sustainable, trending, or profitable cryptos!"

    disclaimer = "⚠️ Crypto is risky—always do your own research!"
    return jsonify(response=f"{response}\n\n{disclaimer}")

if __name__ == '__main__':
    app.run(debug=True)
