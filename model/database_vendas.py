import sqlite3

def connect_vendas():
    conn = sqlite3.connect("database/venda.db")
    return conn