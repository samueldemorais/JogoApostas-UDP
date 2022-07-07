#CODIGO SEM CONEXÃO SERVIDOR-CLIENTE
from this import s
from aposta import apostador, apostas
numeros_apostados = []
dinheiro = []
nomes = []
pontos = []

def cadastrar(nome):
    print (f'=========oi {nome}, bem vindo a MEGA-SENA LSD=========')
    
    usuario = apostador(input('qual o seu nome de apostador?'), 
    int(input("qual o valor da sua aposta?")))
    dinheiro.append(usuario.aposta)
    temp = usuario.apostar()
    nomes.append(usuario.nome)
    numeros_apostados.append(temp)
    print("aposta cadastrada com sucesso")
    

def jogar():
    if len(nomes) >= 2:
        jogo = apostas(apostador)
        ganha = jogo.SortearNumeros()
        print(f'os números sorteados são: {ganha}')
        num = 0 
        for c in range(len(numeros_apostados)):
            cont = 0
            for i in range(3):
                for j in range(len(numeros_apostados[0])):
                    if ganha[i] == numeros_apostados[num][j]:
                        cont += 1
            num += 1    
            pontos.append(cont)
    else: print('número de apostadores insuficiente :(')



def exibir_resultador():
    premio = 0

    for i in range(len(dinheiro)):
        premio += dinheiro[i]


    max_value = None
    max_idx = None

    for idx, num in enumerate(pontos):
        if (max_value is None or num > max_value):
            max_value = num
            max_idx = idx
    print(f'o ganhador do jogo foi {nomes[max_idx]}, acertando {max_value} números e levando o prêmio de {premio} reais')

def reset(): 
    numeros_apostados.clear()
    dinheiro.clear()
    nomes.clear()
    pontos.clear()


while True:
    
    tokens = input("\nLSD>>>").upper().split()
    print()
    command = tokens[0]

    if command == "SAIR":
        break
    
    if command == "CAD":
        cadastro = cadastrar(tokens[1])
            
    elif command == "PLAY":
        game =  jogar()
    
    elif command == "SHOW":
        results = exibir_resultador()

    elif command == "RESET":
        resetar = reset()
    else:
        print("Digite um comando válido.")

print("\n---Encerramento do programa---")