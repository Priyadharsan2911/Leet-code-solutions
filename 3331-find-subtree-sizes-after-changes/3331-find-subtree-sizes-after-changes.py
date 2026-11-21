from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        orig_adj = [[] for _ in range(n)]
        for i in range(1, n):
            orig_adj[parent[i]].append(i)

        new_parent = parent[:]
        last_seen = [-1] * 26

        def dfs_reparent(u: int) -> None:
            ch = ord(s[u]) - ord("a")
            prev_anc = last_seen[ch]
            if u != 0 and prev_anc != -1:
                new_parent[u] = prev_anc

            last_seen[ch] = u
            for v in orig_adj[u]:
                dfs_reparent(v)
            last_seen[ch] = prev_anc

        dfs_reparent(0)

        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [0] * n

        def dfs_size(u: int) -> int:
            size = 1
            for v in new_adj[u]:
                size += dfs_size(v)
            ans[u] = size
            return size

        dfs_size(0)
        return ans