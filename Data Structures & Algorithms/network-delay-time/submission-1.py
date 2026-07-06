import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        result = -1
        adj = {a:[] for a in range(1,n+1)}
        
        for (a,b,c) in times:
            adj[a].append((b,c))
        
        reached = {a:float('inf') for a in range(1,n+1)}
        reached[k] = 0

        heap = [(0,k)]
        visited = set()
        
        while heap:
            dist, cur = heapq.heappop(heap) 
            if cur in visited : continue
            visited.add(cur)

            for (c, v) in adj[cur]:
                if reached[c] > dist + v:
                    reached[c] = dist+v
                    heapq.heappush(heap, (dist+v, c))
    
        
        print(reached)
        
        result = max(reached.values())
        return result if result != float('inf') else -1