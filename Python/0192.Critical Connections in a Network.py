class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adjlist = [[] for _ in range(n)]
        
        for src,dst in connections:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        
        visited = [-1]* n
        timestamp = [0]
        lowestarr = [-1]*n
        result =[]
        arrival = [-1]*n
        parent = {}
        parent[0] = None
        
        
        def dfs(node):
            arrival[node] = timestamp[0]+1
            timestamp[0] += 1
            lowestarr[node] = arrival[node]
            visited[node] = 1
            for nbr in adjlist[node]:
                if visited[nbr] == -1:
                    parent[nbr] = node
                    visited[nbr] = 1
                    lowestarr[node] = min(lowestarr[node], dfs(nbr))
                elif parent[node] != nbr:
                        lowestarr[node] = min(arrival[nbr], lowestarr[node])
            
            if arrival[node] == lowestarr[node] and node != 0:
                result.append((node, parent[node]))
            
            return lowestarr[node]
        
        dfs(0)
        return result
