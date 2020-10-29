class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        graph = collections.defaultdict(set)
        n = len(beginWord)
        for w in wordList:
            for i in range(n):
                key = w[:i] + '*' + w[i+1:]
                graph[key].add(w)
                
        parents = collections.defaultdict(set)
        visited = {beginWord:1}
        
        while visited and endWord not in parents:
            next_level = collections.defaultdict(set)
            for curr in visited:
                for i in range(n):
                    k = curr[:i] + '*' + curr[i+1:]
                    for nei in graph.get(k, []):
                        if nei not in parents:
                            next_level[nei].add(curr)
            visited = next_level
            parents.update(next_level)
            
        def backtrack(ret, temp, node):
            if node == beginWord:
                ret.append(list(temp[::-1]))
            else:
                for child in parents.get(node, []):
                    temp.append(child)
                    backtrack(ret, temp, child)
                    temp.pop()
        
        result = []
        backtrack(result, [endWord], endWord)
        return result