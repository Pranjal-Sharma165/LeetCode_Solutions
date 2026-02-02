class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        delta = (sumB - sumA) // 2
        setB = set(bobSizes)

        for x in aliceSizes:
            if x + delta in setB:
                return [x, x + delta]