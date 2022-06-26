class Solution:
    def containsDuplicate(self, nums):
        hashmap={}
        count
        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap[i]=1
        return False
            
