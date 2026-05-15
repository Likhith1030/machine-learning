class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0
        d = defaultdict(list)
        present = set()
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)

        def dfs(node):

            if node in present:
                return

            present.add(node)
            
            for el in d[node]:
                dfs(el)

            return
        

        for node in range(n):
            if node not in present:
                count += 1
                dfs(node)
        
        return count
