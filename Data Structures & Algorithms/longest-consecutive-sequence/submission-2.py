class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set()
        for num in nums:
            hashset.add(num)
        
        # now we are having everything in set so check whether an elemenet is having left neighbour
        count = 1
        max_count = 1
        for num in nums:
            if num-1 in hashset:
                continue
            else:
                count = 1
                #now num is the start of sequenece
                current = num
                while(current+1 in hashset):
                    count +=1
                    current+=1
            max_count = max(count,max_count)
        return max_count
                    


        