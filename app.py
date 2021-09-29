import os
from woocommerce import API
from dotenv import load_dotenv

from tests.data.mock_order import order

from flask import Flask, render_template
app = Flask(__name__)

load_dotenv()
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

STORES = ["store1", "store2"]
# Define function for consumer key & consumer secret.
# Define function for for Api call.


def woo_get(url: str, endpoint: str):
    wcapi = API(
        url=f"{url}",
        consumer_key=CONSUMER_SECRET,
        consumer_secret=CONSUMER_KEY,
        version="wc/v3"
    )
    return wcapi.json()


@app.route("/")
def index():
    order_data = order
    return render_template("index.html", order=order_data)
