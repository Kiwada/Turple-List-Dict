#Crie um programa que vai gerar cinco números
#leatórios e colocar em uma tuplaDepois disso, 
# mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na tupla.


from random import randint


numeros = (randint (1,101)),(randint (1,101)),(randint (1,101)),(randint (1,101)),(randint (1,101))
print('Os valores sorteados foram :' ,end='')
for n in numeros:
    print(f' {n}' , end='')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')