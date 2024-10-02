from qt_core import *
import model.estoque_dao as funcoes_estoque
FILE_UI = "view/cardEstoquePage.ui"

class cardEstoque(QWidget):
    def __init__(self,estoque):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        self.estoque = estoque
        self.label_id.setText(str(self.estoque.id))
        self.label_nome.setText(self.estoque.nome)
        self.label_quant_inicial.setText(str(self.estoque.quant_inicial))
        self.label_quant_atual.setText(str(estoque.quant_atual))
        self.label_nome.setText(self.estoque.nome)
        self.label_quant_inicial.setText(str(self.estoque.quant_inicial))

       
        for estoque in funcoes_estoque.listar_estoque():
            if self.estoque.id == estoque.id_produto:
              
                    rq = self.estoque.quant_inicial - estoque.vendidos #rq guarda o valor da quantidade de produtos atual.
                    x = (100*rq)/self.estoque.quant_inicial
                    if x <= 20:
                        estoque.situacao = 'Vermelho'
                        self.label_situacao.setStyleSheet('font-size: 22px; color: red;')
                    elif x > 50:
                        estoque.situacao = 'Verde'
                        self.label_situacao.setStyleSheet('font-size: 22px; color: rgb(0, 255, 0);')
                    else:
                        estoque.situacao = 'Normal'
                        self.label_situacao.setStyleSheet('font-size: 22px; color: white;')


                    self.label_quant_atual.setText(str(rq))
                    self.label_situacao.setText(estoque.situacao)
                    self.label_vendidos.setText(str(estoque.vendidos))
        