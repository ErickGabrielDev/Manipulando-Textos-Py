# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ').strip()
print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
print(f'Seu nome em letras minúsculas é: {nome.lower()}')
print(f'Seu nome ao todo tem: {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem: {nome.find(' ')} letras')