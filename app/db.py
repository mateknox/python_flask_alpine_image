import sqlite3
import config
import logging


def create_table():
    try:
        sqlite_connection = sqlite3.connect(config.DATABASE_NAME)
        sqlite_create_table_query = '''CREATE TABLE clients (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    birthday_date datetime);'''
        cursor = sqlite_connection.cursor()

        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        logging.info("Table created")
    except sqlite3.Error as error:
        logging.info(error)
        cursor.close()
    finally:
        if (sqlite_connection):
            cursor.close()
            sqlite_connection.close()


def insert_user(id, name, email, birthday_date):
    try:
        sqlite_connection = sqlite3.connect(config.DATABASE_NAME)
        sqlite_insert_query = "INSERT INTO clients (id, name, email, birthday_date) VALUES " + '(' + id + ', "' \
                              + name + '", "' + email + '", ' + birthday_date + ')'
        logging.info(sqlite_insert_query)
        cursor = sqlite_connection.cursor()

        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        logging.info("Inserted to db")
    except sqlite3.Error as error:
        logging.info(error)
        cursor.close()
    finally:
        if (sqlite_connection):
            cursor.close()
            sqlite_connection.close()


def select_from_db(select_statement, return_one_record=False):
    try:
        sqlite_connection = sqlite3.connect(config.DATABASE_NAME)
        sqlite_select_query = select_statement
        cursor = sqlite_connection.cursor()

        cursor.execute(sqlite_select_query)
        if return_one_record:
            record = cursor.fetchone()
        else:
            record = cursor.fetchall()
        logging.info(record)
        return record
    except sqlite3.Error as error:
        logging.info(error)
        cursor.close()
    finally:
        if (sqlite_connection):
            cursor.close()
            sqlite_connection.close()


def insert_to_db(name, mail, date):
    create_table()
    # Just select everything
    statement = "select * from clients;"
    select_from_db(statement, False)
    # Get max id value to insert bigger one
    statement = "select max(id) from clients;"
    max_id = select_from_db(statement, True)
    # Insert first record if table is empty
    if max_id[0] is None:
        try:
            insert_user("1", name, mail, date)
        except Exception as error:
            logging.info(error)
    # Insert seq+1 record otherwise
    else:
        max_id = max_id[0] + int(1)
        try:
            insert_user(str(max_id), name, mail, date)
        except Exception as error:
            logging.info(error)