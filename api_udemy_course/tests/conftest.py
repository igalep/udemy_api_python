import pytest
from api_udemy_course.src.dao.products_dao import ProductsDao
from api_udemy_course.src.dao.orders_dao import OrdersDao
from api_udemy_course.src.helpers.orders_helper import OrdersHelper
from api_udemy_course.src.helpers.coupon_helper import CouponHelper
from dataclasses import dataclass

@dataclass
class SetupData:
    id : int
    order_helper : OrdersHelper
    orders_dao : OrdersDao



@pytest.fixture(scope="class")
def tests_setup_order_id():
    product_dao = ProductsDao()
    random_product = product_dao.get_random_product_id()

    return SetupData(id=random_product[0]['ID'], order_helper=OrdersHelper(), orders_dao=OrdersDao())


@pytest.fixture()
def delete_coupon():
    coupon_to_delete = []

    yield coupon_to_delete

    for coupon in coupon_to_delete:
        CouponHelper().delete_coupon(coupon_id= coupon)

