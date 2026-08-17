class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mp1 = {}
        mp2 = {}

        for i in range(26):
            mp1[i] = 0
            mp2[i] = 0

        # Create first window
        for i in range(len(s1)):
            mp1[ord(s1[i]) - ord('a')] += 1
            mp2[ord(s2[i]) - ord('a')] += 1

        # Count matching frequencies
        matches = 0

        for i in range(26):
            if mp1[i] == mp2[i]:
                matches += 1

        l = 0

        for r in range(len(s1), len(s2)):

            # Check current window
            if matches == 26:
                return True

            # ----------------
            # Remove s2[l]
            # ----------------
            idx = ord(s2[l]) - ord('a')

            if mp1[idx] == mp2[idx]:
                matches -= 1

            mp2[idx] -= 1

            if mp1[idx] == mp2[idx]:
                matches += 1

            # ----------------
            # Add s2[r]
            # ----------------
            idx = ord(s2[r]) - ord('a')

            if mp1[idx] == mp2[idx]:
                matches -= 1

            mp2[idx] += 1

            if mp1[idx] == mp2[idx]:
                matches += 1

            l += 1

        return matches == 26


        
        
        