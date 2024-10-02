from qt_core import *
import model.estoque_dao as funcoes_estoque
from controller.cardEstoque_page import cardEstoque
FILE_UI = "view/estoque_tela_listar.ui"

class ListarEstoquePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.carregar()
    
    def carregar(self):
        lista = funcoes_estoque.listar_estoque()
        for estoque in lista:
            self.painel_scrollArea.addWidget(cardEstoque(estoque))
