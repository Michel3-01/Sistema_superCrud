from qt_core import *
import model.produtos_dao as funcoes_produtos
import model.vendas_dao as funcoes_vendas
import model.estoque_dao as funcoes_estoque
from model.vendas import Vendas
from datetime import datetime
from model.estoque import Estoque
from controller.comprovante_pagamento import comprovantePagamentoPage
FILE_UI = "view/novaVenda_page.ui"

class NovaVendaPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        self.produto_atual = None
        #lista de produtos da tableWidget
        self.list_produtos = []
        #funções dos  botões
        self.adicionar_btn.clicked.connect(self.add_produto_tabela)
        self.remover_btn.clicked.connect(self.excluir_linha_tabela)
        self.finalizar_venda_btn.clicked.connect(self.finalizar_venda)

        

        #carrega os produtos na listWidget   
        self.carregar_produtos()    
        #carregar os tipos de pagamentos
        self.carregar_pagamentos()  
        

    #Carrega os produtos na tableWidget
    def add_produto_tabela(self):
        print( self.quantidade.text().isnumeric())
        if self.quantidade.text().isnumeric():
            
            if self.quantidade.text() == "" or self.valor_unitario.text() ==  "" or int(self.quantidade.text()) <= 0:
                QMessageBox.about(NovaVendaPage(),"Alerta","Preenchar os campos corretamente!")
            else:
                nome_produto = self.produto_atual.nome

                #Calcular o valor unitário do produto vezes a quantidade de produtos
                self.quant_preco = int(self.quantidade.text()) * float(self.valor_unitario.text())     
                
                #Criar a tupla com a informações do produto e da compra 
                produto = {'id':len(self.list_produtos),'quantidade':self.quantidade.text(),'nome':nome_produto,'total':self.quant_preco}
                self.list_produtos.append(produto)
                self.atualizar_dados_venda()
                #Estoque
                lista = funcoes_estoque.listar_estoque()
                for estoque in lista:
                    if estoque.id == self.produto_atual.id:
                        vendidos = estoque.vendidos
                        
                nome_produto = self.produto_atual.nome
                quant_inicial = self.produto_atual.quant_estoque
                vendidos = vendidos + int(self.quantidade.text())
                
                quant_atual = int(self.produto_atual.quant_estoque) - vendidos
                x = (100*quant_atual)/quant_inicial
                if x <= 20:
                    situacao = 'Vermelho'
                elif x >= 50:
                    situacao = 'Verde'
                else:
                    situacao = 'Normal'
                
                nova_edicao= Estoque(self.produto_atual.id,nome_produto,quant_inicial,vendidos,quant_atual,situacao,self.produto_atual.id)
                print(nova_edicao.vendidos)
                funcoes_estoque.editar_estoque(nova_edicao)
                #funcoes_estoque.adicionar_estoque(novo_estoque)
        else:
            QMessageBox.about(NovaVendaPage(),"Alerta","valores precisam ser numéricos e números positivos!")

    def atualizar_dados_venda(self):
        #valor total da venda 
        self.valor_total = 0
        for produtos in self.list_produtos:
            self.valor_total = self.valor_total + produtos['total']
            self.valor_total = round(self.valor_total,2)
            self.subtotal.setText(f'R${self.valor_total}')

        #zera as linhas da tabela
        self.tabela_produtos.setRowCount(0)
        for produtos in self.list_produtos:
            self.add_linha(produtos)
    def add_linha(self,produtos):
        rowCount = self.tabela_produtos.rowCount()
        self.tabela_produtos.insertRow(rowCount)

        #Elementos de cada coluna da tabela
        id = QTableWidgetItem(str(produtos['id']))
        nome = QTableWidgetItem(produtos['nome'])
        quantidade = QTableWidgetItem(produtos['quantidade'])
        total = QTableWidgetItem(str(produtos['total']))
       
        #Inserir os elementos da tabela na coluna correspondente
        self.tabela_produtos.setItem(rowCount,0,id)
        self.tabela_produtos.setItem(rowCount,1,nome)
        self.tabela_produtos.setItem(rowCount,2,quantidade)
        self.tabela_produtos.setItem(rowCount,3,total)
      
    def carregar_produtos(self):
        lista = funcoes_produtos.listar_prod()
        for produto in lista:
            self.produtos_listWidget.addItem(produto.nome)
        
            #Pegar as informações do produto selecionado
            self.produtos_listWidget.currentRowChanged.connect(self.pegar_produto)
    #Função para buscar as informações do produto
    def pegar_produto(self,index):
        lista = funcoes_produtos.listar_prod()
        self.listar_produtos = []
       
        for produtos in lista:
            self.listar_produtos.append(produtos)   
        self.produto_atual = self.listar_produtos[index]

        #Set o campo valor unitário para o valor do produto atual
        self.valor_unitario.setText(str(self.produto_atual.preco))

    #Excluir Linha da qtableWidget
    def excluir_linha_tabela(self):

       if not self.list_produtos:
             QMessageBox.about(NovaVendaPage(),"Alerta","A qTableWidget está vazia!")
       else:
            linha = self.tabela_produtos.currentRow()
            id_removido = self.tabela_produtos.rowCount()-1
            self.tabela_produtos.removeRow(linha)
            del(self.list_produtos[id_removido])
            
            
       self.atualizar_dados_venda()
    #Carregar tipos de pagamentos
    def carregar_pagamentos(self):
        lista_pagamentos = ['crédito','debito','à vista','pix']
        self.pagamentos_comboBox.addItems(lista_pagamentos)
    #Formatar a data da compra
    def formatando_data(self):
        data = self.dateEdit.text()
        atual = datetime.now()
        ano = atual.year
        print(ano)
        if(int(data[6:]) < ano or int(data[6:]) > ano):
            QMessageBox.about(NovaVendaPage(),"Alerta","Preenchar a data corretamente!")
    #Finaliza a venda realizada
    def finalizar_venda(self):
        
        if (self.subtotal.text() == "" or self.total_pago == ""  or self.troco == ""):
            QMessageBox.about(NovaVendaPage(),"Alerta","Ainda possui campos vazios!")
        else:
            valor_tot = self.subtotal.text()[2:]
            if (self.total_pago.text().isnumeric()):
                valor_troco =   float(self.total_pago.text()) - float(valor_tot)
                valor_troco = round(valor_troco,2)
                
                if valor_troco < 0:
                    QMessageBox.about(NovaVendaPage(),"Alerta","Valor insuficiênte para paga a compra!")
                else:
                    
                    self.troco.setText(str(valor_troco))
                    #criar nova_venda
                    tipo = self.pagamentos_comboBox.currentText()
                    nova_venda = Vendas(None,tipo,valor_tot,self.dateEdit.text(),self.timeEdit.text())
                    funcoes_vendas.adicionar(nova_venda)
            else:
                QMessageBox.about(NovaVendaPage(),"Alerta","valores precisam ser numéricos!")


            lista_produtos_venda = []
            for produtos in self.list_produtos:
                produto = {'nome':produtos['nome'],'quantidade':produtos['quantidade'],'total':produtos['total']}
                lista_produtos_venda.append(produto)
            #win
            #self.win_comprovante = comprovantePagamentoPage(lista_produtos_venda,self.subtotal.text(),self.total_pago.text(),self.troco.text(),self.dateEdit.text(),self.timeEdit.text())
            #self.win_comprovante.show()



      
        
        
