import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        
        busy_servers = []  # stores (free_time, weight, index)
        ans = [0] * len(tasks)
        current_time = 0
        
        for j, task_time in enumerate(tasks):
            # Jump time forward if no servers are free and current_time is ahead of task arrival
            current_time = max(current_time, j)
            
            # Free up servers whose tasks have finished by current_time
            while busy_servers and busy_servers[0][0] <= current_time:
                _, w, i = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (w, i))
            
            # If still no servers are free, jump time to the next available server's release time
            if not free_servers:
                current_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= current_time:
                    _, w, i = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (w, i))
            
            # Assign the task to the best available server
            w, i = heapq.heappop(free_servers)
            ans[j] = i
            heapq.heappush(busy_servers, (current_time + task_time, w, i))
            
        return ans