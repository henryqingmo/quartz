### Idea
![[Pasted image 20251010154237.png|500]]
![[Pasted image 20251010154304.png]]
We want to build the set $L_{i}$ and so we start with the set at $L_{i-1}$, and visit each of their neighbours (distance at most i), and removing the one we visited (distance ≤ i - 1), and setting their previous node.

### Time Complexity

$O(|V| + |E|)$ We enqueued and dequeued each vertex → $O(|V|)$

For each vertex, we look at all of it’s edges so the worst case of undirected graph would have checked $2|E|$ times.

### Implementation
```python
def bfs(adj):
    V = len(adj)
    # create an array to store the traversal
    res = []
    s = 0
    from collections import deque
    q = deque()
    visited = [False] * V
    visited[s] = True
    q.append(s)
	# q = [remaining members in l_i - 1 ... , members in l_i]
	# Since we visiting the closest neiboughers first, they are
	# always at the front of the queue
    while q:
        u = q.popleft()
        res.append(curr)
       for v in adj[curr]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
    return res
```

#coding #algorithm #graph_theory #search



