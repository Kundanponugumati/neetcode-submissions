class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod,zeros = 1,0
        for num in nums:
            if(num==0):
                zeros +=1
            else:
                prod = prod*num
        if zeros>=2:
            return [0]*len(nums)
        if zeros==1:
            for num in nums:
                if num ==0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        if zeros<1:
            for num in nums:
                res.append(int(prod/num))
            return res

            



        