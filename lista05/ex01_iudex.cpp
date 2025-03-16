#include <bits/stdc++.h>
#define endl '\n'

using namespace std;

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

struct Edge {
    int u, v;
    int cost;
};

int partition(Edge arr[], int low, int high) {
    Edge pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j].cost < pivot.cost) {
            i++;
            Edge temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    Edge temp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = temp;
    return i + 1;
}

void quicksort(Edge arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

int find(int parent[], int i) {
    if (parent[i] != i)
        parent[i] = find(parent, parent[i]);
    return parent[i];
}

void unionSets(int parent[], int rank[], int x, int y) {
    int xroot = find(parent, x);
    int yroot = find(parent, y);

    if (xroot == yroot)
        return;
    if (rank[xroot] < rank[yroot])
        parent[xroot] = yroot;
    else if (rank[xroot] > rank[yroot])
        parent[yroot] = xroot;
    else {
        parent[yroot] = xroot;
        rank[xroot]++;
    }
}

int main(int argc, char *argv[]) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    getline(cin, line);
    line = strip(line);
    int M, N;
    {
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
        M = stoi(s1);
        N = stoi(s2);
    }

    Edge *edges = new Edge[N];
    for (int i = 0; i < N; i++) {
        getline(cin, line);
        line = strip(line);

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

        string sc = "";
        while (pos < line.size() && line[pos] != ' ') {
            sc.push_back(line[pos]);
            pos++;
        }

        edges[i].u = stoi(su);
        edges[i].v = stoi(sv);
        edges[i].cost = stoi(sc);
    }

    quicksort(edges, 0, N - 1);

    int *parent = new int[M];
    int *rank = new int[M];
    for (int i = 0; i < M; i++) {
        parent[i] = i;
        rank[i] = 0;
    }

    int edgeCount = 0;
    long long totalCost = 0;
    for (int i = 0; i < N && edgeCount < M - 1; i++) {
        int u = edges[i].u;
        int v = edges[i].v;
        int setU = find(parent, u);
        int setV = find(parent, v);
        if (setU != setV) {
            totalCost += edges[i].cost;
            unionSets(parent, rank, setU, setV);
            edgeCount++;
        }
    }
    cout << totalCost << endl;

    delete [] edges;
    delete [] parent;
    delete [] rank;

    return 0;
}
