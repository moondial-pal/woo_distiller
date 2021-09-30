import requests
from woocommerce import API


def test_list_orders(mocker):
    url = "https://www.anything.com"
    ck = "test_key"
    cs = "test_secret"
    wcapi = API(
        url=f"{url}",
        consumer_key=f"{ck}",
        consumer_secret=f"{cs}",
        version="wc/v3"
    )
    mocker.patch('requests.get')
    wcapi.get("/orders", params={"per_page": 20}).json()

    requests.get.assert_called_once_with("orders")
