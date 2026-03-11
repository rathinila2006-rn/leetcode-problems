class Solution(object):
    def getSum(self, a, b):
        mask=0xffffffff
        max_init=0x7fffffff
        while b!=0:
            carry =(a&b) << 1
            a=(a^b) & mask
            b=carry & mask
        if a <= max_init:
            return a
        else:
            return ~(a^mask)        
