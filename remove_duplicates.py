class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        writepos =0
        for readpos in range(1,len(nums)):
            if nums[readpos] != nums[writepos]:
                writepos +=1
                nums[writepos] = nums[readpos]
        return writepos+1            
        
