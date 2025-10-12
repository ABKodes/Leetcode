class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = {id}
        queue = deque([id])
        
        for _ in range(level):
            for _ in range(len(queue)):
                person = queue.popleft()
                for f in friends[person]:
                    if f not in visited:
                        visited.add(f)
                        queue.append(f)
        
        freq = Counter()
        for person in queue:
            freq.update(watchedVideos[person])
        return sorted(freq.keys(), key=lambda x: (freq[x], x))
            
            