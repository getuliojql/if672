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
    
    def __str__(self) -> str:
        