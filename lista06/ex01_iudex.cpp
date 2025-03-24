#include <bits/stdc++.h>
#define endl '\n'
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

// Estrutura Node: nó da lista encadeada de inteiros.
struct Node {
    int val;
    Node* next;
    Node(int v) {
        val = v;
        next = nullptr;
    }
};

// Classe SinglyLinkedList: lista encadeada simples para armazenar os vizinhos.
class SinglyLinkedList {
public:
    Node* head;
    
    SinglyLinkedList() {
        head = nullptr;
    }
    
    // Insere um elemento no início da lista.
    void push_front(int v) {
        Node* newNode = new Node(v);
        newNode->next = head;
        head = newNode;
    }
    
    // Retorna true se a lista estiver vazia.
    bool isEmpty() {
        return head == nullptr;
    }
    
    // Imprime os elementos da lista.
    void printList() {
        if (head == nullptr) {
            cout << "Lista Vazia";
            return;
        }
        Node* cur = head;
        while (cur != nullptr) {
            cout << cur->val << " ";
            cur = cur->next;
        }
    }
    
    // Destrutor: libera os nós.
    ~SinglyLinkedList() {
        Node* cur = head;
        while (cur != nullptr) {
            Node* nxt = cur->next;
            delete cur;
            cur = nxt;
        }
    }
};

// Função DFS recursiva.
void dfs(int u, bool visited[], SinglyLinkedList** graph) {
    visited[u] = true;
    cout << u << " ";
    // Percorre a lista de adjacências de u.
    Node* cur = graph[u]->head;
    while (cur != nullptr) {
        int v = cur->val;
        if (!visited[v])
            dfs(v, visited, graph);
        cur = cur->next;
    }
}

int main(int argc, char *argv[]) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string line;
    // Lê o número de vértices.
    getline(cin, line);
    line = strip(line);
    int Q = stoi(line);
    
    // Cria o grafo: um vetor de ponteiros para SinglyLinkedList, um para cada vértice.
    SinglyLinkedList** graph = new SinglyLinkedList*[Q];
    for (int i = 0; i < Q; i++) {
        graph[i] = new SinglyLinkedList();
    }
    
    // Lê as conexões.
    // Cada linha tem o formato: "u v flag"
    // flag==1 => continue; flag==0 => última conexão.
    while (true) {
        getline(cin, line);
        line = strip(line);
        if (line == "") continue;
        // Parse dos três inteiros.
        int pos = 0;
        string su = "";
        while (pos < line.size() && line[pos] != ' ') {
            su.push_back(line[pos]);
            pos++;
        }
        while (pos < line.size() && line[pos] == ' ')
            pos++;
        string sv = "";
        while (pos < line.size() && line[pos] != ' ') {
            sv.push_back(line[pos]);
            pos++;
        }
        while (pos < line.size() && line[pos] == ' ')
            pos++;
        string sf = "";
        while (pos < line.size() && line[pos] != ' ') {
            sf.push_back(line[pos]);
            pos++;
        }
        int u = stoi(su);
        int v = stoi(sv);
        int flag = stoi(sf);
        // Como o grafo é não orientado, adiciona v na lista de u e u na lista de v.
        graph[u]->push_front(v);
        graph[v]->push_front(u);
        if (flag == 0)
            break;
    }
    
    // Imprime a lista de adjacências de cada vértice.
    for (int i = 0; i < Q; i++) {
        cout << i << ": ";
        if (graph[i]->isEmpty())
            cout << "Lista Vazia";
        else
            graph[i]->printList();
        cout << "\n";
    }
    cout << "\n";
    
    // Executa a busca em profundidade (DFS) a partir do vértice 0.
    bool visited[1000]; // considerando Q <= 1000 (ajuste se necessário)
    for (int i = 0; i < Q; i++)
        visited[i] = false;
    
    dfs(0, visited, graph);
    cout << "\n";
    
    // Libera a memória.
    for (int i = 0; i < Q; i++) {
        delete graph[i];
    }
    delete [] graph;
    
    return 0;
}
