import sqlite3


class Repo:
    @staticmethod
    def perform_db_query(query):
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        conn.close()

    @staticmethod
    def perform_db_query_and_return_data(query):
        conn = sqlite3.connect('company.db')
        cursor = conn.cursor()
        cursor.execute(query)
        all_data = cursor
        conn.commit()
        conn.close()
        return all_data
