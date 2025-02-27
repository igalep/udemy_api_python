import pytest
from api_udemy_course.src.helpers.coupon_helper import CouponHelper
from api_udemy_course.src.helpers.products_helper import ProductHelper



def test_create_new_coupon_and_order(tests_setup_order_id, delete_coupon):
    coupon_helper = CouponHelper()
    product_helper = ProductHelper()

    coupon_data = {
        'code' : '50off',
        'amount' : '50',
        'minimum_amount' : '1'
    }

    created_coupon = coupon_helper.create_new_coupon(**coupon_data)
    delete_coupon.append(created_coupon['id'])

    random_product_id = tests_setup_order_id.id

    partial_order_payload = {
        "line_items": [
            {
                "product_id": random_product_id,
                "quantity": 1
            }
        ],
        "shipping_lines": [
            {
                "method_id": "flat_rate",
                "method_title": "Flat Rate",
                "total": "10.00"
            }
        ],
        "coupon_lines" : [{
         "code" : created_coupon['code']
        }]
    }

    product = product_helper.get_product_by_id(product_id=random_product_id)
    product_original_price = product['price']

    created_order = tests_setup_order_id.order_helper.create_order(**partial_order_payload)

    if product['on_sale'] is False:
        assert float(created_order['discount_total']) == float(product_original_price) * (float(created_coupon['amount']) / 100)
    else:
        assert created_order['data']['status'] == 400

@pytest.mark.negative
def test_wrong_coupon_type():
    coupon_helper = CouponHelper()

    coupon_data = {
        'code' : '50off',
        'amount' : '50',
        "discount_type": "invalid_coupon_type_!@#@!",
        'minimum_amount' : '1'
    }

    created_coupon = coupon_helper.create_new_coupon(**coupon_data)

    assert created_coupon['data']['status'] == 400





