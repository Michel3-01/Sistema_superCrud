from qt_core import *
from model.produto import Produto
import model.produtos_dao as funcoes_produtos
FILE_UI = "view/edicao_prod_page.ui"

class EdicaoProdPage(QWidget):
    def __init__(self,janela_produtos,produtos):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.janela_produtos = janela_produtos
        self.produtos = produtos
        self.salvar_btn.clicked.connect(self.salvar_edicao)
        self.carregar_dados()
        self.carregar_tipoProd()
    def carregar_tipoProd(self):
        lista_tipoProd = ["produtos alimentícios","bebidas","produtos de higiene pessoal","produtos de limpeza","produtos de beleza"]
        self.comboBox_prod.addItems(lista_tipoProd)
    def carregar_dados(self):
        self.nome.setText(self.produtos.nome)
       
        self.preco.setText(str(self.produtos.preco))
        self.estoque.setText(str(self.produtos.quant_estoque))
    def salvar_edicao(self):
        nome = self.nome.text()
        tipo = self.comboBox_prod.currentText()
        preco = self.preco.text()
        estoque = self.estoque.text()

        nova_edicao = Produto(self.produtos.id,nome,tipo,preco,estoque)
        funcoes_produtos.editar_prod(nova_edicao)

        self.janela_produtos.show_listar()
