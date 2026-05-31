class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        freq = {}
        for char in t:
            freq[char] = freq.get(char, 0) + 1

        l = 0
        ml = float('inf')
        st = 0
        c = 0

        for r in range(n):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    c += 1
                freq[s[r]] -= 1   # always decrement

            while c == len(t):
                if (r - l + 1) < ml:
                    ml = r - l + 1
                    st = l

                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        c -= 1
                l += 1

        return "" if ml == float('inf') else s[st:st+ml]