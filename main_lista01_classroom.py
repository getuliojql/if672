from ex01_lista01_classroom import ObjectArrayList
from ex02_lista01_classroom import SinglyLinkedList
from ex03_lista01_classroom import DoublyLinkedList
from ex04_lista01_classroom import Stack
from ex05_lista01_classroom import Queue

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
    print(f'A lista contém 20? {singly_list.contains(20)}')
    print(f'A lista contém 99? {singly_list.contains(99)}')

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
