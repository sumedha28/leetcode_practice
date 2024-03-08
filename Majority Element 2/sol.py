#Implemented in Python3
#Boyer Moore's Voting Algo Extension

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        minCount = n//3
        count1, count2 = 0, 0
        el1, el2 = float('-inf'), float('-inf')
        for i in range(n):
            if count1==0 and el2!=nums[i]:
                count1 = 1
                el1 = nums[i]
            elif count2==0 and el1!=nums[i]:
                count2 = 1
                el2 = nums[i]
            elif el1 == nums[i]:
                count1 += 1
            elif el2 == nums[i]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = 0
        count2 = 0
        for i in range(n):
            if el1==nums[i]:
                count1 += 1
            if el2== nums[i]:
                count2 += 1
        
        ans = []
        if count1>minCount:
            ans.append(el1)
        if count2>minCount:
            ans.append(el2)

        return ans
