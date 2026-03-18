from time import sleep

def converter_para_decimal(binario):
    decimal = 0
    for chave, valor in enumerate(binario[::-1]):
        if valor == '1':
            decimal += 2**chave
    print(f'\033[31m    — O resultado é: {decimal}\033[0m')
    print('\033[93m|—————————————————————————|FIM|———————————————————————————|\033[0m')

def exibir_entrada(tempo):
    for i in binario:
        print(f' {i}', end='    ', flush=True)
        sleep(tempo)
    print()

def exibir_entrada_invertida(tempo):
    for i in binario[::-1]:
        print(f' {i}', end='    ', flush=True)
        sleep(tempo)
    print()

def exibir_potenciacao(tempo):
    for chave, _ in enumerate(binario[::-1]):
        if chave < len(binario[::-1]) - 1:
            print(f'2^{chave}', end=' + ', flush=True)
            sleep(tempo)
        else:
            print(f'2^{chave}', flush=True)

def exibir_resolver_potenciacao(tempo):
    for chave, _ in enumerate(binario[::-1]):
        if chave < len(binario[::-1]) - 1:
            print(f'{2**chave:03}', end=' + ', flush=True)
            sleep(tempo)
        else:
            print(f'{2**chave:03}', flush=True)

def exibir_isolar_um(tempo):
    for i in binario[::-1]:
        if i == '1':
            print(f' {i}', end='    ', flush=True)
            sleep(tempo)
    print()

def exibir_isolar_potenciacao(tempo):
    for chave, valor in enumerate(binario[::-1]):
        if valor == '1':
            if chave < binario[::-1].rindex('1'):
                print(f'2^{chave}', end=' + ', flush=True)
                sleep(tempo)
            else:
                print(f'2^{chave}', flush=True)

def exibir_isolar_resolver_potenciacao(tempo):
    for chave, valor in enumerate(binario[::-1]):
        if valor == '1':
            if chave < binario[::-1].rindex('1'):
                print(f'{2**chave:03}', end=' + ', flush=True)
                sleep(tempo)
            else:
                print(f'{2**chave:03}', flush=True)

def UI(binario, tempo):
    print('|——————| Conversor de binário para decimal |——————|')
    exibir_entrada(tempo)
    print()
    print('Invertendo as posições do binário...')
    exibir_entrada_invertida(tempo)
    print()
    print('Construindo potenciação...')
    exibir_potenciacao(tempo)
    print()
    print('Resolvendo potencioação...')
    exibir_resolver_potenciacao(tempo)
    print()
    print('Isolando o um...')
    exibir_isolar_um(tempo)
    print()
    print('Isolando potenciação...')
    exibir_isolar_potenciacao(tempo)
    print()
    print('Isolando resolução de potenciação...')
    exibir_isolar_resolver_potenciacao(tempo)
    print()
    print('Retornado resultado da conversão para decimal...')
    converter_para_decimal(binario)

binarios = ['100010011', '10010011','00010001', '00000010',
            '10101010', '101','10010010011', '11111', '111101']

for binario in binarios:
    UI(binario, 0.0)