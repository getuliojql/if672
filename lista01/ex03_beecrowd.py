# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

def read_line():  # Lê uma linha de entrada
    read_line_str = ''  # Armazena a linha lida
    temp_char = ''  # Caractere temporário
    while True:  # Loop até conseguir ler uma linha
        try:
            temp_char = input()  # Lê a linha do usuário
            read_line_str = temp_char  # Armazena no variável final
            break
        except:
            return None  # Caso não consiga ler, retorna None
    if read_line_str == '':  # Se a linha for vazia
        return ''  # Retorna vazio
    return read_line_str  # Retorna a linha lida

def parse_integers(input_string):  # Extrai inteiros de uma string
    idx = 0  # Índice de iteração
    str_length = 0  # Tamanho da string
    for char in input_string:  # Conta o tamanho total da string
        str_length += 1
    numbers = [0]*2  # Array inicial para dois inteiros
    count = 0  # Contador de quantos inteiros foram encontrados
    num_str = ''  # String temporária para formar o número
    while idx < str_length:  # Percorre cada caractere da string
        char = input_string[idx]  # Caractere atual
        if char == ' ':  # Se encontrar um espaço, converte num_str em inteiro
            if num_str != '':  # Se já houver conteúdo numérico
                value = 0  # Valor numérico final
                negative = False  # Flag para número negativo
                num_size = 0  # Tamanho da string numérica
                for c in num_str:
                    num_size += 1
                j = 0
                while j < num_size:  # Converte cada dígito em inteiro
                    digit = num_str[j]
                    if digit == '-':
                        negative = True
                    else:
                        value = value*10+(ord(digit)-ord('0'))
                    j += 1
                if negative:
                    value = -value
                numbers[count] = value
                count += 1
                num_str = ''
        else:
            num_str = num_str + char  # Constrói o número
        idx += 1
    if num_str != '':  # Caso tenha sobrado algum número após o final da string
        value = 0
        negative = False
        num_size = 0
        for c in num_str:
            num_size += 1
        j = 0
        while j < num_size:
            digit = num_str[j]
            if digit == '-':
                negative = True
            else:
                value = value*10+(ord(digit)-ord('0'))
            j += 1
        if negative:
            value = -value
        numbers[count] = value
        count += 1
    result = [0]*count
    i = 0
    while i < count:
        result[i] = numbers[i]
        i += 1
    return result

while True:  # Loop principal de leitura
    initial_line = read_line()  # Lê primeira linha
    if initial_line is None or initial_line == '':
        break  # Se não houver mais linhas, encerra
    initial_values = parse_integers(initial_line)  # Extrai valores inteiros
    if len(initial_values) < 2:
        break  # Se não houver 2 valores, encerra
    num_cars = initial_values[0]  # Número de motoristas
    num_spots = initial_values[1]  # Número de vagas
    if num_cars == 0 and num_spots == 0:
        break  # Condição de parada
    arrival_times = [0]*num_cars  # Lista para tempos de chegada
    departure_times = [0]*num_cars  # Lista para tempos de saída
    i = 0
    while i < num_cars:
        car_line = read_line()  # Lê linha com chegada e saída do carro
        car_values = parse_integers(car_line)  # Extrai inteiros da linha
        arrival_times[i] = car_values[0]  # Tempo de chegada
        departure_times[i] = car_values[1]  # Tempo de saída
        i += 1
    stack_departures = [0]*num_spots  # Pilha para armazenar tempos de saída
    stack_top = 0  # Aponta para o topo da pilha
    possible = True  # Flag para indicar se é possível acomodar todos os carros
    i = 0
    while i < num_cars:
        current_arrival = arrival_times[i]  # Tempo de chegada do carro atual
        current_departure = departure_times[i]  # Tempo de saída do carro atual
        # Remove da pilha todos os carros que já saíram antes ou no momento da chegada atual
        remove_flag = True
        while remove_flag and stack_top > 0:
            if stack_departures[stack_top-1] <= current_arrival:
                stack_top -= 1
            else:
                remove_flag = False
        if stack_top < num_spots:
            stack_departures[stack_top] = current_departure
            stack_top += 1
        else:
            possible = False
            break
        i += 1
    if possible:
        print("Sim")  # Se couberam todos os carros, imprime "Sim"
    else:
        print("Nao")  # Caso contrário, imprime "Nao"
