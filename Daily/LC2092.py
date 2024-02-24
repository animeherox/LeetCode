from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        visited = [False] * n
        visited[0] = visited[firstPerson] = True
        meetings.sort(key=lambda x: x[2])
        i, totalMeetings = 0, len(meetings)
        while i < totalMeetings:
            j = i
            while j+1 < totalMeetings and meetings[j+1][2] == meetings[i][2]:
                j += 1
            participants = set()
            connections = defaultdict(list)
            for a, b, _ in meetings[i:j+1]:
                connections[a].append(b)
                connections[b].append(a)
                participants.update([a, b])
            queue = deque([person for person in participants if visited[person]])
            while queue:
                currentPerson = queue.popleft()
                for person in connections[currentPerson]:
                    if not visited[person]:
                        visited[person] = True
                        queue.append(person)
            i = j + 1
        return [person for person, knows in enumerate(visited) if knows]
