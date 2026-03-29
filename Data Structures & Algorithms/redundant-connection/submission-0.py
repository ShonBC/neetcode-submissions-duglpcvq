

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = {key : [] for key in range(1, n + 1)}
        ans = []
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visit = [False] * (n + 1)
        cycle = set()
        cstart = -1

        def dfs(node, par):
            nonlocal cstart
            if visit[node]:
                cstart = node
                return True
            visit[node] = True
            for nei in adjList[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cstart != -1:
                        cycle.add(node)
                    if node == cstart:
                        cstart = -1
                    return True
            return False
        
        dfs(1, -1)
        for i, j in reversed(edges):
            if i in cycle and j in cycle:
                return [i, j]
        return []