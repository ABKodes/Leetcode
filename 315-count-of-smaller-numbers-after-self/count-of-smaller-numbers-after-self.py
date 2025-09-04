class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        temp = [[num, index] for index, num in enumerate(nums)]

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    result.append(left[i])
                    counts[left[i][1]] += j
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                counts[left[i][1]] += j
                i += 1
            result.extend(right[j:])

            return result

        merge_sort(temp)
        return counts