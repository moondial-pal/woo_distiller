import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from woocommerce import API

# Import both mock files from mock_data/
from mock_data.mock_order import order as single_mock_order
from mock_data.mock_orders import orders as multiple_mock_orders

# Load .env config
load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
WC_URL = os.getenv("WC_URL", "https://www.pybit.es")

# Flask app instance
app = Flask(__name__)

# WooCommerce API client
def get_wcapi():
    return API(
        url=WC_URL,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        version="wc/v3",
        timeout=50
    )

# --- ROUTES ---

# 1. Homepage — uses your existing index.html and shows products
@app.route("/")
def index():
    try:
        if not CONSUMER_KEY or not CONSUMER_SECRET:
            print("⚠️ No API credentials found. Returning empty mock response.")
            response = []
        else:
            wcapi = get_wcapi()
            res = wcapi.get("products", params={"per_page": 20})
            if res.status_code != 200:
                print(f"❌ API error: {res.status_code}")
                response = {"error": "Failed to fetch products"}
            else:
                response = res.json()
        return render_template("index.html", response=response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2. Multiple orders — mock or live WooCommerce orders
@app.route("/orders")
def show_orders():
    try:
        if not CONSUMER_KEY or not CONSUMER_SECRET:
            print("⚠️ Using mock_orders from mock_orders.py")
            orders = multiple_mock_orders
        else:
            wcapi = get_wcapi()
            res = wcapi.get("orders", params={"per_page": 5})
            if res.status_code != 200:
                print(f"❌ API error: {res.status_code}")
                orders = multiple_mock_orders
            else:
                orders = res.json()
        return render_template("orders.html", orders=orders)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. Single mock order — always uses mock_order.py
@app.route("/single-order")
def show_single_order():
    try:
        return render_template("orders.html", orders=[single_mock_order])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
