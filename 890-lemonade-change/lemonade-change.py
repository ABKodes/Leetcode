class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billsCount = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                billsCount[bill] +=1
            elif bill == 10:
                if billsCount[5] > 0:
                    billsCount[5] -= 1
                    billsCount[bill] +=1
                else:
                    return False
            else:
                if billsCount[10] > 0 and billsCount[5] > 0:
                    billsCount[10] -=1
                    billsCount[5] -=1
                    billsCount[20] +=1
                elif billsCount[5] >=3:
                    billsCount[5] -= 3
                    billsCount[20] +=1
                else:
                    return False
        return True