from model import database_estoque
from model.estoque import Estoque
#Adicionar adicionar
def adicionar_estoque(estoque):
    try:
        conn = database_estoque.connect_estoque()
        cursor = conn.cursor()
        sql = """INSERT INTO Estoque (nome_prod,quant_inicial,vendidos,quant_atual,situacao,id_produto) VALUES (?,?,?,?,?,?);"""
        cursor.execute(sql,estoque.getEstoque())
        conn.commit()
    except Exception as e:
        print("Deu erro: ",e)
    finally:
        conn.close()
#Lista estoque
def listar_estoque():
    listar_estoque = []
    try:
        conn = database_estoque.connect_estoque()
        cursor = conn.cursor()
        sql = """SELECT * FROM Estoque;"""
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for estoque in linhas:
            id = estoque[0]
            nome_produto = estoque[1]
            quant_inicial = estoque[2]
            vendidos = estoque[3]
            quant_atual = estoque[4]
            situacao = estoque[5]
            id_estoque = estoque[6]
            novo_estoque = Estoque(id,nome_produto,quant_inicial,vendidos,quant_atual,situacao,id_estoque)
            listar_estoque.append(novo_estoque)
    except Exception as e:
        print("Deu erro: ",e)
    finally:
        conn.close()
    return listar_estoque

def editar_estoque(estoque):
    try:
        conn = database_estoque.connect_estoque()
        cursor = conn.cursor()
        sql = """UPDATE Estoque SET nome_prod=?, quant_inicial=?, vendidos=?, quant_atual=?, situacao=?, id_produto=? WHERE id=?;"""
        l = estoque.getEstoque()
        l.append(estoque.id)
        cursor.execute(sql,l)
        conn.commit()
    except Exception as e:
        print("Deu erro: ", e)
    finally:
        conn.close()
    
#Deleta do estoque com base no id do produto
def excluir_estoque(id_produto):
    try:
        conn = database_estoque.connect_estoque()
        cursor = conn.cursor()
        sql = "DELETE FROM Estoque WHERE id =?;"
        cursor.execute(sql,[id_produto])
        conn.commit()
    except Exception as e:
        print("Deu erro:", e)
    finally: 
        conn.close()


