import random
import unicodedata


def remover_caracteres_especiais(string: str) -> str:  # remove caracteres especiais da palavra
    palavra_limpa = unicodedata.normalize('NFD', string)
    return palavra_limpa.encode('ascii', 'ignore').decode('utf8').casefold()


def printar_forca(erros):
    if erros == 0:
        print("+---------+")
        print("|         |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("====")
    if erros == 1:
        print("+---------+")
        print("|         |")
        print("|       ('.') ")
        print("|")
        print("|")
        print("|")
        print("====")
    if erros == 2:
        print("+---------+")
        print("|         |")
        print("|       ('.') ")
        print("|         |")
        print("|         |")
        print("|")
        print("====")
    if erros == 3:
        print("+---------+")
        print("|         |")
        print("|       ('.') ")
        print("|         |\\")
        print("|         |")
        print("|")
        print("====")
    if erros == 4:
        print("+---------+")
        print("|         |")
        print("|       ('.') ")
        print("|        /|\\")
        print("|         |")
        print("|")
        print("====")
    if erros == 5:
        print("+---------+")
        print("|         |")
        print("|       ('.') ")
        print("|        /|\\")
        print("|         |")
        print("|          \\")
        print("====")
    if erros == 6:
        print("+---------+")
        print("|         |")
        print("|       (x.x) ")
        print("|        /|\\")
        print("|         |")
        print("|        / \\")
        print("====")


def jogo():
    with open('palavras.txt', 'r', encoding='utf8') as arquivo:  # abre o arquivo de palavras
        texto = arquivo.read()
        lista_palavras = list(map(str, texto.split(',')))
        palavra = random.choice(lista_palavras).strip()  # escolhe uma palavra aleatoria da lista
    palavra_simples = remover_caracteres_especiais(palavra).upper()  # transforma a palavra em UPPERCASE
    # e remove caracteres especiais

    erro = 0
    enigma = ['_' for _ in range(len(palavra_simples))]  # palavra a ser descoberta
    letras_inseridas = []

    for i in range(len(palavra_simples)):  # adiciona hífen a palavras compostas no enigma
        if palavra_simples[i] == '-':
            enigma[i] = '-'

    print(*enigma)
    while erro < 6:
        while True:
            letra = input('Insira uma letra: ').upper()
            # garante que é apenas uma letra e que não consta na lista das ja inseridas
            if len(letra) == 1 and letra.isalpha() and letra not in letras_inseridas:
                letras_inseridas.append(letra)
                break
            if letra in letras_inseridas:
                print("Letra já inserida anteriormente")
            else:
                print('Tente novamente. Insira uma única letra.')
        if letra not in palavra_simples:  # se a letra nao esta na palavra, aumenta um ponto de erro
            erro += 1
        else:
            for i in range(len(palavra_simples)):  # adiciona a letra correta em sua posição no enigma
                if letra == palavra_simples[i]:
                    enigma[i] = letra.upper()
        if list(palavra_simples.upper()) == enigma:  # se a palavra for completada, o jogo acaba
            print(*enigma)
            print(f"Você venceu!! A palavra era {palavra.upper()}")
            break
        printar_forca(erro)
        print(*enigma)
        print("Já inseridas: ", *letras_inseridas)
    if erro == 6:
        print(f"Você perdeu RIP. A palavra era {palavra.upper()}")


if __name__ == '__main__':
    while True:
        jogo()
        continuar = str(input("Insira qualquer comando para jogar novamente ou 0 para sair: "))
        if continuar == '0':
            break
    print("Jogo finalizado.")
