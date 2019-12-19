from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = Counter(A[0])
        for a in A:
            ans &= Counter(a)
        # Counter define OR operation as returning the minimum value of the key
        return list(ans)
