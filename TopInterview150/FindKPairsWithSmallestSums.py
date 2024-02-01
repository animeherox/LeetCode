from heapq import heapify, heappop, heappush

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Initialize heap with sums and indices of some candidate pairs
        pq = [[u + nums2[0], i, 0] for i, u in enumerate(nums1[:k])]
        heapify(pq)
        pairs = []
        while pq and k > 0:
            sum, i_1, i_2 = heappop(pq)
            pairs.append([nums1[i_1], nums2[i_2]])
            k -= 1
            if i_2 + 1 < len(nums2):
                # If possible, pair the element from nums1 with the next element of
                # nums2 as the next possible candidate
                heappush(pq, [nums1[i_1] + nums2[i_2 + 1], i_1, i_2 + 1])
        return pairs
