from config import password, db_name, user, host
from aiogram import Bot,Dispatcher,types,executor
import asyncio
import psycopg2

def output():
    connection = None
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name

        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM data;")
            rows = cursor.fetchall()
            data =[]
            for row in rows:
                row_dict = {"id": row[0], "name": row[1], "price": row[2],
                            "rating": row[3], "num_revives": row[4], "picture_link": row[5], "product_link": row[6]}
                data.append(row_dict)
        return data
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed, data into")