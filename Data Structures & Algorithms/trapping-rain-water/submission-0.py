class Solution:
    def trap(self, height: List[int]) -> int:
        #max_height array 
        left_max = [0]*len(height)
        right_max = [0]*len(height)
        max_left = 0
        for i,num in enumerate(height):
            if num>max_left:
                max_left = num
            left_max[i] = max_left
        max_right = 0
        for i in range(len(height)-1,-1,-1):
            if height[i]>max_right:
                max_right=height[i]
            right_max[i] = max_right

        # now for calcuation we apply value = min(L,R) - h[i]
        area = 0
        for i in range(len(height)-1):
            if min(left_max[i],right_max[i])-height[i] >0:
                area += min(left_max[i],right_max[i])-height[i]
        return area



