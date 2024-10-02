from qt_core import*
from model.produto import Produto
from model.produtos_dao import adicionar_prod, listar_prod
import model.estoque_dao as funcoes_estoque
from model.estoque import Estoque     
 
FILE_UI = "view/cadastro_prod_page.ui"

class CadastroProdPage(QWidget):
    def __init__(self,janela_produtos):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.janela_produtos = janela_produtos
        #Evento dos botões
        self.salvar_btn.clicked.connect(self.salvar_produto)
        self.cancelar_btn.clicked.connect(self.cancelar)
        self.carregar_tipoProd()
    def carregar_tipoProd(self):
        lista_tipoProd = ["produtos alimentícios","bebidas","produtos de higiene pessoal","produtos de limpeza","produtos de beleza"]
        self.comboBox_prod.addItems(lista_tipoProd)
    def limpar_campos(self):
        self.nome.setText("")
        self.preco.setText("")
        self.estoque.setText("")
    def salvar_produto(self):
        if (self.nome.text()=="" or self.preco.text() == "" or self.estoque.text()==""):
            QMessageBox.about(self.janela_produtos,"Alerta","Preencha os campos corretamente!")
        elif (self.estoque.text().isnumeric() == False):
            QMessageBox.about(self.janela_produtos,"Alerta","O valores precisam ser númericos e positivo!")
        else:
            nome = self.nome.text()
            tipo = self.comboBox_prod.currentText()
            preco = self.preco.text()
            estoque = self.estoque.text()
            novo_produto = Produto(None,nome,tipo,preco,estoque)
            adicionar_prod(novo_produto)
            novo_estoque = Estoque(None,nome,estoque,0,0,"Normal",None)
            funcoes_estoque.adicionar_estoque(novo_estoque)
            self.janela_produtos.show_listar()
            self.limpar_campos()
            
    def cancelar(self):
          self.janela_produtos.show_listar()