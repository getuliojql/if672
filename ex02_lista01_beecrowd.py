# -*- coding: utf-8 -*-

def simulate_structure():
    # Função para ler entrada manualmente
    def read_input():
        buffer = ""
        try:
            while True:
                buffer += input() + "\n"
        except EOFError:
            pass
        return buffer

    # Função para dividir texto em linhas manualmente
    def split_lines(data):
        lines = []
        current = ""
        for char in data:
            if char == "\n":
                lines += [current]
                current = ""
            else:
                current += char
        if current:
            lines += [current]
        return lines

    # Função para simular pilha
    def stack_operations(stack, x, operation):
        if operation == "push":
            stack[0] += 1
            stack[stack[0]] = x
        elif operation == "pop":
            if stack[0] > 0:
                return stack[stack[0]]
            return None
        stack[0] -= 1
        return None

    # Função para simular fila
    def queue_operations(queue, x, operation):
        if operation == "enqueue":
            queue[0] += 1
            queue[queue[0]] = x
        elif operation == "dequeue":
            if queue[1] <= queue[0]:
                result = queue[queue[1]]
                queue[1] += 1
                return result
            return None
        return None

    # Função para simular fila de prioridade
    def priority_queue_operations(pq, x, operation):
        if operation == "enqueue":
            pq[0] += 1
            pq[pq[0]] = x
            # Ordena os elementos manualmente
            for i in range(pq[0], 1, -1):
                if pq[i] > pq[i - 1]:
                    pq[i], pq[i - 1] = pq[i - 1], pq[i]
                else:
                    break
        elif operation == "dequeue":
            if pq[0] > 0:
                result = pq[1]
                for i in range(1, pq[0]):
                    pq[i] = pq[i + 1]
                pq[0] -= 1
                return result
            return None
        return None

    # Leitura da entrada
    data = read_input()
    lines = split_lines(data)
    
    results = []
    i = 0

    while i < len(lines):
        n = int(lines[i])
        i += 1

        # Inicializando estruturas
        stack = [0] + [0] * 1000  # Array simulado para pilha
        queue = [0, 1] + [0] * 1000  # Array simulado para fila
        priority_queue = [0] + [0] * 1000  # Array simulado para fila de prioridade
        
        is_stack = True
        is_queue = True
        is_priority_queue = True

        for _ in range(n):
            command = lines[i]
            i += 1

            if command[0] == "1":  # Operação de inserção
                x = int(command[2:])
                if is_stack:
                    stack_operations(stack, x, "push")
                if is_queue:
                    queue_operations(queue, x, "enqueue")
                if is_priority_queue:
                    priority_queue_operations(priority_queue, x, "enqueue")

            elif command[0] == "2":  # Operação de remoção
                x = int(command[2:])
                if is_stack:
                    top = stack_operations(stack, 0, "pop")
                    if top != x:
                        is_stack = False
                if is_queue:
                    front = queue_operations(queue, 0, "dequeue")
                    if front != x:
                        is_queue = False
                if is_priority_queue:
                    highest = priority_queue_operations(priority_queue, 0, "dequeue")
                    if highest != x:
                        is_priority_queue = False

        # Determinando resultado
        possible = is_stack + is_queue + is_priority_queue
        if possible == 0:
            results += ["impossible"]
        elif possible > 1:
            results += ["not sure"]
        elif is_stack:
            results += ["stack"]
        elif is_queue:
            results += ["queue"]
        elif is_priority_queue:
            results += ["priority queue"]

    # Imprimindo os resultados
    for result in results:
        print(result)
