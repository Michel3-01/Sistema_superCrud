class Produto():
    def __init__(self,id,nome_prod,tipo_prod,preco_prod,quant_estoque,excluir=0):
        self.id = id
        self.nome = nome_prod
        self.preco = preco_prod
        self.quant_estoque = quant_estoque
        self.tipo_prod = tipo_prod
        self.excluir = excluir
    def getProd(self):
        return [self.nome,self.tipo_prod,self.preco,self.quant_estoque]