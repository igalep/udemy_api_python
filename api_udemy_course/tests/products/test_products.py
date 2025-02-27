import logging
import pytest
from datetime import datetime, timedelta
from api_udemy_course.src.helpers.products_helper import ProductHelper
from api_udemy_course.src.dao.products_dao import ProductsDao
from api_udemy_course.src.utilities.genericUtilities import generate_fake_product
import random


@pytest.mark.regression
class TestProducts:
    product_h = ProductHelper()

    def test_list_products_with_filter(self):
        #get recent list of products (API)
        x_days_from_today = 10
        payload = dict()

        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date_iso = _after_created_date.isoformat()
        payload['after'] = after_created_date_iso
        payload['per_page'] = 2


        max_pages = 200
        all_products = []
        all_products_ = []
        for i in range(1, max_pages + 1):
            logging.info(f'Now in page : {i}')

            payload['page'] = i
            rs_api = self.product_h.get_products(**payload)

            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
                all_products_.append(rs_api)

        #get recent list of products (DB)
        product_db = ProductsDao()
        products_db_ans = product_db.get_products_after_created_date(date=after_created_date_iso)

        assert len(products_db_ans) == len(all_products), 'The number of items in DB are different from the number in API'

        ids_in_api = [i['id'] for i in all_products]
        ids_in_db = [i['ID'] for i in products_db_ans]

        # id_diff_list = list(set(ids_in_db) - set(ids_in_api))
        id_diff_list = list(set(ids_in_api) - set(ids_in_db))

        assert not id_diff_list

    def test_update_price(self):
        new_product_payload = generate_fake_product()
        created_product = self.product_h.create_product(payload=new_product_payload)
        new_product_id = created_product['id']

        product_price = created_product['regular_price']
        new_product_from_api = self.product_h.get_product_by_id(new_product_id)

        assert product_price == new_product_from_api['regular_price']

        update_payload = {
            'id': new_product_id,
            'payload':{
                'regular_price': '{:.2f}'.format(random.uniform(3, 5))
            }
        }

        self.product_h.update_product(**update_payload)
        updated_product = self.product_h.get_product_by_id(new_product_id)

        assert update_payload['payload']['regular_price'] == updated_product['regular_price']



    @pytest.mark.parametrize('sale_status',
                             [True,
                              False])
    def test_update_sale_price(self, sale_status, sale_price_fixture):
        new_product_payload = generate_fake_product()
        created_product = self.product_h.create_product(payload=new_product_payload)
        regular_price = float(created_product['regular_price'])

        discount = sale_price_fixture

        updated_payload = {
            'id' : created_product['id'],
            'payload' : {
                'sale_price' : str(round(regular_price * (1 - discount), 2)) if type(discount) == float else ''
            }
        }
        on_sale_status_new_p = created_product['on_sale']
        assert on_sale_status_new_p == False

        update_product = self.product_h.update_product(**updated_payload)

        assert update_product['on_sale'] == sale_status , f'The product with id {update_product['id']} has a wrong on_sale status'

    @pytest.fixture
    def sale_price_fixture(self, sale_status):
        aa =  random.uniform(0, 1) if sale_status else ''
        return aa