#Código do cliente LSD
import socket
from aposta import apostador, apostas
import threading
import sys

YELLOW = '\033[93m' 
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def sair():
    sair_programa = 'SAIR'
    udp.sendto(sair_programa.encode(), servidor)

def cadastrar(nome):
    '''Método em que o usuário digita os dados, os quais são concatenados e enviados para o servidor'''

    print (f'{REVERSE}===========oi {nome}, bem vindo a MEGA-SENA LSD==========={RESET}')
    A = input('qual o seu nome de apostador?')
    B = input("qual o valor da sua aposta?")
    C = input("Informe a 1° dezena:")
    D = input("Informe a 2° dezena:")
    E = input("Informe a 3° dezena:")
    F = input("Informe a 4° dezena:")
    G = input("Informe a 5° dezena:")
    dados = "DADOS" + " " + A + "," + B + "," + C + "," + D + "," + E + "," + F + "," + G
    udp.sendto(dados.encode(), servidor)
    #msg_servidor, serv = udp.recvfrom(1024)
    #print(msg_servidor.decode())
        
print(f'{REVERSE}============ LISTA DE COMANDO ============={RESET}'
 f'\n{BOLD}CAD   ---- Cadastrar novo usuário'
  f'\nPLAY  ---- jogar na Mega-sena LSD '
  f'\nSHOW  ---- Mostrar os resultados '
  f'\nRESET ---- resetar jogo '
  f'\nSAIR  ---- encerrar o programa{RESET}')


def recebimento():
    '''função que permite o recebimento de dados do servidor e o tratamento desses dados'''
    while True:
        #print('Lendo:', udp.getsockname())
        msg_servidor, servidor = udp.recvfrom(1024)
        #print('Recebi:', msg_servidor.decode())
        mensagem_servidor = msg_servidor.decode().split(",")
        results = mensagem_servidor[0].split()
        if results[0] == "ERROR":
           print(f'{RED}- {mensagem_servidor[0]}{RESET}')
        if results[0] == "OK":
           print(f'{GREEN}+ {mensagem_servidor[0]}{RESET}')

        if mensagem_servidor[0] == "SAIR":
            print(f"{YELLOW}Obrigado por jogar com a gente :){RESET}")
            sys.exit()
        if mensagem_servidor[0] == "ERROR DEBORA":
            print(f"{YELLOW}Não há apostadores suficentes{RESET}")

        if mensagem_servidor[0] == "ERROR LOUISE":
            print(f"{YELLOW}Comando digitado não é reconhecido{RESET}")

        if mensagem_servidor[0] == "ERROR WAGNER":
            print(f"{YELLOW}Pontuação Máxima foi 0 e não houve ganhador{RESET}")

        if mensagem_servidor[0] == "OK JUNIOR":
            print(f"{YELLOW}O jogo foi resetado com sucesso{RESET}")

        if mensagem_servidor[0] == "OK GUSTAVO":
            print(f"{YELLOW}Números sorteados: {mensagem_servidor[1:]}{RESET}")

        if mensagem_servidor[0] == "OK SAMUEL":
            print(f"{REVERSE}============RESULTADO============={RESET}")
            print(f'{BOLD}ganhador:{CYAN}{mensagem_servidor[1]}{RESET}')
            print(f'{BOLD}pontuação:{CYAN}{mensagem_servidor[2]}{RESET}')
            print(f'{BOLD}prêmio total:{CYAN}{mensagem_servidor[3]} reais{RESET}')

        if mensagem_servidor[0] == "OK LEONIDAS":
            print(f"{YELLOW}Cadastro realizado com sucesso{RESET}")
        

def envio():
    '''função que trata a mensagem digitada pelo usário e envia para o servidor'''
    while True:
        msg = input()
        if msg:
            mensagem = msg.split()
            command = mensagem[0].upper()
            if command == "CAD":
                cadastrar(mensagem[1])
            if command == "SAIR":
                udp.sendto(msg.encode(), servidor)
                sys.exit()

            else:
                udp.sendto(msg.encode(), servidor)
        else: 
            print('Digite algum comando')


HOST = '127.0.0.1'
PORT = 40000

#deixando o ip dinâmico para conexões em máquinas diferentes na mesma rede
if len(sys.argv) > 1:
    HOST = sys.argv[1]

cliente = ("0.0.0.0", 0)
servidor = (HOST, PORT)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(cliente)
udp.connect(servidor)


#criação e iniciação das threads
thread_recebimento = threading.Thread(target = recebimento)
thread_recebimento.start()
thread_envio = threading.Thread(target = envio)
thread_envio.start()

