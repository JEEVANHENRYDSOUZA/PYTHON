# two strings are said to be anagram if they contain the same number of characters but their ordering can be different

class Solution(object):
    def isAnagram(self, s, t):
        string1_dict={}
        string2_dict={}
        for char in s:
            if char in string1_dict:
                string1_dict[char]+=1
            else:
                string1_dict[char]=1
                
        for char in t:
            if char in string2_dict:
                string2_dict[char]+=1
            else:
                string2_dict[char]=1
                
                
                
        return string1_dict==string2_dict
