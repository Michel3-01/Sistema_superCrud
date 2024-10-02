from qt_core import*
from controller.produdos_main_window import ProdutosMain
from controller.vendas_main_window import VendasMain
from controller.resumo_page import resumoPage
from controller.estoque_listar_page import ListarEstoquePage

#Arquivo .ui
FILE_UI = "view/main_page.ui"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)


        #Evento dos botões
        self.produtos_btn.clicked.connect(self.show_produtos)
        self.vendas_btn.clicked.connect(self.show_vendas)
        self.dashboard_btn.clicked.connect(self.show_dashboard)
        self.estoque_btn.clicked.connect(self.show_estoque)
    def show_produtos(self):
        self.painel_principal.setCurrentIndex(0)
        self.painel_principal.insertWidget(0,ProdutosMain())
    def show_vendas(self):
        self.painel_principal.setCurrentIndex(1)
        self.painel_principal.insertWidget(1,VendasMain())
    def show_dashboard(self):
        self.painel_principal.setCurrentIndex(2)
        self.painel_principal.insertWidget(2,resumoPage())
    def show_estoque(self):
        self.painel_principal.setCurrentIndex(3)
        self.painel_principal.insertWidget(3,ListarEstoquePage())
     
        