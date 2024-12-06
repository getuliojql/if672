class ObjectArrayList:
    def __init__(self, size=3):
        self.objects = [None] * size # array com capacidade inicial 3
        self.object_counter = 0      # contador de elementos 

    def add(self, obj):
        if self.object_counter >= len(self.objects): # verifica se a array está cheia
            self.resize() # redimensiona a array, se necessário

        self.objects[self.object_counter] = obj # adiciona o elemento no final
        self.object_counter += 1 # incrementa o contador

    def add_at(self, position, obj):
        if position < 0 or position > self.object_counter: # verifica se a posição é válida
            raise IndexError('Index out of range') # se o índice for inválido, mostra mensagem de erro

        if self.object_counter >= len(self.objects): # verifica se a array está cheia
            self.resize() # redimensiona a array, se necessário

        for i in range(self.object_counter, position, -1): # desloca elementos para direita a partir da posição determinada
            self.objects[i] = self.objects[i - 1]

        self.objects[position] = obj # adiciona o elemento na posição especificada
        self.object_counter += 1 # incrementa o contador

    def add_all(self, position, elements):
        if position < 0 or position > self.object_counter: # verifica se a posição é válida
            raise IndexError('Index out of range') # se o índice for inválido, mostra mensagem de erro
        
        while self.object_counter + len(elements) > len(self.objects):
            self.resize() # redimensiona quantas vezes for necessário para garantir que há espaço suficiente

        for i in range(self.object_counter - 1, position - 1, -1):
            self.objects[i + len(elements)] = self.objects[i] # move os elementos existentes para direita para abrir espaço

        for i in range(len(elements)):
            self.objects[position + i] = elements[i] # adiciona os novos elementos

        self.object_counter += len(elements) # atualiza o contador

    def remove(self, obj):
        for i in range(self.object_counter):
            if self.objects[i] == obj: # encontra o elemento determinado
                self.remove_at(i) # remove o elemento utilizando sua posição
                return

        raise ValueError('Element not found') # se o elemento não for encontrado, mostra mensagem de erro

    def remove_at(self, index):
        if 0 <= index < self.object_counter: # verifica se o índice é válido
            for i in range(index, self.object_counter - 1): # desloca os elementos subsequentes para esquerda
                self.objects[i] = self.objects[i + 1]

            self.objects[self.object_counter - 1] = None # remove o elemento especificado
            self.object_counter -= 1 # decrementa o contador

        else:
            raise IndexError('Index out of range') # se o índice for inválido, mostra mensagem de erro
        
    def get(self, index):
        if 0 <= index < self.object_counter: # verifica se o índice é válido
            return self.objects[index] # retorna o elemento naquela posição, se o índice for válido

        else:
            raise IndexError('Index out of range') # se o índice for inválido, mostra mensagem de erro
        
    def is_empty(self):
        return self.object_counter == 0 # retorna True se a array estiver vazia e False se não estiver
    
    def size(self):
        return self.object_counter # retorna a quantidade de elementos na array
    
    def clear(self):
        self.objects = [None] * len(self.objects) # redefine a array como vazia
        self.object_counter = 0 # reseta o contador

    def resize(self):
        new_objects = [None] * (len(self.objects) * 2) # cria uma array com o dobro do tamanho da anterior

        for i in range(len(self.objects)): # copia os elementos da array antiga para a nova
            new_objects[i] = self.objects[i]

        self.objects = new_objects # substitui a array anterior pela maior
    
    def __str__(self) -> str:
        result = '[' # adiciona o colchete de abertura

        for i in range(self.object_counter):
            result += str(self.objects[i]) # adiciona o elemento da vez como string

            if i < self.object_counter - 1:
                result += ', ' # adiciona uma vírgula e um espaço para separar os elementos, exceto se for o último

        result += ']' # adiciona o colchete de fechamento

        return result # retorna a string final

class SinglyNode:
    def __init__(self, data):
        self.data = data # armazena a informação do nó
        self.next = None # aponta para o próximo nó (inicialmente inexistente)

