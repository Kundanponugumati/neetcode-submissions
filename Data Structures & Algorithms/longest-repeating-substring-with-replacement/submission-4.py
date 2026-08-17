class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest = 0
        # for i in range(len(s)):
        #     mp = {}
        #     max_feq = 0
        #     for j in range(i,len(s)):
        #         mp[s[j]] = mp.get(s[j],0)+1
        #         max_feq = max(max_feq,mp[s[j]])
        #         remaining = j-i+1 - max_feq
        #         if remaining <= k:
        #             longest = max(longest,j-i+1)
        #         else:
        #             break
        # return longest

        longest = 0
        start = 0
        mp = {}
        max_freq = 0
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i],0)+1
            max_freq = max(max_freq,mp[s[i]])
            eligible = i - start +1 - max_freq
            if eligible <=k:
                longest = max(longest,i-start+1)
            else:
                mp[s[start]] -=1
                start+=1
        return longest
                




