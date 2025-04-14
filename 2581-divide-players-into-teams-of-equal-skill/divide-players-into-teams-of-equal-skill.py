class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        totalSkill = skill[left] + skill[right]
        result = 0
        while left < right:
            if skill[left+1] + skill[right-1] != totalSkill:
                result = -1
                break
            else:
                result = result + (skill[left] * skill[right])
                left += 1
                right -= 1
        return result