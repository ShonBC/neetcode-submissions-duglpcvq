class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        start at end of cost, update the cost to get to each index with
        min cost for step to either i + 1 or i + 2
        update cost[i] += min cost for each step
        once step out of range, return min cost[0] or cost[1]
        '''

        for i in range(len(cost) - 3, -1, -1):
                cost[i] += min(cost[i+1], cost[i + 2])
                print(i, cost)

        return min(cost[0], cost[1])
        