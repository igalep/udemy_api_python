from api_udemy_course.src.utilities.genericUtilities import read_json_file as file_reader
from api_udemy_course.src.utilities.requestesUtility import RequestUtility

class CouponHelper:
    def __init__(self):
        self.request = RequestUtility()

    def create_new_coupon(self,**kwargs):
        endpoint = 'coupons'

        payload = file_reader('coupon_payload.json')

        payload.update(kwargs)

        created_coupon = self.request.woocommerce_post(endpoint=endpoint, payload=payload)

        return created_coupon

    def delete_coupon(self, coupon_id):
        endpoint = f'coupons/{coupon_id}'

        delete_coupon_res = self.request.woocommerce_delete(endpoint= endpoint)

        return delete_coupon_res