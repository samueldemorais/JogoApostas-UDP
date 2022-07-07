import random;

class apostas:
    """Classe que define as apostas"""
    def __init__(self, jogador):
        self.jogador = jogador 


    def SortearNumeros(self):
        '''método para sortear os números'''
        sorteados = []
        for aux in range(5):
            sorteio = random.randint(10, 30)
            while sorteio in sorteados:
                sorteio = random.randint(10, 30)
            sorteados.append(sorteio)
        return sorteados 

class apostador:
    '''classe que define os apostadores'''
    def __init__(self, nome, aposta, cliente):
        self.nome = nome
        self.aposta = aposta
        self.cliente = cliente
        

    def imprimir(self):
        print(apostas)