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

// Função my_abs: retorna o valor absoluto de um inteiro.
int my_abs(int x) {
    return (x < 0) ? -x : x;
}

// Estrutura Pair: representa o par (T, C)
// T: timestamp (unsigned int); C: cliente (unsigned int)
struct Pair {
    unsigned int T;
    unsigned int C;
};

// Estrutura AVLNode: representa um nó na árvore AVL.
struct AVLNode {
    int id;                   // device id
    unsigned int wei;         // total bytes transmitidos para este dispositivo
    unsigned int subtreeSum;  // soma dos wei de toda a subárvore
    int height;               // altura do nó
    AVLNode* left;
    AVLNode* right;
    AVLNode(int id, unsigned int w) {
        this->id = id;
        wei = w;
        subtreeSum = w;
        height = 1;
        left = right = nullptr;
    }
};

// Funções auxiliares para AVL.
int getHeight(AVLNode* node) {
    return node ? node->height : 0;
}
unsigned int getSum(AVLNode* node) {
    return node ? node->subtreeSum : 0;
}
void updateNode(AVLNode* node) {
    if (node) {
        node->height = max(getHeight(node->left), getHeight(node->right)) + 1;
        node->subtreeSum = getSum(node->left) + node->wei + getSum(node->right);
    }
}
int getBalance(AVLNode* node) {
    return node ? getHeight(node->left) - getHeight(node->right) : 0;
}
AVLNode* rightRotate(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;
    x->right = y;
    y->left = T2;
    updateNode(y);
    updateNode(x);
    return x;
}
AVLNode* leftRotate(AVLNode* x) {
    AVLNode* y = x->right;
    AVLNode* T2 = y->left;
    y->left = x;
    x->right = T2;
    updateNode(x);
    updateNode(y);
    return y;
}

// Classe AVLTree: gerencia a árvore AVL dos dispositivos.
class AVLTree {
private:
    AVLNode* root;
public:
    AVLTree() { root = nullptr; }
    ~AVLTree() { clear(root); }
    
    void clear(AVLNode* node) {
        if (node) {
            clear(node->left);
            clear(node->right);
            delete node;
        }
    }
    
    // Função recursiva de inserção: se o nó com id X já existe, soma W; caso contrário, insere.
    // Retorna o novo nó raiz da subárvore.
    AVLNode* insert(AVLNode* node, int id, unsigned int w, bool &inserted, int &depth, int currentDepth) {
        if (!node) {
            inserted = true;
            depth = currentDepth;
            return new AVLNode(id, w);
        }
        if (id == node->id) {
            node->wei += w;
            inserted = false;
            depth = currentDepth;
        } else if (id < node->id) {
            node->left = insert(node->left, id, w, inserted, depth, currentDepth+1);
        } else {
            node->right = insert(node->right, id, w, inserted, depth, currentDepth+1);
        }
        updateNode(node);
        int balance = getBalance(node);
        // Balanceamento AVL.
        if (balance > 1 && id < node->left->id)
            return rightRotate(node);
        if (balance < -1 && id > node->right->id)
            return leftRotate(node);
        if (balance > 1 && id > node->left->id) {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }
        if (balance < -1 && id < node->right->id) {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }
        return node;
    }
    
    // Insere ou atualiza o nó com id e w; retorna a profundidade do nó inserido/atualizado.
    int insert(int id, unsigned int w) {
        bool inserted = false;
        int depth = -1;
        root = insert(root, id, w, inserted, depth, 0);
        return depth;
    }
    
    // Busca o nó com id X; retorna par (wei, depth) ou (0, -1) se não encontrado.
    pair<unsigned int, int> search(int id) {
        AVLNode* curr = root;
        int depth = 0;
        while (curr) {
            if (id == curr->id)
                return make_pair(curr->wei, depth);
            else if (id < curr->id)
                curr = curr->left;
            else
                curr = curr->right;
            depth++;
        }
        return make_pair(0u, -1);
    }
    
    // Consulta RNK(X): soma de wei de todos os nós com id < X.
    unsigned int queryRNK(int X) {
        AVLNode* curr = root;
        unsigned int res = 0;
        while (curr) {
            if (X > curr->id) {
                res += getSum(curr->left) + curr->wei;
                curr = curr->right;
            } else {
                curr = curr->left;
            }
        }
        return res;
    }
    
    // Retorna o total global de bytes transmitidos.
    unsigned int totalBytes() {
        return getSum(root);
    }
};

int main(int argc, char *argv[]) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    AVLTree tree;
    unsigned int globalTotal = 0;
    string line;
    
    // Processa a entrada até encontrar "END".
    while(getline(cin, line)) {
        line = strip(line);
        if (line == "END")
            break;
        // Se o comando for ADD
        if (line.substr(0, 3) == "ADD") {
            // Formato: "ADD X W"
            int pos = 3;
            while (pos < line.size() && line[pos] == ' ')
                pos++;
            string sx = "";
            while (pos < line.size() && line[pos] != ' ') {
                sx.push_back(line[pos]);
                pos++;
            }
            while (pos < line.size() && line[pos] == ' ')
                pos++;
            string sw = "";
            while (pos < line.size() && line[pos] != ' ') {
                sw.push_back(line[pos]);
                pos++;
            }
            int X = stoi(sx);
            unsigned int W = stoul(sw);
            int depth = tree.insert(X, W);
            globalTotal += W;
            // Após cada ADD, imprime o total global.
            cout << globalTotal << "\n";
        }
        // Se o comando for WEI
        else if (line.substr(0, 3) == "WEI") {
            // Formato: "WEI X"
            int pos = 3;
            while (pos < line.size() && line[pos] == ' ')
                pos++;
            string sx = "";
            while (pos < line.size() && line[pos] != ' ') {
                sx.push_back(line[pos]);
                pos++;
            }
            int X = stoi(sx);
            pair<unsigned int, int> res = tree.search(X);
            cout << res.first << " " << res.second << "\n";
        }
        // Se o comando for RNK
        else if (line.substr(0, 3) == "RNK") {
            // Formato: "RNK X"
            int pos = 3;
            while (pos < line.size() && line[pos] == ' ')
                pos++;
            string sx = "";
            while (pos < line.size() && line[pos] != ' ') {
                sx.push_back(line[pos]);
                pos++;
            }
            int X = stoi(sx);
            unsigned int sumLess = tree.queryRNK(X);
            cout << sumLess << "\n";
        }
    }
    
    return 0;
}
