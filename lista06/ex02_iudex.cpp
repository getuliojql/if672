#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

string strip(const string &s) {
    int start = 0;
    while (start < (int)s.size() && s[start] == ' ')
        start++;
    int end = (int)s.size() - 1;
    while (end >= start && s[end] == ' ')
        end--;
    string result;
    for (int i = start; i <= end; i++)
        result.push_back(s[i]);
    return result;
}

int stoi_noSTL(const string &s, int &pos) {
    return stoi(s);
}

struct Pair {
    int r, c;
};

class ManualQueue {
private:
    Pair* arr;
    int frontIndex, backIndex;
    int capacity;
public:
    ManualQueue(int cap) {
        arr = new Pair[cap];
        frontIndex = 0;
        backIndex = 0;
        capacity = cap;
    }
    ~ManualQueue() {
        delete[] arr;
    }
    bool isEmpty() {
        return (frontIndex == backIndex);
    }
    void push(Pair p) {
        arr[backIndex++] = p;
    }
    Pair pop() {
        return arr[frontIndex++];
    }
};

int bfs(int M, int N, int** lab, int startR, int startC) {
    int** dist = new int*[M];
    for(int i = 0; i < M; i++) {
        dist[i] = new int[N];
        for(int j = 0; j < N; j++)
            dist[i][j] = -1;
    }

    dist[startR][startC] = 0;
    ManualQueue q(M*N);
    q.push({startR, startC});
    
    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    while(!q.isEmpty()) {
        Pair front = q.pop();
        int r = front.r;
        int c = front.c;

        if(lab[r][c] == 3) {
            int ans = dist[r][c];
            for(int i = 0; i < M; i++) {
                delete[] dist[i];
            }
            delete[] dist;
            return ans;
        }
        
        for(int i = 0; i < 4; i++) {
            int rr = r + dr[i];
            int cc = c + dc[i];
            if(rr >= 0 && rr < M && cc >= 0 && cc < N) {
                if(lab[rr][cc] != 1 && dist[rr][cc] == -1) {
                    dist[rr][cc] = dist[r][c] + 1;
                    q.push({rr, cc});
                }
            }
        }
    }

    for(int i = 0; i < M; i++) {
        delete[] dist[i];
    }
    delete[] dist;
    return -1;
}

int main(int argc, char *argv[]) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    getline(cin, line);
    line = strip(line);
    int pos=0; 
    int i=0;
    string sM="", sN="";
    while(i<(int)line.size() && line[i]!=' '){
        sM.push_back(line[i]);
        i++;
    }
    while(i<(int)line.size() && line[i]==' ') i++;
    while(i<(int)line.size() && line[i]!=' '){
        sN.push_back(line[i]);
        i++;
    }
    int M = stoi(sM);
    int N = stoi(sN);

    int** lab = new int*[M];
    for(int r = 0; r < M; r++) {
        lab[r] = new int[N];
    }

    int startR=-1, startC=-1;
    for(int r=0; r<M; r++){
        getline(cin, line);
        line = strip(line);
        int idx=0;
        for(int c=0; c<N; c++){
            while(idx<(int)line.size() && line[idx]==' ') idx++;
            string num="";
            while(idx<(int)line.size() && line[idx]!=' '){
                num.push_back(line[idx]);
                idx++;
            }
            int val = stoi(num);
            lab[r][c] = val;
            if(val==2){
                startR=r; startC=c;
            }
        }
    }

    if(startR==-1 || startC==-1){
        cout<<"Labirinto Impossivel\n";
        for(int r=0; r<M; r++){
            delete[] lab[r];
        }
        delete[] lab;
        return 0;
    }

    int ans = bfs(M,N,lab,startR,startC);
    if(ans==-1) cout<<"Labirinto Impossivel\n";
    else cout<<ans<<"\n";

    for(int r=0; r<M; r++){
        delete[] lab[r];
    }
    delete[] lab;
    return 0;
}
