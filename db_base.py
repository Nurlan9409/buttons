import psycopg2 as db

class Database:
    @staticmethod
    def connect(query,query_type):
        database = db.connect(
            database = "aiogram_bot",
            user = "postgres",
            password ="3110",
            host = "localhost"
        )

        cursor = database.cursor()
        cursor.execute(query)
        if query_type == "insert":
            database.commit()
            return "inserted"

        if query_type == "select":
            return cursor.fetchall()


