from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def risk_engine(amount, hour, previous_avg, transactions_today):
    reasons = []
    score = 10

    # Amount anomaly
    if previous_avg > 0:
        ratio = amount / previous_avg
        if ratio >= 8:
            score += 45
            reasons.append("Transaction amount is much higher than the customer's normal average.")
        elif ratio >= 4:
            score += 30
            reasons.append("Transaction amount is significantly above the customer's normal average.")
        elif ratio >= 2:
            score += 15
            reasons.append("Transaction amount is above the customer's normal average.")

    # Unusual time
    if hour >= 0 and hour <= 5:
        score += 20
        reasons.append("Transaction occurred during an unusual late-night/early-morning period.")

    # Frequency
    if transactions_today >= 10:
        score += 20
        reasons.append("High number of transactions detected for the customer today.")
    elif transactions_today >= 6:
        score += 10
        reasons.append("Transaction frequency is higher than usual.")

    score = min(score, 100)

    if score >= 70:
        level = "HIGH"
        action = "Require additional verification before processing."
    elif score >= 40:
        level = "MEDIUM"
        action = "Review the transaction and customer activity."
    else:
        level = "LOW"
        action = "Allow transaction and continue monitoring."

    if not reasons:
        reasons.append("No major anomaly indicators detected.")

    return score, level, action, reasons

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True)
    amount = float(data.get("amount", 0))
    hour = int(data.get("hour", 12))
    previous_avg = float(data.get("previous_avg", 1000))
    transactions_today = int(data.get("transactions_today", 1))

    score, level, action, reasons = risk_engine(
        amount, hour, previous_avg, transactions_today
    )

    return jsonify({
        "score": score,
        "level": level,
        "action": action,
        "reasons": reasons
    })

if __name__ == "__main__":
    # 0.0.0.0 allows the Raspberry Pi dashboard to be opened from another device
    app.run(host="0.0.0.0", port=5000, debug=False)
