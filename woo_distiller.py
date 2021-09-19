from woocommerce import API


# Define function for consumer key & consumer secret.
# Define function for for Api call.


def woo_get(url: str, endpoint: str):
    ck = input("Enter consumer_key: ")
    cs = input("Enter consumer_secret: ")
    wcapi = API(
        url=f"{url}",
        consumer_key=f"{ck}",
        consumer_secret=f"{cs}",
        version="wc/v3"
    )

    print(wcapi.get(f"{endpoint}", params={"per_page": 20}).json())
