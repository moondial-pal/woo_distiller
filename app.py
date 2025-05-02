import os

from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from woocommerce import API

# Load environment variables
load_dotenv()

WC_URL = os.getenv("WC_URL", "https://www.pybit.es")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

# Validate required environment variables
if not CONSUMER_KEY or not CONSUMER_SECRET:
    raise RuntimeError("Missing WooCommerce API credentials in environment variables.")

# Initialize Flask application
app = Flask(__name__)

# WooCommerce API GET wrapper
def woo_get(endpoint: str):
    wcapi = API(
        url=WC_URL,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        version="wc/v3",
        timeout=50
    )
    response = wcapi.get(endpoint, params={"per_page": 20})
    if response.status_code != 200:
        raise Exception(f"Failed to fetch '{endpoint}': {response.status_code} - {response.text}")
    return response.json()

# Index route
@app.route("/")
def index():
    try:
        products = woo_get("products")
        return render_template("index.html", response=products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Optional: debug run
# if __name__ == "__main__":
#     app.run(debug=True)
