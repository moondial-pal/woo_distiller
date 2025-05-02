import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from woocommerce import API
from mock_data.mock_order import order as mock_orders

# Load environment variables
load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
WC_URL = os.getenv("WC_URL", "https://www.pybit.es")

# Initialize Flask app
app = Flask(__name__)

def get_orders():
    if not CONSUMER_KEY or not CONSUMER_SECRET:
        print("⚠️ No API credentials found. Using mock data.")
        return mock_orders

    wcapi = API(
        url=WC_URL,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        version="wc/v3",
        timeout=50
    )

    response = wcapi.get("orders", params={"per_page": 5})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ API Error {response.status_code}: {response.text}")
        return mock_orders

@app.route("/")
def index():
    try:
        orders = get_orders()
        return render_template("orders.html", orders=orders)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
