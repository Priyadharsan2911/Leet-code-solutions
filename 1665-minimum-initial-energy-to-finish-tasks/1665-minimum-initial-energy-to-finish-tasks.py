class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # Sort tasks by difference (minimum - actual) in descending order
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        current_energy = 0
        total_required = 0
        
        for actual, minimum in tasks:
            if current_energy < minimum:
                total_required += (minimum - current_energy)
                current_energy = minimum
            current_energy -= actual
            
        return total_required