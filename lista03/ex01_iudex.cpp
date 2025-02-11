#include <iostream>
#include <string>
using namespace std;

// Função strip: remove espaços do início e do fim de uma string.
string strip(const string &s) {
    int start = 0;
    while (start < s.size() && s[start] == ' ')
        start++;
        
    int end = s.size() - 1;
    while (end >= start && s[end] == ' ')
        end--;
        
    string result = "";
    for (int i = start; i <= end; i++)
        result.push_back(s[i]);
        
    return result;
}

// Função my_abs: retorna o valor absoluto de um inteiro.
int my_abs(int x) {
    return (x < 0) ? -x : x;
}

// Classe SinglyNode: representa um nó na lista ligada simples.
class SinglyNode {
public:
    int data;
    SinglyNode *next;
    
    SinglyNode(int d) {
        data = d;
        next = nullptr;
    }
};

// Classe SinglyLinkedList: lista ligada simples com operações básicas.
class SinglyLinkedList {
private:
    SinglyNode *first;
    SinglyNode *last;
    int node_counter;
    
public:
    SinglyLinkedList() {
        first = nullptr;
        last = nullptr;
        node_counter = 0;
    }
    
    // Adiciona um elemento no início da lista.
    void add(int obj) {
        SinglyNode *new_node = new SinglyNode(obj);
        new_node->next = first;
        first = new_node;
        
        if (node_counter == 0)
            last = new_node;
            
        node_counter++;
    }
    
    // Remove o primeiro elemento da lista.
    void remove() {
        if (first == nullptr)
            throw "Lista vazia";
            
        SinglyNode *temp = first;
        first = first->next;
        delete temp;
        node_counter--;
        
        if (node_counter == 0)
            last = nullptr;
    }
    
    // Retorna o dado no índice especificado.
    int get(int index) {
        if (index < 0 || index >= node_counter)
            throw "Índice fora de alcance";
            
        SinglyNode *curr = first;
        int i = 0;
        while (i < index) {
            curr = curr->next;
            i++;
        }
        return curr->data;
    }
    
    // Retorna true se a lista estiver vazia.
    bool is_empty() {
        return (node_counter == 0);
    }
    
    // Retorna o número de elementos na lista.
    int size() {
        return node_counter;
    }
};

// Classe Stack: implementa uma pilha utilizando a lista ligada.
class Stack {
private:
    SinglyLinkedList list;
    
public:
    // Empilha um elemento.
    void push(int element) {
        list.add(element);
    }
    
    // Desempilha e retorna o elemento do topo.
    int pop() {
        if (is_empty())
            throw "Pilha vazia";
            
        int top = peek();
        list.remove();
        return top;
    }
    
    // Retorna o elemento do topo sem desempilhar.
    int peek() {
        if (is_empty())
            throw "Pilha vazia";
            
        return list.get(0);
    }
    
    // Retorna true se a pilha estiver vazia.
    bool is_empty() {
        return list.is_empty();
    }
    
    // Retorna o número de elementos na pilha.
    int size() {
        return list.size();
    }
};

int main() {
    int t;
    string line;
    
    // Lê o número de casos e remove espaços indesejados.
    getline(cin, line);
    line = strip(line);
    t = stoi(line);
    
    for (int rodada = 1; rodada <= t; rodada++) {
    
        // Lê linhas até encontrar uma não vazia.
        do {
            getline(cin, line);
            line = strip(line);
        } while (line == "");
        
        Stack pilha;
        int n = stoi(line);
        
        // Processa a partida até ler 0.
        while (n != 0) {
            pilha.push(n);
            
            // Enquanto houver pelo menos dois elementos, processa a subtração.
            while (pilha.size() >= 2) {
                int a = pilha.pop();
                int b = pilha.pop();
                
                if ((a % 2) == (b % 2)) {
                    int diff = my_abs(a - b);
                    // Empilha a diferença somente se não for zero.
                    if (diff != 0)
                        pilha.push(diff);
                } else {
                    // Se as paridades forem diferentes, recoloca os elementos.
                    pilha.push(b);
                    pilha.push(a);
                    break;
                }
            }
            
            getline(cin, line);
            line = strip(line);
            n = stoi(line);
        }
        
        int tamanho = pilha.size();
        int top;
        if (tamanho > 0)
            top = pilha.peek();
        else
            top = -1;
            
        cout << "Pilha " << rodada << ": " << tamanho << " " << top << "\n";
    }
    
    return 0;
}
