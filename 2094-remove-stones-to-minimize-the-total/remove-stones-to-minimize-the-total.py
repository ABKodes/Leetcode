class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-p for p in piles]
        heapq.heapify(maxHeap)

        for _ in range(k):
            largest = -heapq.heappop(maxHeap)
            reduced = largest - largest//2
            heapq.heappush(maxHeap, -reduced)
        
        return -sum(maxHeap)