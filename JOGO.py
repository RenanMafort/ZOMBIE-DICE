import random
import time

# Definicao dos dados (C - cerebro, T - tiro e P - passos)
# Dados verdes (6 dados)
dadoVerde = {0: "Cerebro", 1: "Passos", 2: "Cerebro", 3: "Tiro", 4: "Passos", 5: "Cerebro"}

# Dados amarelos (4 dados)
dadoAmarelo = {0: "Tiro", 1: "Passos", 2: "Cerebro", 3: "Tiro", 4: "Passos", 5: "Cerebro"}

# Dados vermelhos (3 dados)
dadoVermelho = {0: "Tiro", 1: "Passos", 2: "Tiro", 3: "Cerebro", 4: "Passos", 5: "Tiro"}


def sorteia_lado():
    lado = random.randrange(6)
    return lado


def sorteia_cor():
    color = random.randrange(13)

    if color < 6:
        return "verde"
    elif color >= 6 and color < 10:
        return "amarelo"
    elif color >= 10 and color < 13:
        return "vermelho"


def rolar_dado():
    dado = sorteia_cor()
    lado = sorteia_lado()
    if dado == "verde":
        return (dado, dadoVerde[lado])
    elif dado == "amarelo":
        return ("AMARELO", dadoAmarelo[lado])
    elif dado == "vermelho":
        return (dado, dadoVermelho[lado])




cerebro = 0
tiro = 0
passos = 0
n = 0


def girar_dados():
    print("Iniciando o jogo...")
    time.sleep(3)

    print("Rolando dado...")
    for i in reversed(range(1, 4)):
        time.sleep(1.5)
        print("%s\r" % i)
        time.sleep(1)

    global cerebro
    global tiro
    global passos
    for i in range(0, 3):
        dado_cor, resultado = rolar_dado()
        if resultado == "Cerebro":
            cerebro += 1
        elif resultado == "Tiro":
            tiro += 1
        elif resultado == "Passos":
            passos += 1
        print("Dado: %s e obteve %s " % (dado_cor, resultado))
    print("Cerebro: %s\nTiro: %s\nPassos: %s\n " % (cerebro, tiro, passos))



print("Bem vindo ao jogo Zombie Dice!!!")

numberPlayer=0
while numberPlayer < 2:
    numberPlayer=int(input("INFORME O NUMERO DE JOGADORES: "))

    if numberPlayer < 2:
        print("AVISO! É NECESSARIO NO MINIMO 2 JOGADORES!\n")


listaJogadores = []
for i in range(numberPlayer):
    namePlayer = input("Digite o nome do " + str(i+1) + "° jogador: ")
    listaJogadores.append(namePlayer)

currentPlayer = 0
while True:

    print("Jogador %s irá começar o jogo!" % listaJogadores[currentPlayer])

    girar_dados()
    Continuarjogo =input("VOCÊ DESEJA CONTNUAR JOGANDO? sim / nao: ")
    if Continuarjogo =="nao":
        currentPlayer +=1
        cerebro = 0
        tiro = 0
        passos = 0

        if currentPlayer == len(listaJogadores):
            print("FINALIZANDO O JOGO...")
            break









###########


