alfabeto = {' ':32, '!':33, '"':34, '#':35, '$':36, '%':37, '&':38, "'":39, '(':40,
                ')':41, '*':42, '+':43, ',':44, '-':45, '.':46, '/':47, 'A':65, 'B':66,
                'C':67, 'D':68,'E': 69, 'F':70, 'G':71, 'H':72, 'I':73, 'J':74,
                'K':75, 'L':76, 'M':77, 'N':78, 'O':79, 'P':80, 'Q':81, 'R':82,
                'S':83, 'T':84, 'U':85, 'V':86, 'W':87, 'X':88,'Y':89, 'Z':90,
                'a':97, 'b':98, 'c':99, 'd':100, 'e':101, 'f':102,'g':103, 'h':104,
                'i':105, 'j':106, 'k':107, 'l':108, 'm':109,'n':110, 'o':111, 'p':112,
                'q':113, 'r':114, 's':115, 't':116,'u':117, 'v':118, 'w':119, 'x':120,
                'y':121, 'z':122}


def converter_letra_binario(texto):

    binario = ''

    for i in texto:
        if i in alfabeto:
            resto_temp = ''
            divisao = alfabeto[i]
            while divisao >= 1:
                resto_temp += str(divisao % 2)
                divisao //= 2

            if len(resto_temp) < 8:
                resto_temp += '0' * (8 - len(resto_temp))
            binario += resto_temp[::-1] + ' '
    return binario

def converter_binario_texto(binario):
    
    texto = ''

    bin = binario.split(' ')
    for i in bin:
        decimal = 0
        for chave, valor in enumerate(i[::-1]):
            if valor == '1':
                decimal += 2**chave
        for c, v in alfabeto.items():
            if decimal == v:
                texto += c
    return texto


binario = converter_letra_binario('oi, eu so rafael teixeira maia')
print(binario)
texto = converter_binario_texto(binario)
print(texto)