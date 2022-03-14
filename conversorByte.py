# CONVERTER BITS DECIMAIS PARA BINÁRIO E HEXADECIMAL
from bases import base_binarios as base_binarios



def bin_to_decimal(binario):
    """Função para realizar a conversão de um número binário para decimal. Limite de 32 bits.

    Args:
        binario (str): string.
    """

    # ETAPA 1: LIMITANDO OS BITS
    if len(binario) > 32:
        raise ValueError('O número de bits ultrapassou o limite de 32 bits.')

    # ETAPA 2: VERIFICAR SE OS ELEMENTOS SÃO BINÁRIOS
    bin = []
    for digit in binario:
        if digit == ' ':
            continue
        else:
            bin.append(int(digit))
    
    for i in range(len(bin)):
        if bin[i] not in (0, 1):
            raise ValueError('Foi encontrado um valor que não corresponde a um valor binário!')

    # ETAPA 3: VERIFICAR OS ESPAÇOS VAZIOS E COMPLETAR
    while len(bin) % 4 != 0:
        bin.insert(0, 0)

    # ETAPA 4: REALIZANDO AS CONVERSÕES
    dec = 0
    if len(bin) > 28:
        x = 0
        for i in range(len(bin)):
            if bin[i] == 1:
                dec += base_binarios[x] * bin[i]
            x += 1
    elif len(bin) > 24:
        x = 4
        for i in range(len(bin)):
            if bin[i] == 1:
                dec += base_binarios[x] * bin[i]
            x += 1
    elif len(bin) > 20:
        x = 8
        for i in range(len(bin)):
            if bin[i] == 1:
                dec += base_binarios[x] * bin[i]
            x += 1
    elif len(bin) > 16:
        x = 12
        for i in range(len(bin)):
            if bin[i] == 1:
                dec += base_binarios[x] * bin[i]
            x += 1
    elif len(bin) > 12:
        x = 16
        for i in range(len(bin)):
            if bin[i] == 1:
                dec += base_binarios[x] * bin[i]
            x += 1
    elif len(bin) > 8:
        x = 20
        for i in range(len(bin)):
            if bin[i] == 1:
                dec += base_binarios[x] * bin[i]
            x += 1
    elif len(bin) > 4:
        x = 24
        for i in range(len(bin)):
            if bin[i] == 1:
                dec += base_binarios[x] * bin[i]
            x += 1
    else:
        x = 28
        for i in range(len(bin)):
            if bin[i] == 1:
                dec += base_binarios[x] * bin[i]
            x += 1

    # ETAPA 5: RETORNANDO O RESULTADO
    print(f'{bin} to decimal = {dec}')
