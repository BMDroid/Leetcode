class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        l = list(set(nums1).intersection(set(nums2)))
        lst = []
        for n in l:
            ln = [n] * min(c1[n], c2[n])
            lst.extend(ln)
        return lst
