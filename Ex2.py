"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Qual é o comprimento da frase inserida (incluindo espaços)
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""

def conta_capitais():
    contar_ma = 0
    for n in capitais:
        if n.isupper():
            contar_ma += 1
    return contar_ma


def conta_minusculas(minusculas):
    contar_mi = 0
    for n in minusculas:
        if n.islower():
            contar_mi += 1
    return contar_mi


def frase_invertida(frase):
    return frase[::-1]


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        n_vogais = 0
        n_numeros = 0

        frase = input('Insira uma frase: ')
        print(f'O comprimento da frase é: {len(frase)}')

        nl = frase.split(' ')
        print(f'A frase tem {len(nl)} palavras')

        vogais = "aeiou"
        numeros = "0123456789"
        for n in frase:
            if n in numeros:
                n_numeros += 1

        for char in frase:
            if char in vogais:
                n_vogais += 1

        print(f'A frase tem {n_vogais} vogais')

        print(f'A frase tem {conta_capitais(frase)} minusculas')

        print(f' A frase tem {n_numeros} numeros')

        print(f' A frase invertida é: {frase_invertida(frase)}')

        continuar = input('Quer continuar? [s , n]')

    print(f'Adeus!')