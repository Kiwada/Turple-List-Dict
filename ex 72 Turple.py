#crie um programa que tenhoa uma tupla totalmente preenchida 
#com uma contagem por extenso , de zero ate vinte.Seu programa
#deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo 
def escreva(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}  ')
    print('='*tam)







cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <=20:
            break
        print('Número inválido. ', end='')
    escreva(f'O número digitado foi {cont[num]}.')
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if resp == 'N'or int:
        break
escreva('PROGRAMA ENCERRADO')




        


