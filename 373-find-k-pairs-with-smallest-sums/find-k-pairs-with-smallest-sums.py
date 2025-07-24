class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq
        if not nums1 or not nums2:
            return []
        
        min_heap = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        result = []
        while k > 0 and min_heap:
            sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        
        return result