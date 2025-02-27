import  pytest
import random
import string
from api_udemy_course.src.helpers.customer_helper import CustomerHelper
from api_udemy_course.src.helpers.orders_helper import OrdersHelper

@pytest.mark.regression
class TestOrders:
    def test_create_new_order(self, tests_setup_order_id):
        # get product from db
        random_product_id = tests_setup_order_id.id

        partial_payload = {
            "line_items": [
                {
                    "product_id": random_product_id,
                    "quantity": 1
                }
            ]
        }

        # make api call
        order_helper = tests_setup_order_id.order_helper
        order_body = order_helper.create_order(**partial_payload)

        new_order_item_id = order_body['line_items'][0]['product_id']
        assert new_order_item_id == random_product_id, f'The id returned from order creation {new_order_item_id} is \
                                                        different than id which was used for order creation {random_product_id}'

        orders_dao = tests_setup_order_id.orders_dao
        order_items = orders_dao.get_order_by_order_id(order_id=order_body['id'])
        order_item_line_item =  [i for i in order_items if i['order_item_type'] == 'line_item']
        assert len(order_item_line_item) == 1, f'Expected 1 line item for order {order_body['id']}'

        order_item_id = order_item_line_item[0]['order_item_id']

        order_item_meta = orders_dao.get_order_item_meta(order_item_id=order_item_id)
        db_product_id = order_item_meta['_product_id']
        assert random_product_id == db_product_id , f'The returned product id from DB for the order is \
                                                     different from the random product id used for order creation'


    def test_create_paid_order_new_created_customer(self, tests_setup_order_id):
        # get product from db
        orders_dao = tests_setup_order_id.orders_dao
        order_helper = tests_setup_order_id.order_helper
        customer_helper = CustomerHelper()

        new_customer_id = customer_helper.create_customer()['id']
        random_product_id = tests_setup_order_id.id

        partial_payload = {
            'line_items': [
                {
                    "product_id": random_product_id,
                    "quantity": 1
                }
            ],
            'customer_id' : new_customer_id
        }

        # make api call
        order_body = order_helper.create_order(**partial_payload)

        assert order_body['customer_id'] == new_customer_id, f'The customer id in order response is different than the one who made the order'

        new_order_item_id = order_body['line_items'][0]['product_id']
        assert new_order_item_id == random_product_id, f'The id returned from order creation {new_order_item_id} is \
                                                                different than id which was used for order creation {random_product_id}'

        order_items = orders_dao.get_order_by_order_id(order_id=order_body['id'])
        order_item_line_item = [i for i in order_items if i['order_item_type'] == 'line_item']
        assert len(order_item_line_item) == 1, f'Expected 1 line item for order {order_body['id']}'

        order_item_id = order_item_line_item[0]['order_item_id']

        order_item_meta = orders_dao.get_order_item_meta(order_item_id=order_item_id)
        db_product_id = order_item_meta['_product_id']
        assert random_product_id == db_product_id, f'The returned product id from DB for the order is \
                                                             different from the random product id used for order creation'

    @pytest.mark.parametrize('update_status',[
        'failed',
        'cancelled',
        'on-hold'
    ])
    def test_update_order_status(self, update_status):
        #create new order
        order_helper = OrdersHelper()
        new_order = order_helper.create_order()

        new_order_status = new_order['status']
        new_order_id = new_order['id']

        order_after_update =  order_helper.update_order_status(**{'id': new_order_id, 'status':update_status})
        retrieved_order = order_helper.retrieve_order_by_id(new_order_id)

        assert new_order_status != order_after_update['status']
        assert retrieved_order['status'] == update_status
        assert retrieved_order['status'] == order_after_update['status']


    def test_negative_order_status(self):
        # create new order
        order_helper = OrdersHelper()
        new_order = order_helper.create_order()
        new_order_id = new_order['id']

        failed_order_response = order_helper.update_order_status(**{'id': new_order_id, 'status': ''.join(random.choices(string.ascii_lowercase, k=5))})

        assert failed_order_response['data']['status'] == 400
