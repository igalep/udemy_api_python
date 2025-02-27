import random

from api_udemy_course.src.utilities.dbUtility import DbUtility



class ProductsDao:
    def __init__(self):
        self.dbUtility = DbUtility()

    def get_random_product_id(self):
        query = 'select * from udemy_wp.wp_posts where post_type = "product" limit 10'
        query_ans = self.dbUtility.execute_select_query(query)

        return random.sample(query_ans,1)

    def get_product_by_id(self, product_id):
        query = f'select * from udemy_wp.wp_posts where post_type = "product" and id = {product_id}'
        query_ans = self.dbUtility.execute_select_query(query)

        return query_ans

    def get_products_after_created_date(self, date):
        query = f'select * from udemy_wp.wp_posts where post_type = "product" and post_date > "{date}"'
        query_ans = self.dbUtility.execute_select_query(query)

        return query_ans
