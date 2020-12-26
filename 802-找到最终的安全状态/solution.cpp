#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

class Solution
{
public:
    vector<int> eventualSafeNodes(vector<vector<int>> &graph){
        unordered_set<int> cycle;
        unordered_set<int> acycle;
        vector<int> ret;
        for (int i = 0; i < graph.size(); i++){
            if(cycle.find(i) != cycle.end()){
                continue;
            }
            if(acycle.find(i) != acycle.end()){
                ret.push_back(i);
                continue;
            }
            unordered_set<int> path;
            unordered_set<int> visited;
            bool flag = this->cycle(graph, i, path, visited);
            if(flag){
                handler(path, cycle);
            }else{
                ret.push_back(i);
                handler(visited, acycle);
            }
        }
        return ret;
    }

    void handler(unordered_set<int> &source, unordered_set<int> &target){
        for (auto iter = source.begin(); iter != source.end(); iter++){
            target.insert(*iter);
        }   
    }

    bool cycle(vector<vector<int>> &graph, int v, unordered_set<int> &path, unordered_set<int> &visited){
        visited.insert(v);
        path.insert(v);
        for (int i = 0; i < graph[v].size(); i++){
            if(path.find(graph[v][i]) != path.end()){
                return true;
            }
            if(cycle(graph, graph[v][i], path, visited)){
                return true;
            }
        }
        path.erase(v);
        return false;
    }
};