class Node:
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
        new_node = Node(obj) # cria um novo nó com a informação fornecida
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
            new_node = Node(obj) # se a lista não estiver vazia, cria um novo nó com a informação fornecida

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

            new_node = Node(obj) # cria o novo nó

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
