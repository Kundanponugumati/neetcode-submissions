class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            # initalize an array of 26 char
            count = [0]*26
            for char in str:
                idx = ord(char) - ord("a")
                count[idx] +=1
            # store key as this count array and value as different strings
            res[tuple(count)].append(str)
        return list(res.values())

        