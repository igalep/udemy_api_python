from api_udemy_course.src.utilities.genericUtilities import generate_random_email_and_password
from api_udemy_course.src.utilities.requestesUtility import RequestUtility

class CustomerHelper:
    def __init__(self):
        self.requests = RequestUtility()


    def create_customer(self, email=None, password=None, **kwargs):
        endpoint = 'customers'
        if not email:
            email_password = generate_random_email_and_password()
            email = email_password['email']
        if not password:
            password = 'Password123'

        payload = {'email': email, 'password': password}
        payload.update(kwargs)

        # created_user_json = self.requests.post(endpoint=endpoint, payload=payload, expected_status_code=201)

        wc_user_response = self.requests.woocommerce_post(endpoint='customers', payload=payload)

        return wc_user_response

    def get_all_customers(self):
        endpoint = 'customers'
        response = self.requests.woocommerce_get(endpoint=endpoint)

        return response
