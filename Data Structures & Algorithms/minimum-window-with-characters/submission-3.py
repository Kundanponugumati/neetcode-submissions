class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if m>n:
            return ""
        min_length = len(s)+1  
        # sliding window approach
        hasharr = [0]*256
        for i in range(m):
            hasharr[ord(t[i])]+=1
        count = 0
        #take left and right pointer and start window
        start_idx,end_idx = -1,-1
        l = 0
        r = 0
        while(r<n):
            if hasharr[ord(s[r])]>0:
                count +=1       
            hasharr[ord(s[r])]-=1
            while(count == m):
                if r-l+1 < min_length:
                    min_length = r-l+1
                    start_idx = l
                    end_idx = r
                if hasharr[ord(s[l])]<0:
                    hasharr[ord(s[l])] +=1
                else:
                    count -=1
                    hasharr[ord(s[l])] +=1
                l+=1                 
            r+=1
        return s[start_idx:end_idx+1]
        