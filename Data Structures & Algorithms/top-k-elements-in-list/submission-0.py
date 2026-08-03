class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        sorted_list = (sorted(hashmap.items(), key=lambda item: item[1],reverse=True))
        final_list = []
        for i in range(0,k):
            final_list.append(sorted_list[i][0])
        return final_list


        