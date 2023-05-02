jogador_X = "X"
jogador_O = "O"

tab = [[" "] * 3, [" "] * 3, [" "] * 3]


def tabuleiro():  # monta o tabuleiro
    for x in range(3):
        print(*tab[x][0], "|", *tab[x][1], "|", *tab[x][2])
        if x < 2:
            print("--+---+--")


def checar_ganhador():  # checa se o tabuleiro está completo e informa o ganhador
    global tab
    win = False
    for i in ("X", "O"):
        # vertical
        if tab[0][0] == tab[0][1] == tab[0][2] == i:
            return i, win is True
        if tab[1][0] == tab[1][1] == tab[1][2] == i:
            return i, win is True
        if tab[2][0] == tab[2][1] == tab[2][2] == i:
            return i, win is True
        # horizontal
        if tab[0][0] == tab[1][0] == tab[2][0] == i:
            return i, win is True
        if tab[0][1] == tab[1][1] == tab[2][1] == i:
            return i, win is True
        if tab[0][2] == tab[1][2] == tab[2][2] == i:
            return i, win is True
        # diagonal
        if tab[0][0] == tab[1][1] == tab[2][2] == i:
            return i, win is True
        if tab[0][2] == tab[1][1] == tab[2][0] == i:
            return i, win is True
        else:
            win = False
    return win


def jogada(jogador):  # faz a jogada
    global tab
    while True:
        lin, col = list(map(int, input(f"Insira linha e coluna de sua jogada, jogador {jogador}: ").split()))
        if (lin or col) not in range(1, 4):
            print("Coordenadas inválidas. Tente novamente.")
        elif tab[lin - 1][col - 1] in ["X", "O"]:
            print("Espaço já preenchido. Tente novamente")
        else:
            tab[lin - 1][col - 1] = jogador
            break


def jogo():
    print("VAI COMEÇAR O JOGO!!")
    tabuleiro()
    rodada = 0
    while rodada <= 9:
        if rodada % 2 == 1:
            jogada(jogador_X)
            rodada += 1
            if checar_ganhador():
                print("++++++++++O jogador X é o vencedor!!++++++++++")
                tabuleiro()
                break
            tabuleiro()
        elif rodada % 2 == 0:
            jogada(jogador_O)
            rodada += 1
            if checar_ganhador():
                print("++++++++++O jogador O é o vencedor!!++++++++++")
                tabuleiro()
                break
            tabuleiro()
    if not checar_ganhador():
        print("----------Deu Velha :(----------")
        print("Tabuleiro final:")
        tabuleiro()

if __name__ == '__main__':
    while True:
        jogo()
        cont = str(input("Deseja jogar novamente? S/N: "))
        if cont in ['n', 'N']:
            break
    print("Jogo finalizado.")
