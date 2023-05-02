class JogoDaVelha:
    def __init__(self):
        self.jogador_x = 'X'
        self.jogador_o = "O"
        self.tabuleiro = [[" "] * 3, [" "] * 3, [" "] * 3]

    def montar_tabuleiro(self):  # monta o tabuleiro
        for x in range(3):
            print(*self.tabuleiro[x][0], "|", *self.tabuleiro[x][1], "|", *self.tabuleiro[x][2])
            if x < 2:
                print("--+---+--")

    def checar_ganhador(self):  # checa se o tabuleiro está completo e informa o ganhador
        win = False
        for i in ("X", "O"):
            # vertical
            if self.tabuleiro[0][0] == self.tabuleiro[0][1] == self.tabuleiro[0][2] == i:
                return i, win is True
            if self.tabuleiro[1][0] == self.tabuleiro[1][1] == self.tabuleiro[1][2] == i:
                return i, win is True
            if self.tabuleiro[2][0] == self.tabuleiro[2][1] == self.tabuleiro[2][2] == i:
                return i, win is True
            # horizontal
            if self.tabuleiro[0][0] == self.tabuleiro[1][0] == self.tabuleiro[2][0] == i:
                return i, win is True
            if self.tabuleiro[0][1] == self.tabuleiro[1][1] == self.tabuleiro[2][1] == i:
                return i, win is True
            if self.tabuleiro[0][2] == self.tabuleiro[1][2] == self.tabuleiro[2][2] == i:
                return i, win is True
            # diagonal
            if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == i:
                return i, win is True
            if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == i:
                return i, win is True
            else:
                win = False
        return win

    def fazer_jogada(self, jogador):  # faz a jogada
        while True:
            try:
                lin, col = list(map(int, input(f"Insira linha e coluna de sua jogada, jogador {jogador}: ").split()))
                if lin or col not in range(1, 4):
                    print("Coordenadas inválidas. Tente novamente.")
                if self.tabuleiro[lin - 1][col - 1] in ["X", "O"]:
                    print("Espaço já preenchido. Tente novamente")
                else:
                    self.tabuleiro[lin - 1][col - 1] = jogador
                    break
            except ValueError:
                print("Coordenadas inválidas. Tente numeros de 1 a 3 separados por espaço.")

    def jogar(self):
        print("VAI COMEÇAR O JOGO!!")
        print("Insira o numero da linha e da coluna separados por espaço. As linhas e colunas possuem numeros 1, 2 e 3."
              " BOM JOGO!")
        self.montar_tabuleiro()
        rodada = 0
        while rodada <= 9:
            if rodada % 2 == 1:
                self.fazer_jogada(self.jogador_x)
                rodada += 1
                if self.checar_ganhador():
                    print("\n++++++++++O jogador X é o vencedor!!++++++++++")
                    self.montar_tabuleiro()
                    break
                self.montar_tabuleiro()
            elif rodada % 2 == 0:
                self.fazer_jogada(self.jogador_o)
                rodada += 1
                if self.checar_ganhador():
                    print("\n++++++++++O jogador O é o vencedor!!++++++++++")
                    self.montar_tabuleiro()
                    break
                self.montar_tabuleiro()
        if not self.checar_ganhador():
            print("\n----------Deu Velha :(----------")
            print("Tabuleiro final:")
            self.montar_tabuleiro()


if __name__ == '__main__':
    jogo = JogoDaVelha()
    while True:
        jogo.jogar()
        cont = str(input("Deseja jogar novamente? S/N: "))
        if cont.upper() == 'N':
            break
    print("Jogo finalizado.")
