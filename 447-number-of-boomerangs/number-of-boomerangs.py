class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for i in points:
            distance_count = {}
            for j in points:
                if i == j:
                    continue
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                dist_sq = dx * dx + dy * dy
                distance_count[dist_sq] = distance_count.get(dist_sq, 0) + 1
            for count in distance_count.values():
                total += count * (count - 1)
        return total