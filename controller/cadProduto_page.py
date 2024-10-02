from qt_core import *
from model.produtos_dao import excluir_prod
import model.estoque_dao as funcoes_estoque
FILE_UI ="view/cadProdutoPage.ui"

class cadProduto(QWidget):
    def __init__(self,produtos,janela_produto):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.produtos = produtos
        self.janela_produto = janela_produto

        #Funcão dos botões
        self.editar_btn.clicked.connect(self.editar)
        self.excluir_btn.clicked.connect(self.excluir)


        #colocando o nomes nos produtos
        self.label_id.setText(str(self.produtos.id))
        self.label_nome.setText(self.produtos.nome)
        self.label_preco.setText(str(self.produtos.preco))
        self.label_tipo.setText(self.produtos.tipo_prod)
        self.label_estoque.setText(str(self.produtos.quant_estoque))
        
    #Editar um produto no banco       
    def editar(self):
        self.janela_produto.show_edicao(self.produtos)
    #Excluir um produto no banco de dados
    def excluir(self):
        lista = funcoes_estoque.listar_estoque()
        id = self.produtos.id
        for estoque in lista:
            if estoque.id == id:
                if estoque.vendidos != estoque.quant_inicial:
                    QMessageBox.about(self.janela_produto,"Alerta","Só pode excluir o produto quando o estoque for 0.")  
                else:
                    excluir_prod(id)
                    funcoes_estoque.excluir_estoque(id)
                    self.load()
    def load(self):
        self.janela_produto.show_listar()
   