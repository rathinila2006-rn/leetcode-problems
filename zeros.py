class Solution(object):
    def zeroFilledSubarray(self, nums):
        count = 0
        zerocount = 0
        for i in nums:
            if i == 0:
                zerocount += 1
                count += zerocount
            else:
                zerocount = 0
        return count            
