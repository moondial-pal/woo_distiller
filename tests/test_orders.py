import requests
import requests_mock

from woocommerce import API

from mock_data.mock_order import order
from app import woo_get

BASE_URL = "https://www.anything.com"

def test_list_orders():
    with requests_mock.Mocker() as m:
        mock_url = f"{BASE_URL}/wp-json/wc/v3/orders?per_page=20"
        m.get(mock_url, json=order)
        actual = woo_get(BASE_URL, "orders")
        assert actual == order
    # requests.get.assert_called_once_with("orders")


def test_order_id():
    assert order[0]["id"] == 727
