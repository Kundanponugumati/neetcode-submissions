class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        mp1 = {}
        for i in range(len(s1)):
            mp1[s1[i]] = mp1.get(s1[i],0)+1
        mp2 = {}
        for i in range(len(s1)):
            mp2[s2[i]] = mp2.get(s2[i],0)+1
        if mp2 == mp1:
            return True
        start = 0
        right = len(s1)
        while(right<len(s2)):
            mp2[s2[start]] = mp2.get(s2[start],0)-1
            if mp2[s2[start]] == 0:
                del mp2[s2[start]]
            mp2[s2[right]] = mp2.get(s2[right],0)+1
            if mp2 == mp1:
                return True
            start +=1
            right+=1
        return False



        