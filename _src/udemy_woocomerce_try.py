from woocommerce import API
import pprint

wcapi = API(
    url="http://localhost:8880/index.php/",
    consumer_key="ck_91f178b81f4d81e447ba3ace38e99532dbfdb28b",
    consumer_secret="cs_6015eba636ff57b15fc9202a7e7f356b10532149",
    version="wc/v3"
)

r = wcapi.get("products")

pprint.pprint(r.json())