from faker import Faker
from api_udemy_course.src.utilities.requestesUtility import RequestUtility
from api_udemy_course.src.utilities.genericUtilities import read_json_file as file_reader


class OrdersHelper:
    def __init__(self):
        self.requests = RequestUtility()
        self.fake = Faker()


    def create_order(self, **kwargs):
        endpoint = 'orders'


        payload = file_reader('order_payload.json')
        payload['billing']['first_name'] = self.fake.first_name()
        payload['billing']['last_name'] = self.fake.last_name()
        payload['billing']['city'] = self.fake.city()
        payload['billing']['email'] = self.fake.email()

        payload.update(kwargs)

        res_ans = self.requests.woocommerce_post(endpoint=endpoint, payload=payload)
        return res_ans

    def update_order_status(self, **kwargs):
        endpoint = f'orders/{kwargs['id']}'

        payload = {
            'status' : kwargs['status']
        }

        res_ans = self.requests.woocommerce_put(endpoint=endpoint, payload=payload)

        return res_ans

    def retrieve_order_by_id(self, order_id):
        endpoint = f'orders/{order_id}'

        res_ans = self.requests.woocommerce_get(endpoint=endpoint)

        return res_ans
