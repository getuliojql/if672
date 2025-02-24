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

// Estrutura Pair: representa (T, C)
// T: timestamp (unsigned int); C: cliente (unsigned int)
struct Pair {
    unsigned int T;
    unsigned int C;
};

// Classe ObjectArrayList: vetor dinâmico genérico.
template <typename T>
class ObjectArrayList {
private:
    T* arr;
    int capacity;
    int count;
    void resize() {
        int newCapacity = capacity * 2;
        T* newArr = new T[newCapacity];
        for (int i = 0; i < count; i++)
            newArr[i] = arr[i];
        delete [] arr;
        arr = newArr;
        capacity = newCapacity;
    }
public:
    ObjectArrayList(int initCapacity = 4) {
        capacity = initCapacity;
        arr = new T[capacity];
        count = 0;
    }
    ~ObjectArrayList() {
        delete [] arr;
    }
    // Adiciona elemento no final.
    void add(const T &obj) {
        if (count >= capacity)
            resize();
        arr[count++] = obj;
    }
    // Insere elemento na posição index, deslocando os demais.
    void add_at(int index, const T &obj) {
        if (index < 0 || index > count)
            throw "Index out of range";
        if (count >= capacity)
            resize();
        for (int i = count; i > index; i--)
            arr[i] = arr[i-1];
        arr[index] = obj;
        count++;
    }
    T get(int index) const {
        if (index < 0 || index >= count)
            throw "Index out of range";
        return arr[index];
    }
    int size() const {
        return count;
    }
};

// Função binarySearch: encontra o índice onde inserir um par com timestamp T.
int binarySearch(const ObjectArrayList<Pair> &bucket, unsigned int T) {
    int lo = 0, hi = bucket.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (bucket.get(mid).T < T)
            lo = mid + 1;
        else
            hi = mid;
    }
    return lo;
}

// Função insert_sorted: insere p na lista ordenada por T e retorna a posição de inserção.
int insert_sorted(ObjectArrayList<Pair> &bucket, const Pair &p) {
    int pos = binarySearch(bucket, p.T);
    bucket.add_at(pos, p);
    return pos;
}

// Implementação de quicksort para um array de Pair, usando seleção aleatória de pivô.
void quickSort(Pair arr[], int low, int high) {
    if (low < high) {
        int pivotIndex = low + rand() % (high - low + 1);
        Pair temp = arr[pivotIndex];
        arr[pivotIndex] = arr[high];
        arr[high] = temp;
        unsigned int pivot = arr[high].T;
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j].T < pivot) {
                i++;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;
        int pi = i + 1;
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Classe Hashtable: armazena pares (T, C) usando open hashing com listas ordenadas.
class Hashtable {
private:
    ObjectArrayList< ObjectArrayList<Pair>* > *table; // vetor dinâmico de ponteiros para listas de Pair.
    int M;         // tamanho da tabela.
    float Lmax;    // fator de carga máximo.
    int total;     // total de pares armazenados.
    
    // Realiza rehashing: nova tabela de tamanho 2*M+1, reinserindo os pares.
    void rehash() {
        int oldM = M;
        M = 2 * M + 1;
        ObjectArrayList< ObjectArrayList<Pair>* > *newTable = new ObjectArrayList< ObjectArrayList<Pair>* >(M);
        // Inicializa as novas listas para cada bucket.
        for (int i = 0; i < M; i++) {
            newTable->add(new ObjectArrayList<Pair>());
        }
        // Coleta todos os pares da tabela antiga.
        Pair* allPairs = new Pair[total];
        int idx = 0;
        for (int i = 0; i < oldM; i++) {
            ObjectArrayList<Pair>* bucket = table->get(i);
            for (int j = 0; j < bucket->size(); j++) {
                allPairs[idx++] = bucket->get(j);
            }
            delete bucket;
        }
        delete table;
        table = newTable;
        // Ordena os pares usando quicksort.
        quickSort(allPairs, 0, total - 1);
        // Reinsere os pares na nova tabela.
        for (int i = 0; i < total; i++) {
            Pair p = allPairs[i];
            int index = p.T % M;
            ObjectArrayList<Pair>* bucket = table->get(index);
            bucket->add(p); // Já estão ordenados globalmente.
        }
        delete [] allPairs;
    }
    
public:
    Hashtable(int initM, float LmaxVal) {
        M = initM;
        Lmax = LmaxVal;
        total = 0;
        table = new ObjectArrayList< ObjectArrayList<Pair>* >(M);
        // Inicializa cada bucket com uma lista vazia.
        for (int i = 0; i < M; i++) {
            table->add(new ObjectArrayList<Pair>());
        }
    }
    ~Hashtable() {
        for (int i = 0; i < M; i++) {
            delete table->get(i);
        }
        delete table;
    }
    // Insere um par (T, C) na tabela; imprime "I S" (bucket e tamanho da lista).
    void insert(unsigned int T, unsigned int C) {
        float L = (float)total / M;
        if (L > Lmax) {
            rehash();
        }
        Pair p;
        p.T = T;
        p.C = C;
        int index = T % M;
        ObjectArrayList<Pair>* bucket = table->get(index);
        insert_sorted(*bucket, p);
        total++;
        cout << index << " " << bucket->size() << "\n";
    }
    // Consulta a tabela para o timestamp T; imprime "C J" se encontrado, ou "-1 -1" se não.
    void query(unsigned int T) {
        int index = T % M;
        ObjectArrayList<Pair>* bucket = table->get(index);
        int pos = -1;
        for (int i = 0; i < bucket->size(); i++) {
            if (bucket->get(i).T == T) {
                pos = i;
                break;
            }
        }
        if (pos == -1)
            cout << "-1 -1" << "\n";
        else
            cout << bucket->get(pos).C << " " << pos << "\n";
    }
};

int main(int argc, char *argv[]) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int initM;
    float Lmax;
    string line;
    getline(cin, line);
    line = strip(line);
    // A primeira linha contém "M Lmax".
    int i = 0;
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
    initM = stoi(s1);
    Lmax = stof(s2);
    
    Hashtable ht(initM, Lmax);
    
    while (getline(cin, line)) {
        line = strip(line);
        if (line == "END")
            break;
        if (line.substr(0, 3) == "NEW") {
            // Formato: "NEW T C"
            int pos = 3;
            while (pos < line.size() && line[pos] == ' ')
                pos++;
            string st = "";
            while (pos < line.size() && line[pos] != ' ') {
                st.push_back(line[pos]);
                pos++;
            }
            while (pos < line.size() && line[pos] == ' ')
                pos++;
            string sc = "";
            while (pos < line.size() && line[pos] != ' ') {
                sc.push_back(line[pos]);
                pos++;
            }
            unsigned int T = strtoul(st.c_str(), nullptr, 10);
            unsigned int C = strtoul(sc.c_str(), nullptr, 10);
            ht.insert(T, C);
        }
        else if (line.substr(0, 3) == "QRY") {
            // Formato: "QRY T"
            int pos = 3;
            while (pos < line.size() && line[pos] == ' ')
                pos++;
            string st = "";
            while (pos < line.size() && line[pos] != ' ') {
                st.push_back(line[pos]);
                pos++;
            }
            unsigned int T = strtoul(st.c_str(), nullptr, 10);
            ht.query(T);
        }
    }
    
    return 0;
}
