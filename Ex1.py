"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""

ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']

if __name__ == '__main__':
    vendas = []
    for ilha in ilhas:
        vendas.append((float(input(f'Insira as vendas para {ilha} '))))
    print(f'Vendas={vendas}')

    menor = vendas[0]
    maior = vendas[0]
    for x in range(1, len(vendas)):
        if vendas[x] < menor:
            menor = vendas[x]
        if vendas[x] > maior:
            maior = vendas[x]
    print(f'O maior valor inserido é {maior} e o menor valor é {menor}.')

    total = 0
    for v in vendas