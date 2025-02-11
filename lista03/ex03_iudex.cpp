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

// Mapeamento de jogadores:
// - nameMap: mapeia o nome para a pontuação.
// - ranking: mapeia a pontuação para o nome (ordenado em ordem crescente).
// Todos os nomes e pontuações são únicos.

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int K;
    string line;
    
    // Lê o número de comandos e remove espaços indesejados.
    getline(cin, line);
    line = strip(line);
    K = stoi(line);
    
    unordered_map<string, int> nameMap; // nome -> pontuação
    map<int, string> ranking;             // pontuação -> nome
    
    for (int i = 0; i < K; i++) {
        getline(cin, line);
        line = strip(line);
        if (line == "") {
            i--;
            continue;
        }
        
        istringstream iss(line);
        string cmd;
        iss >> cmd;
        
        if (cmd == "ADD") {
            string name;
            int score;
            iss >> name >> score;
            // Se o jogador já estiver no sistema.
            if (nameMap.find(name) != nameMap.end()) {
                cout << name << " ja esta no sistema." << endl;
            } else {
                nameMap[name] = score;
                ranking[score] = name;
                cout << name << " inserido com sucesso!" << endl;
            }
        }
        else if (cmd == "PROX") {
            int score;
            iss >> score;
            // Procura o jogador com a pontuação score.
            auto it = ranking.find(score);
            string playerName = it->second;
            
            // Determina o predecessor.
            auto pred = it;
            bool hasPred = false;
            if (it != ranking.begin()) {
                pred--;
                hasPred = true;
            }
            
            // Determina o sucessor.
            auto succ = it;
            succ++;
            bool hasSucc = (succ != ranking.end());
            
            // Formata a saída conforme as proximidades.
            if (!hasPred && !hasSucc) {
                cout << "Apenas " << playerName << " existe no sistema..." << endl;
            }
            else if (!hasPred && hasSucc) {
                cout << playerName << " e o menor! e logo apos vem " << succ->second << endl;
            }
            else if (hasPred && !hasSucc) {
                cout << playerName << " e o maior! e logo atras vem " << pred->second << endl;
            }
            else {
                cout << playerName << " vem apos " << pred->second << " e antes de " << succ->second << endl;
            }
        }
    }
    
    return 0;
}
