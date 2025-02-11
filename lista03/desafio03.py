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

    # MÉTODO ADICIONAL PARA ATUALIZAR UM ELEMENTO NA POSIÇÃO DETERMINADA
    def set(self, index, value):
        if index < 0 or index >= self.object_counter:
            raise IndexError('Index out of range')
        self.objects[index] = value
    
    def __str__(self) -> str:
        result = '[' # adiciona o colchete de abertura

        for i in range(self.object_counter):
            result += str(self.objects[i]) # adiciona o elemento da vez como string

            if i < self.object_counter - 1:
                result += ', ' # adiciona uma vírgula e um espaço para separar os elementos, exceto se for o último

        result += ']' # adiciona o colchete de fechamento

        return result # retorna a string final


def char_to_num(c):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0

    while i < 26:
        if alphabet[i] == c:
            return i + 1
        i += 1

    return 0


def num_to_char(n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if n < 1 or n > 26:
        return '?'
    
    return alphabet[n - 1]


def copy_OAL(oal):
    new_oal = ObjectArrayList(oal.size())
    i = 0

    while i < oal.size():
        new_oal.add(oal.get(i))
        i += 1

    return new_oal


def combined_array(original, even, evenIndices):
    combined = copy_OAL(original)
    i = 0

    while i < evenIndices.size():
        index = evenIndices.get(i)
        combined.set(index, even.get(i))
        i += 1

    return combined


def array_state(arr, label):
    letters = numbers = ''
    i = 0

    while i < arr.size():
        num = arr.get(i)
        letters += num_to_char(num)
        numbers += str(num)

        if i < arr.size() - 1:
            letters += ''
            numbers += ''
        
        i += 1
    print(f'{label}: {letters}   {numbers}')


def bubble_sort(even, original, evenIndices):
    comparisons = swaps = loop_iterations = 0
    n = even.size()

    print('===== BUBBLE SORT =====')

    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Estado inicial")
    i = 0

    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            loop_iterations += 1
            comparisons += 1
            if even.get(j) > even.get(j + 1):
                temp = even.get(j)
                even.set(j, even.get(j + 1))
                even.set(j + 1, temp)
                swaps += 1
            j += 1
        combined = combined_array(original, even, evenIndices)
        array_state(combined, "Após iteração " + str(i + 1))
        i += 1
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Vetor final ordenado")
    print("Comparações:", comparisons, "Trocas:", swaps, "Iterações de laço:", loop_iterations)

def selection_sort(even, original, evenIndices):
    comparisons = 0
    swaps = 0
    loop_iterations = 0
    n = even.size()
    print("\n===== SELECTION SORT =====")
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Estado inicial")
    i = 0
    while i < n - 1:
        min_index = i
        j = i + 1
        while j < n:
            loop_iterations += 1
            comparisons += 1
            if even.get(j) < even.get(min_index):
                min_index = j
            j += 1
        if min_index != i:
            temp = even.get(i)
            even.set(i, even.get(min_index))
            even.set(min_index, temp)
            swaps += 1
        combined = combined_array(original, even, evenIndices)
        array_state(combined, "Após iteração " + str(i + 1))
        i += 1
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Vetor final ordenado")
    print("Comparações:", comparisons, "Trocas:", swaps, "Iterações de laço:", loop_iterations)

def insertion_sort(even, original, evenIndices):
    comparisons = 0
    substitutions = 0
    loop_iterations = 0
    n = even.size()
    print("\n===== INSERTION SORT =====")
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Estado inicial")
    i = 1
    while i < n:
        key = even.get(i)
        j = i - 1
        while j >= 0 and even.get(j) > key:
            loop_iterations += 1
            comparisons += 1
            even.set(j + 1, even.get(j))
            substitutions += 1
            j -= 1
        if j >= 0:
            comparisons += 1
            loop_iterations += 1
        even.set(j + 1, key)
        substitutions += 1
        combined = combined_array(original, even, evenIndices)
        array_state(combined, "Após iteração " + str(i))
        i += 1
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Vetor final ordenado")
    print("Comparações:", comparisons, "Substituições:", substitutions, "Iterações de laço:", loop_iterations)

def shell_sort(even, original, evenIndices):
    comparisons = 0
    substitutions = 0
    loop_iterations = 0
    n = even.size()
    print("\n===== SHELL SORT =====")
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Estado inicial")
    gap = n // 2
    pass_count = 0
    while gap > 0:
        i = gap
        while i < n:
            temp = even.get(i)
            j = i
            while j >= gap and even.get(j - gap) > temp:
                loop_iterations += 1
                comparisons += 1
                even.set(j, even.get(j - gap))
                substitutions += 1
                j -= gap
            if j >= gap:
                comparisons += 1
                loop_iterations += 1
            even.set(j, temp)
            substitutions += 1
            i += 1
        pass_count += 1
        combined = combined_array(original, even, evenIndices)
        array_state(combined, "Após passagem (gap = " + str(gap) + ", iteração " + str(pass_count) + ")")
        gap = gap // 2
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Vetor final ordenado")
    print("Comparações:", comparisons, "Substituições:", substitutions, "Iterações de laço:", loop_iterations)

def merge_sort(even, original, evenIndices):
    comparisons = 0
    substitutions = 0
    loop_iterations = 0
    n = even.size()
    print("\n===== MERGE SORT (Bottom-Up) =====")
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Estado inicial")
    width = 1
    pass_num = 0
    temp_arr = ObjectArrayList(n)
    i = 0
    while i < n:
        temp_arr.add(None)
        i += 1
    while width < n:
        i = 0
        while i < n:
            left = i
            mid = i + width
            if mid > n:
                mid = n
            right = i + 2 * width
            if right > n:
                right = n
            l = left
            r = mid
            k = left
            while l < mid and r < right:
                loop_iterations += 1
                comparisons += 1
                if even.get(l) <= even.get(r):
                    temp_arr.set(k, even.get(l))
                    l += 1
                    substitutions += 1
                else:
                    temp_arr.set(k, even.get(r))
                    r += 1
                    substitutions += 1
                k += 1
            while l < mid:
                loop_iterations += 1
                temp_arr.set(k, even.get(l))
                l += 1
                k += 1
                substitutions += 1
            while r < right:
                loop_iterations += 1
                temp_arr.set(k, even.get(r))
                r += 1
                k += 1
                substitutions += 1
            i += 2 * width
        i = 0
        while i < n:
            even.set(i, temp_arr.get(i))
            i += 1
        pass_num += 1
        combined = combined_array(original, even, evenIndices)
        array_state(combined, "Após passagem " + str(pass_num) + " (largura = " + str(width) + ")")
        width = width * 2
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Vetor final ordenado")
    print("Comparações:", comparisons, "Atribuições/Substituições:", substitutions, "Iterações de laço:", loop_iterations)

def quick_sort(even, original, evenIndices):
    counters = {"comparisons": 0, "swaps": 0, "loop_iterations": 0}
    print("\n===== QUICK SORT =====")
    def partition(arr, low, high):
        pivot = arr.get(high)
        i = low - 1
        j = low
        while j < high:
            counters["loop_iterations"] += 1
            counters["comparisons"] += 1
            if arr.get(j) < pivot:
                i += 1
                temp = arr.get(i)
                arr.set(i, arr.get(j))
                arr.set(j, temp)
                counters["swaps"] += 1
            j += 1
        temp = arr.get(i + 1)
        arr.set(i + 1, arr.get(high))
        arr.set(high, temp)
        counters["swaps"] += 1
        return i + 1
    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            combined = combined_array(original, even, evenIndices)
            array_state(combined, "Após partição com pivô na posição " + str(pi))
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)
    quick_sort_recursive(even, 0, even.size() - 1)
    combined = combined_array(original, even, evenIndices)
    array_state(combined, "Vetor final ordenado")
    print("Comparações:", counters["comparisons"], "Trocas:", counters["swaps"], "Iterações de laço:", counters["loop_iterations"])

