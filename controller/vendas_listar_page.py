from qt_core import*
import model.vendas_dao as funcoes_vendas
from controller.cardVendas_page import cardVendas
FILE_UI = "view/vendas_tela_listar.ui"

class ListarVendasPage(QWidget):
    def __init__(self,janela_vendas):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        self.janela_vendas = janela_vendas
        self.carregar()
    def carregar(self):
        lista = funcoes_vendas.listar_vendas()
        for vendas in lista:
            self.painel_scrollArea.addWidget(cardVendas(vendas,self.janela_vendas))
            