class SinglyLinkedList:
    def __init__(self):
        self.first = None # referência para o primeiro nó da lista
        self.last = None # referência para o último nó da lista
        self.node_counter = 0 # contador de nós

    def add_first(self, obj):
        new_node = SinglyNode(obj) # cria um novo nó com a informação fornecida
        new_node.next = self.first # faz o novo nó apontar para o antigo primeiro, agora segundo nó
        self.first = new_node # atualiza o ponteiro "primeiro"

        if self.node_counter == 0: # verifica se a lista estava vazia
            self.last = new_node # nesse caso, atualiza também o ponteiro "último"

        self.node_counter += 1 # incrementa o contador

    def add_last(self, obj):
        if self.node_counter == 0:
            self.add_first(obj) # se a lista estiver vazia, adiciona no ínicio

        else:
            new_node = SinglyNode(obj) # se a lista não estiver vazia, cria um novo nó com a informação fornecida

            self.last.next = new_node # faz o antigo último, agora penúltimo nó apontar para o novo nó
            self.last = new_node # atualiza o ponteiro "último"

            self.node_counter += 1 # incrementa o contador

    def add_at(self, position, obj):
        if position == 0:
            self.add_first(obj) # se a posição informada for a primeira, adiciona no começo

        elif position == self.node_counter:
            self.add_last(obj) # se a posição informada for a última, adiciona no final

        else:
            prev_node = self.get_node(position - 1) # obtém o nó anterior à posição informada

            new_node = SinglyNode(obj) # cria o novo nó

            new_node.next = prev_node.next # faz o novo nó apontar para o próximo nó
            prev_node.next = new_node # faz o nó anterior apontar para o novo nó

            self.node_counter += 1 # incrementa o contador

    def size(self):
        return self.node_counter # retorna o tamanho da lista
            
    def contains(self, obj):
        current_node = self.first # define o primeiro nó como o atual

        while current_node is not None:
            if current_node.data == obj: # compara o valor do nó atual com o valor procurado
                return True # caso ache, retorna True
            
            current_node = current_node.next # avança para o próximo nó

        return False # caso não ache, retorna False
    
    def get(self, position):
        return self.get_node(position).data
    
    def remove_first(self):
        if not self.busy_position(0):
            raise IndexError('List is empty') # se a lista estiver vazia, retorna mensagem de erro
        
        self.first = self.first.next # atualiza o ponteiro "primeiro"

        if self.node_counter == 0:
            self.last = None # caso a lista tenha ficado vazia, atualiza o ponteiro "último" de acordo

        self.node_counter -= 1

    def remove_last(self):
        if not self.busy_position(self.node_counter - 1):
            raise IndexError('List is empty') # se a lista estiver vazia, retorna mensagem de erro
        
        if self.node_counter == 1: # caso só haja um elemento antes da remoção, atualiza ambos os ponteiros para None
            self.first = None 
            self.last = None

        else:
            penultimate_node = self.get_node(self.node_counter - 2) # obtém o penúltimo nó
            penultimate_node.next = None # faz o penúltimo nó não apontar para nenhum outro
            self.last = penultimate_node # atualiza o ponteiro "último"

    def remove_at(self, position):
        if not self.busy_position(position):
            raise IndexError('Index out of range') # se o índice for inválido, mostra mensagem de erro
        
        if position == 0:
            self.remove_first() # se a posição informada for a primeira, remove o primeiro

        elif position == self.node_counter - 1:
            self.remove_last() # se a posição informada for a última, remove o último

        else:
            prev_node = self.get_node(position - 1) # obtém o nó anterior
            prev_node.next = prev_node.next.next # atualiza o próximo do nó anterior
            self.node_counter -= 1 # decrementa o contador

    def is_empty(self):
        return self.node_counter == 0 # retorna True se a lista estiver vazia e False se não estiver
    
    def clear(self):
        self.first = None # reseta o ponteiro "primeiro"
        self.last = None # reseta o ponteiro "último"
        self.node_counter = 0 # reseta o contador

    def busy_position(self, position):
        return 0 <= position < self.node_counter # retorna True se a posição estiver ocupada, False se não estiver
    
    def get_node(self, position):
        if not self.busy_position(position): # verifica se a posição está ocupada
            raise ValueError('Invalid position') # se não estiver, mostra mensagem de erro
        
        current_node = self.first # define o primeiro nó como o primeiro da iteração

        for _ in range(position):
            current_node = current_node.next # encontra a posição desejada

        return current_node # retorna o nó encontrado
    
    def __str__(self) -> str:
        result = '['  # adiciona o colchete de abertura
        current_node = self.first # define o primeiro nó como o atual

        while current_node is not None:
            result += str(current_node.data) # adiciona o nó da vez como string

            if current_node.next is not None:
                result += ', ' # adiciona uma vírgula e um espaço para separar os nós, exceto se for o último

            current_node = current_node.next # move para o próximo nó
        
        result += ']' # adiciona o colchete de abertura

        return result # retorna a string final

class DoublyNode:
    def __init__(self, data):
        self.data = data # armazena a informação do nó
        self.next = None # aponta para o próximo nó (inicialmente inexistente)
        self.prev = None # aponta para o nó anterior (inicialmente inexistente)

