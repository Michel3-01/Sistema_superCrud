from model import database_vendas
from model.vendas import Vendas
#Adicionar a venda no banco de dados
def adicionar(nova_venda):
    try:
        conn = database_vendas.connect_vendas()
        cursor = conn.cursor()
        sql ="""INSERT INTO Vendas (tipo,valor_total,data,horario) VALUES (?,?,?,?);"""
        cursor.execute(sql,nova_venda.getVenda())
        conn.commit()
    except Exception as e:
        print("Deu erro: ",e)
    finally:
        conn.close()

def listar_vendas():
    lista_vendas = []
    try:
        conn = database_vendas.connect_vendas()
        cursor = conn.cursor()
        sql = """SELECT * FROM Vendas;"""
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for vendas in linhas:
            id = vendas[0]
            tipo = vendas[1]
            valor = vendas[2]
            data = vendas[3]
            horario =  vendas[4]
            nova_venda = Vendas(id,tipo,valor,data,horario)
            lista_vendas.append(nova_venda)
    except Exception as e:
        print("Deu erro: " ,e)
    finally:
        conn.close()
    return lista_vendas

