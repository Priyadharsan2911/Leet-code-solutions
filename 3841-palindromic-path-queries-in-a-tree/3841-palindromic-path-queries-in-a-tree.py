import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)


class Solution:

    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        sz = [0] * n

        # 1. First DFS to find subtree sizes, heavy children, depths, and parents
        def dfs1(u, p, d):
            depth[u] = d
            parent[u] = p
            sz[u] = 1
            max_sz = 0
            for v in adj[u]:
                if v != p:
                    dfs1(v, u, d + 1)
                    sz[u] += sz[v]
                    if sz[v] > max_sz:
                        max_sz = sz[v]
                        heavy[u] = v

        dfs1(0, 0, 0)

        # 2. Second DFS to assign positions and chain heads for HLD
        cur_pos = 0

        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)

        dfs2(0, 0)

        # 3. Segment Tree over the flattened HLD array
        tree = [0] * (4 * n)
        masks = [1 << (ord(c) - ord("a")) for c in s]

        def build(node, l, r):
            if l == r:
                # Find the node corresponding to this position
                # We can precompute inv_pos or just store it
                return
            # Since we can build directly based on pos, let's map pos to initial masks
            pass

        # Mapping position to initial masks
        init_arr = [0] * n
        for i in range(n):
            init_arr[pos[i]] = 1 << (ord(s[i]) - ord("a"))

        def build_tree(node, l, r):
            if l == r:
                tree[node] = init_arr[l]
                return
            mid = (l + r) // 2
            build_tree(2 * node, l, mid)
            build_tree(2 * node + 1, mid + 1, r)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]

        build_tree(1, 0, n - 1)

        def update_tree(node, l, r, idx, val):
            if l == r:
                tree[node] = val
                return
            mid = (l + r) // 2
            if idx <= mid:
                update_tree(2 * node, l, mid, idx, val)
            else:
                update_tree(2 * node + 1, mid + 1, r, idx, val)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]

        def query_tree(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            return query_tree(2 * node, l, mid, ql, qr) ^ query_tree(
                2 * node + 1, mid + 1, r, ql, qr
            )

        # 4. HLD Path Query
        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= query_tree(1, 0, n - 1, pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query_tree(1, 0, n - 1, pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord("a"))
                update_tree(1, 0, n - 1, pos[u], new_mask)
            else:
                u = int(parts[1])
                v = int(parts[2])
                path_mask = query_path(u, v)
                # A bitmask forms a palindrome if it has at most one bit set
                if (path_mask & (path_mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)

        return ans