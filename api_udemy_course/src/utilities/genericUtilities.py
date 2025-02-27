import logging as logger
import random

import os
import json

from faker import Faker

def generate_random_email_and_password():
    logger.debug('Generating random email and password')

    fake = Faker()
    email = fake.company_email()
    password = fake.password()

    return {'email':email, 'password':password}


def generate_fake_product():
    product = dict()

    fake = Faker()
    product['name'] = fake.name()
    product['type'] = 'simple'
    product['regular_price'] = '{:.2f}'.format(random.uniform(5,15))

    return  product

def read_json_file(file_name):
    current_file_path = os.path.dirname(os.path.realpath(__file__))

    payload_template = os.path.join(current_file_path, '..', 'data', file_name)
    with open(payload_template) as f:
        payload = json.load(f)

        return  payload
