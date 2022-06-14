class Solution:
    def maxArea(self, height):
        max_area=0
        left=0
        right=len(height)-1
        while(left<right):
            height_area=min(height[left],height[right])
            distance=right-left
            area=distance*height_area
            max_area=max(area,max_area)
            if(height[left]<height[right]):
                left=left+1
            else:
                right=right-1
        return max_area
                    
                
        
