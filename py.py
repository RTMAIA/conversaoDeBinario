from time import sleep


def converter_binario_para_decimal(b):
    valor_decimal = 0

    sleep(1)
    print()
    print('Convertendo Binário para Decimal...')
    print()
    sleep(0.4)
    print('Obtendo binário...')
    sleep(0.4)

    for i in list(b):
        print(f' {i}', end='    ', flush=True)
        sleep(0.2)

    sleep(0.4)
    print('\n')
    print('Invertendo as posições do binário...')
    sleep(0.2)
    for i in list(b[::-1]):
        print(f' {i}', end='    ', flush=True)
        sleep(0.2)

    print('\n')
    print('Criando calculo...')
    sleep(0.2)
    for c, v in enumerate(b[::-1]):
        if c < len(b) - 1:
            print(f'2^{c}', end=' ', flush=True)
            print('+ ', end='')
            sleep(0.4)
        else:
            print(f'2^{c}', end='  ') 

    print()
    sleep(1)
    print()
    print('Removendo os Zeros...')
    sleep(0.4)

    for i in list(b):
            if i == "1":
                print(f' {i}', end='    ', flush=True)
                sleep(0.2)

    print()

    for c, v in enumerate(b[::-1]):
        if v == '1':
            if c < b[::-1].rfind("1"):
                print(f'2^{c}', end=' ', flush=True)
                print('+ ', end='')
                sleep(0.2)
            else:
                print(f'2^{c}', end='  ') 

    print()

    for chave, valor in enumerate(b[::-1]):
        if valor == '1':
            if chave < b[::-1].rfind("1"):
                print(f'{2**chave:0>2}', end='  ', flush=True)
                sleep(0.2)
                print('+ ', end='')
                sleep(0.2)
            else:
                print(f'{2**chave:0>2}', end='  ')
                
    print('\n')
    sleep(0.4)
    print('Fazendo soma...')
    sleep(0.4)
    for chave, valor in enumerate(b[::-1]):
        if valor == '1':
            valor_decimal += 2**chave
    sleep(1)
    print(f'\033[91m    — Resultado decimal: {valor_decimal}\033[0m', flush=True)
    print()


converter_binario_para_decimal("10010011")
print('''
———————————————————————————————————————————————————————————————————————————
''')
converter_binario_para_decimal("00010001")
print('''
———————————————————————————————————————————————————————————————————————————
''')
converter_binario_para_decimal("00000010")
print('''
———————————————————————————————————————————————————————————————————————————
''')
converter_binario_para_decimal("10101010")
print('''
———————————————————————————————————————————————————————————————————————————
''')
converter_binario_para_decimal("101")
print('''
———————————————————————————————————————————————————————————————————————————
''')
converter_binario_para_decimal("10010010011")
print('''
———————————————————————————————————————————————————————————————————————————
''')
converter_binario_para_decimal("11111")
print('''
———————————————————————————————————————————————————————————————————————————
''')
converter_binario_para_decimal("111101")
print('''
———————————————————————————————————————————————————————————————————————————
''')