class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        define a dict to map a course to its prereq's
        store path in visited, if a course is found in visited during prereq traversal then a cycle has been foudnd
        '''
        preMap = {i: [] for i in range(numCourses)}
        for key, val in prerequisites:
            preMap[key].append(val)
        print(prerequisites, preMap)
        visited = set()

        def dfs(node):
            print(visited)
            if node in visited:
                return False
            if preMap[node] == []:
                return True
            visited.add(node)

            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            visited.remove(node)
            preMap[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True