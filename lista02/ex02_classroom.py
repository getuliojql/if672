def busca_linear(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i
        
    return -1

def busca_binaria(lista, chave):
    limite_inferior = 0
    limite_superior = len(lista) - 1

    while limite_inferior <= limite_superior:
        meio = (limite_inferior + limite_superior) // 2

        if chave == lista[meio]:
            return meio
        
        elif chave > lista[meio]:
            limite_inferior = meio + 1

        else:
            limite_superior = meio - 1

    return -1
