#classe Vendas realizadas

class Vendas():
    def __init__(self,id_venda,tipo_venda,valor_total,data,horario):
        self.id = id_venda
        self.tipo = tipo_venda
        self.valor = valor_total
        self.data = data
        self.horario = horario
    def getVenda(self):
        return [self.tipo, self.valor, self.data, self.horario]