#Funções dao
from model import database_prod
from model.produto import Produto 
lista = []
#Função para adicionar um novo produto no banco de dados
def adicionar_prod(novo_produto):
    try:
        conn = database_prod.connect_produto()
        cursor = conn.cursor()
        sql = """ INSERT INTO Produtos (nome,tipo,preco,estoque,excluir) VALUES (?,?,?,?,0);"""
        cursor.execute(sql,novo_produto.getProd())
        conn.commit()
    except Exception as e:
        print("Deu erro :",e)
    finally:
        conn.close()

#Função para listar os produtos
def listar_prod():
    lista = []
    try:
        conn = database_prod.connect_produto()
        cursor = conn.cursor()
        sql = """SELECT * FROM Produtos WHERE excluir = 0;"""
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for produto in linhas:
            id = produto[0]
            nome = produto[1]
            tipo = produto[2]
            preco = produto[3]
            estoque = produto[4]
            excluir = produto[5]

            novo_produto = Produto(id,nome,tipo,preco,estoque,excluir)
            lista.append(novo_produto)
    except Exception as e:
        print("deu erro: ",e)
    finally:
        conn.close()
    return lista
#Função para excluir um produto no banco de dados
def excluir_prod(id):
    try:
        conn = database_prod.connect_produto()
        cursor = conn.cursor()
        sql = """DELETE FROM Produtos WHERE id =?;"""
        cursor.execute(sql,[id])
        conn.commit()
    except Exception as e:
        print("Deu erro: ",e)
    finally:
        conn.close()
#Função para editar um produto no banco de dados
def editar_prod(produto):
    try:
        conn = database_prod.connect_produto()
        cursor = conn.cursor()
        sql = """UPDATE Produtos SET nome=? ,tipo=?, preco=?, estoque=? WHERE id=?;"""
        l = produto.getProd()
        l.append(produto.id)
        cursor.execute(sql,l)
        conn.commit()
    except Exception as e:
        print("Deu erro:", e)
    finally:
        conn.close()