import os

import pymysql
import logging as logger
from api_udemy_course.src.configs import hosts_config


class DbUtility:
    def __init__(self):
        self.machine = os.environ.get('MACHINE')


    def create_connection(self):
        connection = pymysql.connect(user=hosts_config.DB_CREDENTIALS['user'],
                                     password=hosts_config.DB_CREDENTIALS['password'],
                                     host=hosts_config.DB_HOSTS[self.machine],
                                     port=hosts_config.DB_PORTS[self.machine])

        return connection

    def execute_select_query(self, query):
        connection = self.create_connection()

        try:
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            query_result = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise Exception(f'Error with execution query : {query} \n Error :{e}')
        finally:
            logger.info(f'query : {query} was successfully executed')
            connection.close()

            return query_result