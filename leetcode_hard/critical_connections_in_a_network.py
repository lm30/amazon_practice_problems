class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.graph = collections.defaultdict(list)
        for connection in connections:
            self.graph[connection[0]].append(connection[1])
            self.graph[connection[1]].append(connection[0])
        
        self.visited = [False] * n
        # low id's from Tarjan's algorithm to help identify SCCs
        self.lowId = collections.defaultdict(dict)
        self.counter = 0 # for the low ids
        self.result = [] 
        
        def dfs(node, parent):
            if self.visited[node]:
                return
            
            self.visited[node] = True
            # initially, give the id and low for the node the same value. Change upon going back
            self.lowId[node]['id'] = self.counter
            self.lowId[node]['low'] = self.counter
            self.counter += 1
            
            for child in self.graph[node]:
                if child == parent:
                    continue
                dfs(child, node)
                if self.lowId[node]['id'] < self.lowId[child]['low']:
                    self.result.append([node, child])
                self.lowId[node]['low'] = min(self.lowId[node]['low'], self.lowId[child]['low'])
        
        dfs(0, -1)
        return self.result