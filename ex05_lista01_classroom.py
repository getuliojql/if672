from ex02_lista01_classroom import SinglyLinkedList

class Queue:
    def __init__(self):
        self.list = SinglyLinkedList() # reutiliza a lista encadeada simples para implementar a fila

    def enqueue(self, element):
        self.list.add_last(element) # adiciona o elemento no final da fila

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty') # se a fila estiver vazia, retorna mensagem de erro
        
        front_element = self.list.get(0) # obtém o elemento do início da lista
        self.list.remove_first() # remove o elemento do início
        
        return front_element # retorna o elemento removido
    
    def front(self):
        if self.is_empty():
            raise IndexError('Queue is empty') # se a fila estiver vazia, retorna mensagem de erro
        
        return self.list.get(0) # retorna o elemento do início
    
    def is_empty(self):
        return self.list.is_empty() # retorna True se a fila estiver vazia e False se não estiver
    
    def size(self):
        return self.list.size() # retorna o tamanho da fila
