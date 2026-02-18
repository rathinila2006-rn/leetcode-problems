class Solution(object):
    def majorityElement(self, nums):
        canditate=nums[0]
        count=1
        for i in range(1,len(nums)):
            if count==0:
                canditate=nums[i]
                count = 1
            elif nums[i] == canditate:
                count +=1
            else:
                count -= 1
        return canditate                
