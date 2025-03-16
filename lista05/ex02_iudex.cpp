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

    void add(const T &obj) {
        if (count >= capacity)
            resize();
        arr[count++] = obj;
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

struct Road {
    int v;
    int cost;
};

int dijkstra(int Q, ObjectArrayList<Road> **graph, int src, int dst) {
    const int INF = 1e9;
    int dist[310];
    bool used[310];

    for (int i = 0; i < Q; i++) {
        dist[i] = INF;
        used[i] = false;
    }
    dist[src] = 0;
    for (int i = 0; i < Q; i++) {
        int u = -1, best = INF;
        for (int j = 0; j < Q; j++) {
            if (!used[j] && dist[j] < best) {
                best = dist[j];
                u = j;
            }
        }
        if (u == -1)
            break;
        used[u] = true;
        int sz = graph[u]->size();

        for (int j = 0; j < sz; j++) {
            Road r = graph[u]->get(j);
            if (dist[u] + r.cost < dist[r.v])
                dist[r.v] = dist[u] + r.cost;
        }
    }
    return (dist[dst] == INF) ? -1 : dist[dst];
}

int main(int argc, char *argv[]) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    getline(cin, line);
    line = strip(line);
    int Q, R, N;
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

        while (i < line.size() && line[i] == ' ')
            i++;

        string s3 = "";
        while (i < line.size() && line[i] != ' ') {
            s3.push_back(line[i]);
            i++;
        }
        Q = stoi(s1);
        R = stoi(s2);
        N = stoi(s3);
    }

    ObjectArrayList<Road> **graph = new ObjectArrayList<Road>*[Q];
    for (int i = 0; i < Q; i++) {
        graph[i] = new ObjectArrayList<Road>(4);
    }

    for (int i = 0; i < R; i++) {
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
        int A = stoi(su);
        int B = stoi(sv);
        int Mcost = stoi(sc);

        Road r;
        r.v = B;
        r.cost = Mcost;
        graph[A]->add(r);
    }

    for (int i = 0; i < N; i++) {
        getline(cin, line);
        line = strip(line);

        if (line =="")
            continue;

        if (line[0] == '1') {
            int pos = 1;
            while (pos < line.size() && line[pos] == ' ')
                pos++;

            string sA = "";
            while (pos < line.size() && line[pos] != ' ') {
                sA.push_back(line[pos]);
                pos++;
            }

            while (pos < line.size() && line[pos] == ' ')
                pos++;

            string sB = "";
            while ( pos < line.size() && line[pos] != ' ') {
                sB.push_back(line[pos]);
                pos++;
            }

            while (pos < line.size() && line[pos] == ' ')
                pos++;

            string sM = "";
            while (pos < line.size() && line[pos] != ' ') {
                sM.push_back(line[pos]);
                pos++;
            }
            int A = stoi(sA);
            int B = stoi(sB);
            int Mcost = stoi(sM);

            Road r;
            r.v = B;
            r.cost = Mcost;
            graph[A]->add(r);
        }

        else if (line[0] == '2') {
            int pos = 1;
            while (pos < line.size() && line[pos] == ' ')
                pos++;

            string sA = "";
            while (pos < line.size() && line[pos] != ' ') {
                sA.push_back(line[pos]);
                pos++;
            }

            while (pos < line.size() && line[pos] == ' ')
                pos++;
            
            string sB = "";
            while (pos < line.size() && line[pos] != ' ') {
                sB.push_back(line[pos]);
                pos++;
            }
            int A = stoi(sA);
            int B = stoi(sB);
            int ans = dijkstra(Q, graph, A, B);

            cout << ans << "\n";
        }
    }
    for (int i = 0; i < Q; i++) {
        delete graph[i];
    }
    delete [] graph;

    return 0;
}
