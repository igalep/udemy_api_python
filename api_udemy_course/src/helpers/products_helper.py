from api_udemy_course.src.utilities.requestesUtility import RequestUtility

class ProductHelper:
    def __init__(self):
        self.requests = RequestUtility()


    def get_products(self, **kwargs):
        endpoint = 'products'

        args = {
            'per_page': 50
        }

        args.update(kwargs)

        response = self.requests.woocommerce_get(endpoint=endpoint, **args)
        # logging.info(f'Get all products response: {response}')
        return response

    def get_product_by_id(self, product_id):
        endpoint = f'products/{product_id}'

        response = self.requests.woocommerce_get(endpoint=endpoint)
        # logging.info(f'Get product {product_id} response: {response}')
        return response

    def create_product(self, payload):
        endpoint = 'products'

        response = self.requests.woocommerce_post(endpoint=endpoint, payload=payload)
        # logging.info(f'Newly created product response: {response}')
        return response

    def update_product(self, **kwargs):
        endpoint = f'products/{kwargs['id']}'
        payload_to_update = kwargs['payload']


        res_ans = self.requests.woocommerce_put(endpoint=endpoint, payload=payload_to_update)
        return res_ans