# ============================================================
# FUNÇÃO PRINCIPAL (main)
# ============================================================
def main():
    seq = "RMQFPWZYKASIOHBJLVU"
    # Cria um ObjectArrayList para armazenar o vetor original
    original = ObjectArrayList(len(seq))
    i = 0
    while i < len(seq):
        num = char_to_num(seq[i])
        original.add(num)
        i += 1
    # Cria um ObjectArrayList para armazenar os índices dos números pares
    evenIndices = ObjectArrayList(original.size())
    i = 0
    while i < original.size():
        if original.get(i) % 2 == 0:
            evenIndices.add(i)
        i += 1
    # Exibe a sequência original (letras e números)
    print("Sequência original (letras):", end=" ")
    i = 0
    while i < original.size():
        print(num_to_char(original.get(i)), end=" ")
        i += 1
    print()
    print("Sequência original (números):", end=" ")
    i = 0
    while i < original.size():
        print(original.get(i), end=" ")
        i += 1
    print()
    # Exibe os índices dos números pares
    print("Índices com códigos pares:", end=" ")
    i = 0
    while i < evenIndices.size():
        print(evenIndices.get(i), end=" ")
        i += 1
    print()
    # Cria as cópias dos números pares para cada algoritmo
    evenArray_bubble = ObjectArrayList(evenIndices.size())
    evenArray_selection = ObjectArrayList(evenIndices.size())
    evenArray_insertion = ObjectArrayList(evenIndices.size())
    evenArray_shell = ObjectArrayList(evenIndices.size())
    evenArray_merge = ObjectArrayList(evenIndices.size())
    evenArray_quick = ObjectArrayList(evenIndices.size())
    i = 0
    while i < evenIndices.size():
        index = evenIndices.get(i)
        value = original.get(index)
        evenArray_bubble.add(value)
        evenArray_selection.add(value)
        evenArray_insertion.add(value)
        evenArray_shell.add(value)
        evenArray_merge.add(value)
        evenArray_quick.add(value)
        i += 1
    # Executa os algoritmos de ordenação (os números pares serão ordenados sem alterar os ímpares)
    bubble_sort(evenArray_bubble, original, evenIndices)
    selection_sort(evenArray_selection, original, evenIndices)
    insertion_sort(evenArray_insertion, original, evenIndices)
    shell_sort(evenArray_shell, original, evenIndices)
    merge_sort(evenArray_merge, original, evenIndices)
    quick_sort(evenArray_quick, original, evenIndices)

# ============================================================
# Execução do programa
# ============================================================
main()