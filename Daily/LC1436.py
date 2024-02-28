from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set()
        dests = set()
        for source, dest in paths:
            sources.add(source)
            dests.add(dest)
        dests -= sources
        return list(dests)[0]