class DoublyLinkedList:
    def __init__(self):
        self.first = None # referência para o primeiro nó da lista
        self.last = None # referência para o último nó da lista
        self.node_counter = 0 # contador de nós

    def add_first(self, obj):
        new_node = DoublyNode(obj) # cria um novo nó com a informação fornecida
        new_node.next = self.first # faz o novo nó apontar para o antigo primeiro, agora segundo nó

        if self.first is not None:
            self.first.prev = new_node # atualiza o "prev" do antigo primeiro laço para apontar para o novo primeiro

        self.first = new_node # atualiza o ponteiro "primeiro"

        if self.node_counter == 0: # verifica se a lista estava vazia
            self.last = new_node # nesse caso, atualiza também o ponteiro "último"

        self.node_counter += 1 # incrementa o contador

    def add_last(self, obj):
        if self.node_counter == 0:
            self.add_first(obj) # se a lista estiver vazia, adiciona no ínicio

        else:
            new_node = DoublyNode(obj) # se a lista não estiver vazia, cria um novo nó com a informação fornecida

            new_node.prev = self.last # faz o novo nó apontar para o antigo último, agora penúltimo nó
            self.last.next = new_node # faz o antigo último, agora penúltimo nó apontar para o novo nó
            self.last = new_node # atualiza o ponteiro "último"

            self.node_counter += 1 # incrementa o contador

    def add_at(self, position, obj):
        if position == 0:
            self.add_first(obj) # se a posição informada for a primeira, adiciona no começo

        elif position == self.node_counter:
            self.add_last(obj) # se a posição informada for a última, adiciona no final

        else:
            prev_node = self.get_node(position - 1) # obtém o nó anterior à posição informada

            new_node = DoublyNode(obj) # cria o novo nó

            new_node.next = prev_node.next # faz o novo nó apontar para o próximo nó
            new_node.prev = prev_node # faz o novo nó apontar para o nó anterior

            prev_node.next.prev = new_node # faz o próximo nó apontar para o novo nó
            prev_node.next = new_node # faz o nó anterior apontar para o novo nó

            self.node_counter += 1 # incrementa o contador

    def size(self):
        return self.node_counter # retorna o tamanho da lista
            
    def contains(self, obj):
        current_node = self.first # define o primeiro nó como o atual

        while current_node is not None:
            if current_node.data == obj: # compara o valor do nó atual com o valor procurado
                return True # caso ache, retorna True
            
            current_node = current_node.next # avança para o próximo nó

        return False # caso não ache, retorna False
    
    def get(self, position):
        return self.get_node(position).data
    
    def remove_first(self):
        if not self.busy_position(0):
            raise IndexError('List is empty') # se a lista estiver vazia, retorna mensagem de erro
        
        self.first = self.first.next # atualiza o ponteiro "primeiro"

        if self.first is not None:
            self.first.prev = None # se a lista não ficou vazia, remove a referência ao nó anterior

        else:
            self.last = None # caso a lista tenha ficado vazia, atualiza o ponteiro "último" de acordo

        self.node_counter -= 1

    def remove_last(self):
        if not self.busy_position(self.node_counter - 1):
            raise IndexError('List is empty') # se a lista estiver vazia, retorna mensagem de erro
        
        if self.node_counter == 1: # caso só haja um elemento antes da remoção, atualiza ambos os ponteiros para None
            self.first = None 
            self.last = None

        else:
            self.last = self.last.prev # atualiza o ponteiro "último" de acordo
            self.last.next = None # remove a referência ao nó removido

        self.node_counter -= 1

    def remove_at(self, position):
        if not self.busy_position(position):
            raise IndexError('Index out of range') # se o índice for inválido, mostra mensagem de erro
        
        if position == 0:
            self.remove_first() # se a posição informada for a primeira, remove o primeiro

        elif position == self.node_counter - 1:
            self.remove_last() # se a posição informada for a última, remove o último

        else:
            current_node = self.get_node(position) # obtém o nó na posição especificada

            current_node.prev.next = current_node.next # atualiza o "next" do nó anterior
            current_node.next.prev = current_node.prev # atualiza o "prev" do próximo nó

            self.node_counter -= 1 # decrementa o contador

    def is_empty(self):
        return self.node_counter == 0 # retorna True se a lista estiver vazia e False se não estiver
    
    def clear(self):
        self.first = None # reseta o ponteiro "primeiro"
        self.last = None # reseta o ponteiro "último"
        self.node_counter = 0 # reseta o contador

    def busy_position(self, position):
        return 0 <= position < self.node_counter # retorna True se a posição estiver ocupada, False se não estiver
    
    def get_node(self, position):
        if not self.busy_position(position): # verifica se a posição está ocupada
            raise ValueError('Invalid position') # se não estiver, mostra mensagem de erro
        
        if position < self.node_counter // 2: # se for mais vantajoso, busca do início da lista
            current_node = self.first

            for _ in range(position):
                current_node = current_node.next # encontra a posição desejada

        else: # caso contrário, busca do final da lista
            current_node = self.last

            for _ in range(self.node_counter - position - 1):
                current_node = current_node.prev # encontra a posição desejada

        return current_node # retorna o nó encontrado
    
    def __str__(self) -> str:
        result = '['  # adiciona o colchete de abertura
        current_node = self.first # define o primeiro nó como o atual

        while current_node is not None:
            result += str(current_node.data) # adiciona o nó da vez como string

            if current_node.next is not None:
                result += ', ' # adiciona uma vírgula e um espaço para separar os nós, exceto se for o último

            current_node = current_node.next # move para o próximo nó
        
        result += ']' # adiciona o colchete de abertura

        return result # retorna a string final

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

