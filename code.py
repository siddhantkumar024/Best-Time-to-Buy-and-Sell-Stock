class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxval=0
        b=0
        s=1
        n=len(prices)
        while s<n:
            
            if prices[s]>prices[b]:
                curr=prices[s]-prices[b]
                maxval=max(maxval,curr)
                s+=1
            else :
                b=s
                s+=1
        return maxval

        
