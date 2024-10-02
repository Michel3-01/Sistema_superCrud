import sqlite3

def connect_produto():
    conn = sqlite3.connect("database/produtos.db")
    return conn