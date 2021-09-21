from woocommerce import API
from dotenv import load_dotenv


load_dotenv()

# Define function for consumer key & consumer secret.
# Define function for for Api call.

def woo_get(url: str, endpoint: str):
    ck = (${consumer_key})
    cs = (${consumer_secret})
    wcapi = API(
        url=f"{url}",
        consumer_key=f"{ck}",
        consumer_secret=f"{cs}",
        version="wc/v3"
    )

    print(wcapi.get(f"{endpoint}", params={"per_page": 20}).json())
