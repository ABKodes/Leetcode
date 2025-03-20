class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        current_fruits = 0
        fruit_counter = {}
        left = 0

        for right in range(len(fruits)):
            fruit_counter[fruits[right]] = fruit_counter.get(fruits[right], 0) + 1
            current_fruits += 1

            while len(fruit_counter) > 2:
                fruit_counter[fruits[left]] -= 1
                if fruit_counter[fruits[left]] == 0:
                    del fruit_counter[fruits[left]]
                current_fruits -= 1
                left += 1 
            
            max_fruits = max(max_fruits, current_fruits)
        
        return max_fruits