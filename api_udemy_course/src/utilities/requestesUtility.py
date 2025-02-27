import json
import logging
import requests
import os
from api_udemy_course.src.configs import hosts_config
from requests_oauthlib import OAuth1

from woocommerce import API


class RequestUtility:
    def __init__(self):
        self.machine = os.environ.get('MACHINE')

        self.base_url = hosts_config.API_HOSTS[self.machine] + hosts_config.API_Route
        self.auth = OAuth1(hosts_config.WC_AUTH['consumer_key'],
                           hosts_config.WC_AUTH['consumer_secret'],
                           signature_type='auth_header')

        self.wc_host = hosts_config.WC_HOST[self.machine]

        self.wcapi = API(
            url=self.wc_host,
            consumer_key=hosts_config.WC_AUTH['consumer_key'],
            consumer_secret=hosts_config.WC_AUTH['consumer_secret'],
            version="wc/v3"
        )


    def woocommerce_post(self, endpoint, payload=None):
        res_api = self.wcapi.post(endpoint, data=payload)
        res_json = res_api.json()

        logging.info(f'POST API Response: {res_json}')
        return res_json

    def woocommerce_get(self, endpoint, **kwargs):
        res_api = self.wcapi.get(endpoint, params=kwargs)
        res_json = res_api.json()

        # logging.info(f'API Response: {res_json}')
        return res_json

    def woocommerce_put(self, endpoint, payload=None):
        res_api = self.wcapi.put(endpoint, data=payload)
        # logging.info(f'The payload data for PUT is {payload}')

        res_json = res_api.json()

        # logging.info(f'PUT API Response: {res_json}')
        return res_json

    def woocommerce_delete(self, endpoint):
        res_api = self.wcapi.delete(endpoint, params=None)

        res_json = res_api.json()
        return res_json




    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        url = self.base_url + endpoint

        print(f'URL --->: {url}')

        if not headers:
            headers = {'Content-Type': 'application/json'}

        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        status_code = rs_api.status_code
        assert status_code == expected_status_code, \
            f'Expected status code: {expected_status_code}, but got: {status_code}'

        logging.error(f'API Response: {rs_api.content}')

        # logging.debug(curlify.to_curl(rs_api.request))

        return rs_api.json()