## An AI-assisted transaction risk monitoring prototype designed for Raspberry Pi. The system analyzes transaction amount, transaction timing, customer historical average, and transaction frequency to generate an explainable risk score and recommended action.

## Track
AI Risk Manager

## What it does
PayGuard AI is a lightweight, explainable transaction-risk monitoring prototype designed to run on a Raspberry Pi. It analyzes transaction amount, transaction time, customer historical average and daily transaction frequency to generate a risk score, risk level and explanation.

## Features
- Raspberry Pi compatible Flask application
- Explainable risk scoring
- HIGH / MEDIUM / LOW risk levels
- Recommended action for the merchant
- Simple responsive dashboard
- Runs locally without a cloud dependency

## Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open:

`http://localhost:5000`

From another device on the same network, use:

`http://<RASPBERRY_PI_IP>:5000`

## Demo scenario

Use:
- Amount: 48500
- Hour: 2
- Previous average: 1500
- Transactions today: 8

Expected result: HIGH risk with explanations for amount anomaly, unusual time and high transaction frequency.

## Architecture

Browser → Flask API → Risk Engine → Explainable Risk Result

## Note
This is a prototype risk engine for a buildathon demonstration. It is not a production fraud-detection or financial-decision system.
