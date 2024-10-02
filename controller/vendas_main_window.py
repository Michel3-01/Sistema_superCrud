from qt_core import *
from controller.nova_venda_page import NovaVendaPage
from controller.vendas_listar_page import ListarVendasPage

FILE_UI = "view/vendas_tela_principal.ui"

class VendasMain(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.novaVenda_btn.clicked.connect(self.nova_venda)
        self.listar_btn.clicked.connect(self.listar_vendas)
    
    def nova_venda(self):
        self.painel_vendas.setCurrentIndex(0)
        self.painel_vendas.insertWidget(0,NovaVendaPage())
    def listar_vendas(self):
        self.painel_vendas.setCurrentIndex(1)
        self.painel_vendas.insertWidget(1,ListarVendasPage(self))