import os
import sys
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

DB_NAME = 'rest_api.sqlite'
DB_PATH = 'db/' + DB_NAME

Base = declarative_base()
 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password_hash = Column(String(250), nullable=False)
    email = Column(String(250))
    phone = Column(String(250))
    address = Column(String(250))
    additional_info = Column(String(250))
    is_admin = Column(Boolean(), nullable=False)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///' + DB_PATH)
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

# import sqlite3

# DB_NAME = 'rest_api.sqlite'
# DB_PATH = 'db/' + DB_NAME

# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)
 
#     return None

# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     :return:
#     """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)

# def main():
#     database = DB_PATH
 
#     sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
#                                         id integer PRIMARY KEY, 
#                                         username text NOT NULL, 
#                                         password text NOT NULL, 
#                                         email text, 
#                                         phone text,
#                                         address text,
#                                         additional_info text,
#                                         is_admin boolean
#                                         );"""
 
#     # create a database connection
#     conn = create_connection(database)
#     if conn is not None:
#         # create user table
#         create_table(conn, sql_create_user_table)
#     else:
#         print("Error! cannot create the database connection.")

# if __name__ == '__main__':
#     main()