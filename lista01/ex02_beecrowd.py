# -*- coding: utf-8 -*-

def convert_line_to_integers(input_line): # converte a linha de entrada em inteiros sem usar split
    index_input_line = 0 # índice atual da linha
    input_line_length = 0 # tamanho da linha
    while True: # calcula o tamanho da linha
        if index_input_line < len(input_line):
            input_line_length += 1
            index_input_line += 1
        else:
            break
    index_input_line = 0 # reseta o índice para reuso
    possible_numbers = [0]*2 # array de possíveis números (no máximo 2)
    count_found_integers = 0 # quantos números encontrados
    current_number_string = '' # armazena o número atual em string
    while index_input_line < input_line_length: # percorre a linha caractere por caractere
        current_char = input_line[index_input_line] # caractere atual
        if current_char == ' ': # separador de números
            if current_number_string != '': # se já tem um número acumulado
                number_value = 0 # valor numérico
                index_number = 0 # índice para conversão do número
                number_length = 0 # tamanho do número em caracteres
                while index_number < len(current_number_string): # calcula tamanho do número
                    number_length += 1
                    index_number += 1
                index_number = 0
                is_negative = False # sinaliza se é negativo
                while index_number < number_length: # converte cada dígito
                    char_digit = current_number_string[index_number]
                    if char_digit == '-':
                        is_negative = True
                    else:
                        number_value = number_value*10+(ord(char_digit)-ord('0'))
                    index_number += 1
                if is_negative:
                    number_value = -number_value
                possible_numbers[count_found_integers] = number_value # armazena o número
                count_found_integers += 1
                current_number_string = '' # reseta a string do número
        else:
            current_number_string = current_number_string + current_char # acumula caractere no número
        index_input_line += 1
    if current_number_string != '': # se sobrou um número no final da linha
        number_value = 0
        index_number = 0
        number_length = 0
        while index_number < len(current_number_string):
            number_length += 1
            index_number += 1
        index_number = 0
        is_negative = False
        while index_number < number_length:
            char_digit = current_number_string[index_number]
            if char_digit == '-':
                is_negative = True
            else:
                number_value = number_value*10+(ord(char_digit)-ord('0'))
            index_number += 1
        if is_negative:
            number_value = -number_value
        possible_numbers[count_found_integers] = number_value
        count_found_integers += 1
    output_integers = [0]*count_found_integers # cria array com o tamanho exato dos números encontrados
    idx = 0
    while idx < count_found_integers: # copia números para output_integers
        output_integers[idx] = possible_numbers[idx]
        idx += 1
    return output_integers # retorna a lista de inteiros encontrados

while True: # laço para ler vários casos de teste
    try:
        input_line_n = input() # lê a linha contendo n
    except:
        break # EOF alcançado, sai do loop
    if input_line_n == '':
        break # linha vazia, encerra
    numbers_for_n = convert_line_to_integers(input_line_n) # converte a linha em inteiros
    if len(numbers_for_n) == 0:
        break # não há números, encerra
    number_of_operations = numbers_for_n[0] # n = número de operações

    stack_elements = [0]*1001 # array para simular pilha
    stack_element_count = 0 # topo da pilha
    could_be_stack = True # ainda pode ser pilha

    queue_elements = [0]*1001 # array para simular fila
    queue_start_index = 0 # início da fila
    queue_end_index = 0 # fim da fila
    could_be_queue = True # ainda pode ser fila

    priority_queue_elements = [0]*1001 # array para simular fila de prioridade
    priority_queue_size = 0 # tamanho da fila de prioridade
    could_be_priority_queue = True # ainda pode ser fila de prioridade

    op_index = 0 # índice das operações
    while op_index < number_of_operations:
        input_line_command = input() # lê a linha de comando
        command_numbers = convert_line_to_integers(input_line_command) # converte comando em inteiros
        if command_numbers[0] == 1: # operação de inserir
            inserted_value = command_numbers[1] # valor a inserir
            if could_be_stack: # insere na pilha
                stack_elements[stack_element_count] = inserted_value
                stack_element_count += 1
            if could_be_queue: # insere na fila
                queue_elements[queue_end_index] = inserted_value
                queue_end_index += 1
            if could_be_priority_queue: # insere na pq
                priority_queue_elements[priority_queue_size] = inserted_value
                priority_queue_size += 1
        else: # operação de remover
            expected_value = command_numbers[1] # valor esperado a remover
            if could_be_stack:
                if stack_element_count == 0: # pilha vazia
                    could_be_stack = False
                else:
                    top_value = stack_elements[stack_element_count-1] # valor do topo
                    if top_value == expected_value:
                        stack_element_count -= 1 # remove topo
                    else:
                        could_be_stack = False
            if could_be_queue:
                if queue_start_index == queue_end_index: # fila vazia
                    could_be_queue = False
                else:
                    front_value = queue_elements[queue_start_index] # valor da frente
                    if front_value == expected_value:
                        queue_start_index += 1 # remove da frente
                    else:
                        could_be_queue = False
            if could_be_priority_queue:
                if priority_queue_size == 0: # pq vazia
                    could_be_priority_queue = False
                else:
                    max_val = -999999
                    max_pos = -1
                    idx_pq = 0
                    while idx_pq < priority_queue_size: # busca o maior elemento
                        if priority_queue_elements[idx_pq] > max_val:
                            max_val = priority_queue_elements[idx_pq]
                            max_pos = idx_pq
                        idx_pq += 1
                    if max_val == expected_value:
                        # substitui o removido pelo último da pq
                        priority_queue_elements[max_pos] = priority_queue_elements[priority_queue_size-1]
                        priority_queue_size -= 1
                    else:
                        could_be_priority_queue = False
        op_index += 1

    count_structures_possible = 0 # conta quantas estruturas ainda possíveis
    if could_be_stack:
        count_structures_possible += 1
    if could_be_queue:
        count_structures_possible += 1
    if could_be_priority_queue:
        count_structures_possible += 1

    # imprime o resultado de acordo com quantas estruturas possíveis sobraram
    if count_structures_possible == 0:
        print("impossible")
    elif count_structures_possible > 1:
        print("not sure")
    else:
        if could_be_stack:
            print("stack")
        elif could_be_queue:
            print("queue")
        else:
            print("priority queue")
