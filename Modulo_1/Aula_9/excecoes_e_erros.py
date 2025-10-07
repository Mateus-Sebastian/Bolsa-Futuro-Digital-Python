try:
    numero_int = int(input('Digite um número inteiro: '))

    if numero_int % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')

except ValueError:
    print('Erro na execução: não é um número inteiro válido.')