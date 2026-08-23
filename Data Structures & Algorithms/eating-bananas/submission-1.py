class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while(left<right):
            mid = (left+right)//2
            timetaken = 0
            for num in piles:
                timetaken += math.ceil(num/mid)
            if timetaken<=h:
                right = mid
            else:
                left = mid+1
        return left
        