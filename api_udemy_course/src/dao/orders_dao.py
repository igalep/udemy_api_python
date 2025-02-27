from api_udemy_course.src.utilities.dbUtility import  DbUtility


class OrdersDao:
    def __init__(self):
        self.db_helper = DbUtility()


    def get_order_by_order_id(self, order_id):
        query = f'select * FROM udemy_wp.wp_woocommerce_order_items where order_id = {order_id}'

        query_ans = self.db_helper.execute_select_query(query=query)
        return query_ans

    def get_order_item_meta(self, order_item_id):
        query = f'SELECT * FROM  udemy_wp.wp_woocommerce_order_itemmeta WHERE order_item_id  = {order_item_id}'

        query_ans = self.db_helper.execute_select_query(query=query)

        line_details = dict()
        for meta in query_ans:
            line_details[meta['meta_key']] = int(meta['meta_value']) if meta['meta_value'].isdigit() \
                                                                     else meta['meta_value']

        return line_details