from qt_core import*
from controller.cadastro_produtos_page import CadastroProdPage
from controller.produtos_listar_page import ListarProdPage
from controller.edicao_produtos_page import EdicaoProdPage
#Arquivo tipo ui
FILE_UI = "view/produtos_tela_principal.ui"

class ProdutosMain(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)


        self.cadastrar_btn.clicked.connect(self.show_cadastrar)
        self.listar_btn.clicked.connect(self.show_listar)

    def show_cadastrar(self):
        self.painel_produtos.setCurrentIndex(0)
        self.painel_produtos.insertWidget(0,CadastroProdPage(self))
    def show_listar(self):
        self.painel_produtos.setCurrentIndex(1)
        self.painel_produtos.insertWidget(1,ListarProdPage(self))
    def show_edicao(self,produto=None):
        self.painel_produtos.setCurrentIndex(2)
        self.painel_produtos.insertWidget(2,EdicaoProdPage(self,produto))
