from qt_core import *
from controller.cadProduto_page import cadProduto
import model.produtos_dao as funcoes_produto
FILE_UI = "view/produtos_tela_listar.ui"
class ListarProdPage(QWidget):
    def __init__(self,janela_produtos):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.janela_produtos = janela_produtos
        self.carregar()

    def carregar(self):
        lista = funcoes_produto.listar_prod()
        for self.produto in lista:
            self.painel_scrollArea.addWidget(cadProduto(self.produto,self.janela_produtos))