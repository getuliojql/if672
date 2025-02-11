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

// Função parseMove: extrai dois inteiros S e C de uma linha ("S C").
void parseMove(const string &line, int &S, int &C) {
    int i = 0;
    while (i < line.size() && line[i] == ' ')
        i++;
        
    string s1 = "";
    while (i < line.size() && line[i] != ' ') {
        s1.push_back(line[i]);
        i++;
    }
    
    while (i < line.size() && line[i] == ' ')
        i++;
        
    string s2 = "";
    while (i < line.size() && line[i] != ' ') {
        s2.push_back(line[i]);
        i++;
    }
    
    S = stoi(s1);
    C = stoi(s2);
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
    
    // getAt: retorna o elemento na posição (0 = topo, 1 = segundo, etc.).
    int getAt(int index) {
        return list.get(index);
    }
};

// Função addStone: adiciona uma pedra à coluna e executa a subtração.
void addStone(Stack* col, int stone) {
    col->push(stone);
    while (col->size() >= 2) {
        int top1 = col->peek();
        int second = col->getAt(1);
        if (top1 == second) {
            int color = top1;
            while (!col->is_empty() && col->peek() == color)
                col->pop();
        } else {
            break;
        }
    }
}

// Classe ColumnArray: array dinâmico de colunas (cada coluna é uma Stack*).
class ColumnArray {
private:
    Stack** columns;
    int capacity;
    int count;
    
    // Redimensiona o array de colunas.
    void resize() {
        int newCapacity = capacity * 2;
        Stack** newArray = new Stack*[newCapacity];
        for (int i = 0; i < count; i++) {
            newArray[i] = columns[i];
        }
        delete [] columns;
        columns = newArray;
        capacity = newCapacity;
    }
    
public:
    ColumnArray(int initialCapacity = 10) {
        capacity = initialCapacity;
        count = 0;
        columns = new Stack*[capacity];
    }
    
    ~ColumnArray() {
        for (int i = 0; i < count; i++)
            delete columns[i];
        delete [] columns;
    }
    
    // Retorna o número de colunas.
    int size() {
        return count;
    }
    
    // Retorna a coluna no índice especificado.
    Stack* get(int index) {
        if (index < 0 || index >= count)
            throw "Índice fora de alcance (ColumnArray)";
        return columns[index];
    }
    
    // Insere uma coluna na posição indicada.
    void insert_at(int index, Stack* col) {
        if (count == capacity)
            resize();
        for (int i = count; i > index; i--)
            columns[i] = columns[i - 1];
        columns[index] = col;
        count++;
    }
    
    // Insere uma coluna no final.
    void push_back(Stack* col) {
        insert_at(count, col);
    }
    
    // Remove a coluna do índice especificado.
    void remove_at(int index) {
        if (index < 0 || index >= count)
            throw "Índice fora de alcance (remove_at)";
        delete columns[index];
        for (int i = index; i < count - 1; i++)
            columns[i] = columns[i + 1];
        count--;
    }
};

int main() {
    int P;
    string line;
    
    // Lê o número de casos e remove espaços indesejados.
    getline(cin, line);
    line = strip(line);
    P = stoi(line);
    
    for (int caseIndex = 0; caseIndex < P; caseIndex++) {
    
        // Lê até encontrar uma linha não vazia.
        do {
            getline(cin, line);
            line = strip(line);
        } while (line == "");
        
        ColumnArray board;   // Conjunto de colunas (inicialmente vazio)
        
        // Processa as jogadas até ler a linha "END".
        while (line != "END") {
            int S, C;
            parseMove(line, S, C);
            int N = board.size();   // Número corrente de colunas
            
            if (S == 0) {
                // Inicia nova coluna à esquerda.
                Stack* col = new Stack();
                col->push(C);
                board.insert_at(0, col);
            }
            else if (S == N + 1) {
                // Inicia nova coluna à direita.
                Stack* col = new Stack();
                col->push(C);
                board.push_back(col);
            }
            else if (S >= 1 && S <= N) {
                // Adiciona a pedra na coluna S (1-indexada).
                Stack* col = board.get(S - 1);
                addStone(col, C);
                // Se a coluna ficar vazia, remove-a.
                if (col->size() == 0)
                    board.remove_at(S - 1);
            }
            
            getline(cin, line);
            line = strip(line);
        }
        
        // Fim da partida; pode haver uma linha em branco depois do "END".
        // Imprime o estado final.
        cout << "caso " << caseIndex << ":";
        int finalColumns = board.size();
        if (finalColumns > 0) {
            cout << " ";
            for (int i = 0; i < finalColumns; i++) {
                Stack* col = board.get(i);
                cout << col->peek();
                if (i < finalColumns - 1)
                    cout << " ";
            }
        }
        cout << "\n";
    }
    
    return 0;
}
