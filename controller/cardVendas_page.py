from qt_core import *

FILE_UI = "view/cardVendasPage.ui"

class cardVendas(QWidget):
    def __init__(self,vendas,janela_vendas):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.vendas = vendas
        self.janela_vendas = janela_vendas

        self.label_id.setText(str(self.vendas.id))
        self.label_valor.setText(str(self.vendas.valor))
        self.label_tipo.setText(str(self.vendas.tipo))
        self.label_data.setText(str(self.vendas.data))
        self.label_horario.setText(str(self.vendas.horario))