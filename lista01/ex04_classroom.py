from lista01.ex02_classroom import SinglyLinkedList

class Stack:
    def __init__(self):
        self.list = SinglyLinkedList() # reutiliza a lista encadeada simples para implementar a pilha

    def push(self, element):
        self.list.add_first(element) # adiciona o elemento no topo da pilha

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty') # se a pilha estiver vazia, retorna mensagem de erro
        
        top_element = self.list.get(0) # obtém o elemento do topo da pilha
        self.list.remove_first() # remove o elemento do topo

        return top_element # retorna o elemento removido

    def peak(self):
        if self.is_empty():
            raise IndexError('Stack is empty') # se a pilha estiver vazia, retorna mensagem de erro
        
        return self.list.get(0) # retorna o elemento do topo
    
    def is_empty(self):
        return self.list.is_empty() # retorna True se a pilha estiver vazia e False se não estiver
    
    def size(self):
        return self.list.size() # retorna o tamanho da pilha
