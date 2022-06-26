class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        num_lastpos_dict = {}
        
        for idx, number in enumerate(nums):
            
            if idx - num_lastpos_dict.get(number, -float(inf) ) <= k:
                
                # numbers are the same in two different indices within distance k
                return True
           
            # update lastest position for currnet number
            num_lastpos_dict[number] = idx
        
        return False
