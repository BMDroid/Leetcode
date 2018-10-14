class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for i, p in enumerate(prices):
            if i < len(prices) - 1:
                profit = max(prices[i + 1::]) - p
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit

    def maxProfit2(self, prices):
        if len(prices) == 0:
            return 0
        maxP = 0
        minIndex = prices.index(min(prices))
        maxIndex = prices.index(max(prices))
        if minIndex <= maxIndex:
            maxP = prices[maxIndex] - prices[minIndex]
            return maxP
        maxP = max(Solution.maxProfit2(self, prices[0:maxIndex + 1]), Solution.maxProfit2(
            self, prices[maxIndex + 1:minIndex+1]), Solution.maxProfit2(self, prices[minIndex::]))
        return maxP

    def maxProfit3(self, prices):
        if len(prices) == 0:
            return 0
        maxP = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > minPrice:
                maxP = max(maxP, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return maxP


if __name__ == '__main__':
    s = Solution()
    prices = [1, 3, 5, 7, 1, 5, 3, 6, 4]
    # prices = [0, 0, 1]
    # prices = [7, 6, 4, 3, 1]
    print(s.maxProfit2(prices))
