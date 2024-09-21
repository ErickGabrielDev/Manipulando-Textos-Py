# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome.
nome = input('Digite seu nome completo: ').strip()
print(f'Seu nome tem silva? {'SILVA' in nome.upper()}')