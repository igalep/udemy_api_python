import logging

from api_udemy_course.src.utilities.dbUtility import DbUtility

class CustomerDAO:
    def __init__(self):
        self.dbHelper = DbUtility()

        pass

    def get_customer_by_email(self, email):
        query = f'SELECT * FROM udemy_wp.wp_users WHERE user_email = "{email}"'

        query_response = self.dbHelper.execute_select_query(query)
        return query_response

    def get_random_customer(self):
        query = 'SELECT * FROM udemy_wp.wp_users ORDER BY RAND() LIMIT 1'

        query_response = self.dbHelper.execute_select_query(query)

        logging.info(f'Random customer is : {query_response}')
        return query_response


