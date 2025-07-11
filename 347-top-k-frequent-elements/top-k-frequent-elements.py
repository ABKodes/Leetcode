class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for key,value in count.items():
            freq[value].append(key)
        result = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                result.append(j)
            if len(result) == k:
                return result