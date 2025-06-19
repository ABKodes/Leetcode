class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map={i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            pre_map[course].append(pre)
        visit=set()
        
        def dfs(course):
            if course in visit:
                return False
            if pre_map[course]==[]:
                return True
            visit.add(course)
            for pre in pre_map[course]:
                if not dfs(pre): return False
            visit.remove(course)
            pre_map[course]=[]
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        return True
            