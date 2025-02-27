import pytest
import logging as logger

from api_udemy_course.src.helpers.customer_helper import CustomerHelper
from api_udemy_course.src.dao.customers_dao import CustomerDAO
from api_udemy_course.src.dao.products_dao import ProductsDao
from api_udemy_course.src.helpers.products_helper import ProductHelper
from api_udemy_course.src.utilities.genericUtilities import generate_fake_product

pytestmark = [
    pytest.mark.smoke,
    pytest.mark.regression
]

@pytest.mark.customers
def test_create_customer_only_email_password():
    logger.info('Create customer with email')
    logger.debug('Create customer with password')

    cust_obj = CustomerHelper()
    # cust_api_info = cust_obj.create_customer()
    cust_api_info = cust_obj.create_customer()

    assert cust_api_info['email'] is not None

    db_access = CustomerDAO()
    db_cust_info = db_access.get_customer_by_email(cust_api_info['email'])

    assert cust_api_info['id'] == db_cust_info[0]['ID'], f'Create customer response id not the same as in db'

    # prod_obj = ProductHelper()
    # product_api_info = prod_obj.get_product()

    assert 1==1

@pytest.mark.customers
def test_get_all_customers():
    logger.info('Get all customers')
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.get_all_customers()

    assert  len(cust_api_info) > 1

@pytest.mark.negative
@pytest.mark.customers
def test_negative_create_customer_existing_email():
    #get existing user from db
    db_access = CustomerDAO()
    customer_helper = CustomerHelper()
    random_customer = db_access.get_random_customer()

    random_customer_email = random_customer[0]['user_email']

    #try to create user with existing email
    res_ans = customer_helper.create_customer(email=random_customer_email)

    assert res_ans['data']['status'] == 400
    assert 'An account is already registered' in res_ans['message']

@pytest.mark.products
def test_get_all_products():
    prod_obj = ProductHelper()
    prod_response  = prod_obj.get_products()

    assert len(prod_response) > 15, f'Less than 15 products returned'

@pytest.mark.products
def test_get_product_by_id():
    #get product from db
    db_helper = ProductsDao()

    product_from_db = db_helper.get_random_product_id()
    product_id = product_from_db[0]['ID']

    #get product from api
    prod_api_helper = ProductHelper()

    prod_from_api = prod_api_helper.get_product_by_id(product_id=product_id)

    assert product_id == prod_from_api['id'],'The product id from DB is different from the one in API'
    assert product_from_db[0]['post_title'] == prod_from_api['name'], 'The name in DB is different from the one in API'

@pytest.mark.products
def test_create_product():
    #create new product
    new_product = generate_fake_product()

    product_helper = ProductHelper()
    created_product_response = product_helper.create_product(payload= new_product)

    new_prod_id,new_prod_name = created_product_response['id'], created_product_response['name']

    #get product from_db
    db_helper = ProductsDao()
    new_prod_from_db = db_helper.get_product_by_id(product_id=new_prod_id)

    assert new_prod_name == new_prod_from_db[0]['post_title'], 'The product name from db is equal to the created product name'