def main():
    print('=== Testando Lista ===')
    obj_list = ObjectArrayList()

    obj_list.add(10)
    obj_list.add(20)
    obj_list.add(30)
    print(f'Lista após inserções: {obj_list}')

    obj_list.add_all(1, [40, 50])
    print(f'Lista após add_all na posição 1: {obj_list}')

    obj_list.remove(30)
    print(f'Lista após remoção do 30: {obj_list}')

    obj_list.remove_at(1)
    print(f'Lista após remove_at na posição 1: {obj_list}')

    obj_list.clear()
    print(f'Lista após limpar: {obj_list}')

    obj_list.add(70)
    print(f'Elemento na posição 0: {obj_list.get(0)}')
    print(f'A lista está vazia? {obj_list.is_empty()}')
    print(f'Tamanho da lista: {obj_list.size()}\n')

    print('=== Testando Lista Encadeada Simples ===')
    singly_list = SinglyLinkedList()

    singly_list.add_first(10)
    singly_list.add_last(20)
    singly_list.add_at(1, 15)
    print(f'Lista encadeada após inserções: {singly_list}')

    singly_list.remove_at(1)
    print(f'Lista encadeada após remover elemento na posição 1: {singly_list}')
    print(f'A lista contém 10? {singly_list.contains(10)}')
    print(f'A lista contém 99? {singly_list.contains(99)}')

    singly_list.clear()
    print(f'Lista encadeada após limpar: {singly_list}')

    singly_list.add_last(40)
    print(f'Elemento na posição 0: {singly_list.get(0)}')
    print(f'A lista está vazia? {singly_list.is_empty()}')
    print(f'Tamanho da lista: {singly_list.size()}\n')

    print('=== Testando Lista Encadeada Dupla ===')
    doubly_list = DoublyLinkedList()

    doubly_list.add_first(10)
    doubly_list.add_last(20)
    doubly_list.add_at(1, 15)
    print(f'Lista encadeada dupla após inserções: {doubly_list}')

    doubly_list.remove_at(1)
    print(f'Lista encadeada dupla após remover elemento na posição 1: {doubly_list}')
    print(f'A lista contém 20? {doubly_list.contains(20)}')
    print(f'A lista contém 99? {doubly_list.contains(99)}')

    doubly_list.clear()
    print(f'Lista encadeada dupla após limpar: {doubly_list}')

    doubly_list.add_first(30)
    print(f'Elemento na posição 0: {doubly_list.get(0)}')
    print(f'A lista está vazia? {doubly_list.is_empty()}')
    print(f'Tamanho da lista: {doubly_list.size()}\n')

    print('=== Testando Pilha ===')
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f'Topo da pilha: {stack.peak()}')
    print(f'Removendo elemento do topo: {stack.pop()}')

    stack.push(40)
    print(f'Novo topo após push: {stack.peak()}')
    print(f'A pilha está vazia? {stack.is_empty()}')
    print(f'Tamanho da pilha: {stack.size()}\n')

    print('=== Testando Fila ===')
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f'Início da fila: {queue.front()}')
    print(f'Removendo elemento do início: {queue.dequeue()}')

    queue.enqueue(40)
    print(f'Novo início após enqueue: {queue.front()}')
    print(f'A fila está vazia? {queue.is_empty()}')
    print(f'Tamanho da fila: {queue.size()}')


if __name__ == "__main__":
    main()
