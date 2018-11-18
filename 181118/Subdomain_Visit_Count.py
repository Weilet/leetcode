class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        ans = Counter()
        site_map = {}
        for domain in cpdomains:
            cnt, name = domain.split()
            cnt = int(cnt)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans['.'.join(frags[i:])] += cnt
        return ans
