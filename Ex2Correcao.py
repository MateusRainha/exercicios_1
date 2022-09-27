"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inserido a frase apresente:
 - Qual é o comprimento da frase inserida (incluindo espaços)
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""

if __name__ == '__main__':
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    frase = input('Insira uma frase: ')
    x = 0
    for c in frase:
        x += 1

    print(f'A frase tem {x} caracteres - {len(frase)}')

    num_vogais = 0
    for c in frase:
        if c in vogais:
            num_vogais += 1
    print(f'A frase tem {num_vogais} vogais.')

    nova_frase = frase.split(' ')
    print(nova_frase)
    print(len(nova_frase))


    maiusculas = 0
    minusculas = 0
    for c in frase:
        if c == c.upper():
            maiusculas += 1
        if c == c.lower():
            minusculas += 1

    print(f'A frase tem {maiusculas} letras maiúsculas e {minusculas} minúsculas.')

