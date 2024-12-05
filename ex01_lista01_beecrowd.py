class Node:
    def __init__(self, data):
        self.data = data # armazena a informação do nó
        self.next = None # aponta para o próximo nó
        self.prev = None # aponta para o nó anterior

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None # referência para o primeiro nó
        self.size = 0 # contador de candidatos restantes

    def add(self, data):
        new_node = Node(data) # cria um novo nó, com a informação fornecida

        if self.head is None:
            self.head = new_node # se for o primeiro nó a ser criado, torna-se o primeiro

            self.head.next = self.head # aponta para si mesmo
            self.head.prev = self.head # aponta para si mesmo

        else:
            tail = self.head.prev # se não for o primeiro nó a ser criado, o último é o anterior ao primeiro

            tail.next = new_node # o último nó aponta para o novo nó
            new_node.prev = tail # o novo nó aponta para o último nó

            new_node.next = self.head # o novo nó aponta para o primeiro nó
            self.head.prev = new_node # o primeiro nó aponta para o novo nó

        self.size += 1 # incrementa o contador de candidatos

    def remove(self, node):
        if self.size == 0:
            return # se a lista estiver vazia, não há candidato para remover
        
        if self.size == 1:
            self.head = None # se houver apenas um candidato, a lista fica vazia

        else:
            node.prev.next = node.next # o nó anterior aponta para o próximo
            node.next.prev = node.prev # o próximo nó aponta para o anterior

            if node == self.head:
                self.head = node.next # se o nó removido for o primeiro, atualiza o primeiro nó

        self.size -= 1 # decrementa o contador de candidatos

        return node.data # retorna a informação do nó removido

class InputNode:
    def __init__(self, n, k, m):
        self.n = n # número de participantes
        self.k = k # passos no sentido horário
        self.m = m # passos no sentido anti-horário 

        self.next = None # ponteiro para o próximo nó

def josephus_simulation(n, k, m):
    participants = DoublyCircularLinkedList() # inicializa a lista circular

    for i in range(n):
        participants.add(i + 1) # adiciona os números na lista

    clockwise_pointer = participants.head # aponta para o primeiro elemento e vai girar no sentido horário (k)
    counterclockwise_pointer = participants.head.prev # aponta para o último e gira no sentido anti-horário (m)

    result = '' # armazenará a saída formatada

    while participants.size > 0:
        for _ in range(k - 1):
            clockwise_pointer = clockwise_pointer.next # aponta para o candidato que será retirado pela direita

        for _ in range(m - 1):
            counterclockwise_pointer = counterclockwise_pointer.prev # aponta para o que será retirado pela esquerda

        if clockwise_pointer == counterclockwise_pointer: # se o mesmo candidato for escolhido por ambos
            chosen = participants.remove(clockwise_pointer) # retira apenas ele

            result += f'{chosen:3}' # adiciona o número do candidato removido à saída

            clockwise_pointer = clockwise_pointer.next # aponta para o próximo para recomeçar a contagem
            counterclockwise_pointer = counterclockwise_pointer.prev # aponta para o próximo

        else:
            chosen1 = participants.remove(clockwise_pointer) # remove o primeiro candidato e armazena seu número
            chosen2 = participants.remove(counterclockwise_pointer)# faz o mesmo com o segundo candidato

            result += f'{chosen1:3}{chosen2:3}' # adiciona os números dos candidatos à saída

            clockwise_pointer = clockwise_pointer.next # aponta para o próximo no sentido horário
            counterclockwise_pointer = counterclockwise_pointer.prev # aponta para o próximo no anti-horário

        if participants.size > 0:
            result += ', ' # adiciona uma vírgula e um espaço, exceto no final

    return result # retorna a sequência formatada final

def parse_input():
    head = None # ponteiro para o início da lista encadeada
    tail = None # ponteiro para o final

    control = True # variável de controle para o laço

    while control:
        line = input() # recebe a entrada

        if line == '0 0 0':
            control = False # termina quando a '0 0 0' for inserido como entrada

        else: # obtém os números
            n = m = k = ''
            idx = 0

            while idx < len(line) and line[idx] != ' ':
                n += line[idx]
                idx += 1
            idx += 1
            while idx < len(line) and line[idx] != ' ':
                k += line[idx]
                idx += 1
            idx += 1
            while idx < len(line):
                m += line[idx]
                idx += 1

            n, k, m = int(n), int(k), int(m)
            new_node = InputNode(n, k, m) # cria um novo nó com as entradas

            if head is None: # se for o primeiro nó, ajusta os ponteiros de acordo
                head = new_node
                tail = new_node

            else: # se não for, ajusta apenas o ponteiro do final
                tail.next = new_node
                tail = new_node

    return head # retorna o início da lista encadeada

def main():
    inputs = parse_input()

    current = inputs

    while current is not None:
        result = josephus_simulation(current.n, current.k, current.m)
        print(result)
        current = current.next


if __name__ == '__main__':
    main()
