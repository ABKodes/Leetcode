class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result = 0
        tank = 0
        indx = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            result += gas[i] - cost[i]
            
            if tank < 0:  
                indx = i + 1
                tank = 0
        
        if result >= 0:
            return indx 
        else:
            return -1