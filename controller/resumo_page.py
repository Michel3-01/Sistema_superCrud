from qt_core import *
import matplotlib.pyplot as grafico
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg       
import model.estoque_dao as funcoes_estoque
import model.vendas_dao as funcoes_vendas
import model.produtos_dao as funcoes_produto
import numpy as np


FILE_UI = "view/resumo_page.ui"

class resumoPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.carregar_resumo()
    def carregar_resumo(self):
        #Gráfico de pizza
        quant_credito = 0
        quant_aVista = 0
        quant_debito = 0
        quant_pix = 0
        lista = funcoes_vendas.listar_vendas()
        for vendas in lista:
            if (vendas.tipo == "crédito"):
                quant_credito += 1
            elif(vendas.tipo == "debito"):
                quant_debito += 1
            elif(vendas.tipo == "à vista"):
                quant_aVista += 1
            elif(vendas.tipo == "pix"):
                quant_pix +=1
        
        labels = 'crédito','debito','à vista','pix'
        x = [quant_credito,quant_debito,quant_aVista,quant_pix]
        explode =(0,0.1,0,0)
        figura01 = grafico.Figure(figsize=(11.4,2.5),dpi=66)
        ax01 = figura01.add_subplot(111)
           
        ax01.pie(x,explode = explode,labels=labels,autopct='%1.1f%%',shadow=True, startangle=90)
        ax01.axis('equal')
        canva01 =FigureCanvasQTAgg(figura01)
        self.grafico_04.addWidget(canva01)

       
        #Gráfico de linha
        lista_quant_vendidos = []
        lista_nome_prod = []
    
        lista = funcoes_estoque.listar_estoque()
        
        for estoque in lista:
            lista_quant_vendidos.append(estoque.vendidos)
            lista_nome_prod.append(estoque.nome)
            
        x = lista_nome_prod
        y = lista_quant_vendidos


        figura = grafico.Figure(figsize=(11.4,2.5),dpi=66)
        ax = figura.add_subplot(111)

     
        bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

     

        ax.set_ylabel('quantidade vendida')
        ax.legend(title='produtos')
           
        ax.bar(x,y, color=bar_colors)
        canva =FigureCanvasQTAgg(figura)
        self.grafico_01.addWidget(canva)

    #Grafico faturamento por produto
        #Top 5 faturamento dos produtos
        lista_precos = []
        lista1 = funcoes_produto.listar_prod()
        for produto in lista1:
            lista_precos.append(produto.preco)
        lista2 = funcoes_estoque.listar_estoque()
        lista_prod_quant_vendidos = []
        cont=0
        for estoque in lista2:
            dic = {'id':estoque.id,'nome':estoque.nome,'valor_vendido':estoque.vendidos *lista_precos[cont]}
            cont = cont + 1
            lista_prod_quant_vendidos.append(dic)
        lista_quant_vendidos = []
        lista_nomes_prods = []
        for produtos in lista_prod_quant_vendidos:
            lista_quant_vendidos.append(produtos['valor_vendido'])
            lista_nomes_prods.append(produtos['nome'])
        
        figura02 = grafico.Figure(figsize=(11.4,2.5),dpi=66)
        ax02 = figura02.add_subplot(111)

        bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange']
        

        ax02.set_ylabel('faturamento')
        ax02.legend(title='produtos')
           
        ax02.bar(lista_nomes_prods,lista_quant_vendidos, color=bar_colors)
        

        canva02 =FigureCanvasQTAgg(figura02)
        self.grafico_03.addWidget(canva02)

        #Receita de vendas
        receita = 0
        lista_vendas =funcoes_vendas.listar_vendas()
        for vendas in lista_vendas:
            receita += vendas.valor
        self.valor_receita.setText("R$ "+str(receita))
        #Quantidade de produtos Vendidos
        quantidade_vendida = 0
        lista_estoque = funcoes_estoque.listar_estoque()
        for estoque in lista_estoque:
            quantidade_vendida += estoque.vendidos
        self.valor_quantidade.setText(str(quantidade_vendida))
        ###Configurando o stylesheets
        self.label_dashboard.setStyleSheet('font-size: 22px; color: white;')
        self.valor_receita.setStyleSheet('font-size: 15px; color: white;')
        self.valor_quantidade.setStyleSheet('font-size: 15px; color: white;')
        self.frame_faturamento_prod.setStyleSheet('font-size: 12px; color:black;background-color:#2ef8a0;')
       
            


        
        




    

    

