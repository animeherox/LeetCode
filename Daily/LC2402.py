from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        busyHeap = []
        idleHeap = list(range(n))
        heapify(idleHeap)
        meetingCount = [0] * n
        for start, end in meetings:
            while busyHeap and busyHeap[0][0] <= start:
                room = heappop(busyHeap)[1]
                heappush(idleHeap, room)
            if idleHeap:
                room = heappop(idleHeap)
                meetingCount[room] += 1
                heappush(busyHeap, (end, room))
            else:
                earliestEnd, room = heappop(busyHeap)
                meetingCount[room] += 1
                heappush(busyHeap, (earliestEnd + end - start, room))
        mostBookedRoom = 0
        for i, count in enumerate(meetingCount):
            if meetingCount[mostBookedRoom] < count:
                mostBookedRoom = i
        return mostBookedRoom
