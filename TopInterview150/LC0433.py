from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        mutations = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        bankSet = set(bank) # Convert to set for O(1) lookups
        queue = deque([(startGene, 0)]) # Create queue of genes and step counts

        while queue:
            currentGene, stepCount = queue.popleft()
            if currentGene == endGene:
                return stepCount
            for i, base in enumerate(currentGene):
                for mutation in mutations[base]:
                    nextGene = currentGene[:i] + mutation + currentGene[i+1:]
                    if nextGene in bankSet:
                        queue.append((nextGene, stepCount+1))
                        bankSet.remove(nextGene)
        
        # If all possible mutation paths are exhausted, it must be impossible
        return -1