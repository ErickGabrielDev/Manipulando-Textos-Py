# Crie um programa que leia um nome de uma cidade e diga se ela começa ou nao com o nome 'santo'.

cidade = input('Digite o nome de uma cidade: ').strip()
print(cidade[:5].upper() == 'SANTO')
