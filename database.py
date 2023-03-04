from config import password, db_name, user, host
import psycopg2
import json


def create_table():
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
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS data (
                    id int,
                    name text,
                    price text,
                    rating text,
                    num_revives text,
                    picture_link text,
                    product_link text);"""
            )


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


def put_data(data):
    """with open('all_links.json', encoding='utf-8') as file:
        data = json.load(file)"""
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
            for item in data:
                cursor.execute(
                    "INSERT INTO data (id, name, price, rating, num_revives, picture_link, product_link) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (item['id'], item['name'], item['price'], item['rating'], item['num_revives'], item['picture_link'],
                     item['product_link']))

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed, data into")


def drop():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name

        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """drop table data;"""
            )


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
