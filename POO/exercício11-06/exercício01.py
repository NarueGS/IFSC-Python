class Conta:
    def __init__(self,data, num, kiloW, valor, dataPagamento, media):
        self.__leitura = data
        self.__numeroLeitura = num
        self.__kiloW = kiloW
        self.__valorConta = valor
        self.__dataPagamento = dataPagamento
        self.__mediaConsumo = media
    def __str__(self):
        return str("Data da leitura: {}\n Número da leitura: {}\n Quantia de KW gasto no mês: {}\n Valor da Conta: {}\n Data de pagamento: {}\n Média de Consumo: {}\n".format(self.leitura,self.numeroLeitura,self.kiloW,self.valorConta,self.dataPagamento,self.mediaConsumo))
    @property
    def leitura(self):
        return self.__leitura
    @leitura.setter
    def leitura(self,value):
        self.__leitura = value
    @property
    def numeroLeitura(self):
        return self.__numeroLeitura
    @numeroLeitura.setter
    def numeroLeitura(self,value):
        self.__numeroLeitura = value
    @property
    def kiloW(self):
        return self.__kiloW
    @kiloW.setter
    def kiloW(self,value):
        self.__kiloW = value
    @property
    def valorConta(self):
        return self.__valorConta
    @valorConta.setter
    def valorConta(self,value):
        self.valorConta = value
    @property
    def dataPagamento(self):
        return self.__dataPagamento
    @dataPagamento.setter
    def dataPagamento(self, value):
        self.__dataPagamento = value
    @property
    def mediaConsumo(self):
        return self.__mediaConsumo
    @mediaConsumo.setter
    def mediaConsumo(self,value):
        self.__mediaConsumo = value
    def __gt__(self,other):
        print("A")
        a = self.__kiloW
        b = other.__kiloW
        return a > b
    def __lt__(self,other):
        print("Teste menor {} - maior {} ".format(self.kiloW,other.kiloW))
        a = self.kiloW
        b = other.kiloW
        return a < b
Contas = []
for x in range(3):
    valor1 = input("Digite a data de leitura (com as barras) ")
    valor2 = input("Digite o número de leitura  " )
    valor3 = float(input("Digite o consumo de KW  " ))
    valor4 = float(input("Digite o valor da conta  " ))
    valor5 = input("Digite a data de pagamento (com as barras)  ")
    valor6 = input("Digite a média de consumo   ")
    ContaCriada = Conta(valor1,valor2,valor3,valor4,valor5,valor6)
    Contas.append(ContaCriada)

print(max(Contas))
print(min(Contas))
