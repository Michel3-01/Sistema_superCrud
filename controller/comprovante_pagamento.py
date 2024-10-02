from qt_core import *

FILE_UI = 'view/comprovante_pagamento.ui'

class comprovantePagamentoPage(QWidget):
    def __init__(self,lista_produtos,valor_total,valor_pago,troco,data,hora):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        self.valor_total = valor_total
        print(self.valor_total)
        

        #self.txt_lista.setText(lista_produtos)
        self.txt_valor_total.setText(self.valor_total)