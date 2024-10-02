import sqlite3

def connect_estoque():
    conn = sqlite3.connect("database/estoque.db")
    return conn