from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = prerequisites
        edges =  defaultdict(list)
        for p in pre:
            src, dst = p
            edges[src].append(dst)
        
        visited = set()
        def dfs(cur):
            if cur in visited:
                return False
            if edges[cur] == []:
                return True

            visited.add(cur)
            for p in edges[cur]:
                if not dfs(p):
                    return False

            visited.remove(cur)
            edges[cur] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
