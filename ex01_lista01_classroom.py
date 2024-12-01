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
