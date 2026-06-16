from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        for (a,b) in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        group = 0
        for i in range(n):
            if i in visited:
                continue
            group += 1
            q = deque()
            q.append(i)
            while q:
                cur = q.popleft()
                visited.add(cur)
                for i in adj[cur]:
                    if i in visited:
                        continue
                    q.append(i)                 
                    
        return group