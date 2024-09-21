# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez
frase = input('Digite uma frase sem acentuação: ').lower().strip()
print(f'A letra A aparece: {frase.count('a')} vezes na frase.')
print(f'A primeira letra A aparece na posição: {frase.find('a')+1}.')
print(f'A última letra A aparece na posição: {frase.rfind('a')+1}.')

