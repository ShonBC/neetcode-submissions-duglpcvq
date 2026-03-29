class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        height = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]: # find root node
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: # Same root, cycle found
                return False
            if height[p1] > height[p2]: # join trees and increment height of tree
                par[p2] = p1
                height[p1] += height[p2]
            else:
                par[p1] = p2
                height[p2] += height[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        