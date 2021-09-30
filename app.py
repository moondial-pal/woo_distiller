import os

from dotenv import load_dotenv
from flask import Flask, render_template
from woocommerce import API

from mock_data.mock_order import order

# initialize Flask application
app = Flask(__name__)

# load environment variables
load_dotenv()
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")


# Generalized get function to make requests to woocommerce API
def woo_get(url: str, endpoint: str):
    wcapi = API(
        url=f"{url}",
        consumer_key=CONSUMER_SECRET,
        consumer_secret=CONSUMER_KEY,
        version="wc/v3",
    )
    return wcapi.json()


# Index route for Flask
# This shows an example of how we can use some of our mock data to start
# showing data on the page.
@app.route("/")
def index():
    order_data = order
    return render_template("index.html", order=order_data)
