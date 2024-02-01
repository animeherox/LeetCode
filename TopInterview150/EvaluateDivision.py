from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Weight stores relative values of associated variables
        weight = defaultdict(lambda: 1.0)
        # Parent and find() keep track of associated equations
        parent = defaultdict(str)
        def find(x):
            if parent[x] != x:
                original_parent = parent[x]
                parent[x] = find(parent[x])
                weight[x] *= weight[original_parent]
            return parent[x]
        for a,b in equations:
            parent[a], parent[b] = a, b
        for i, value in enumerate(values):
            a, b = equations[i]
            root_a, root_b = find(a), find(b)
            # If equations are not already associated, combine them
            if root_a != root_b:
                parent[root_a] = root_b
                weight[root_a] = weight[b] * value / weight[a]
        # Process queries
        results = []
        for c,d in queries:
            if c not in parent or d not in parent or find(c) != find(d):
                results.append(-1)
            else:
                results.append(weight[c]/weight[d])
        return results