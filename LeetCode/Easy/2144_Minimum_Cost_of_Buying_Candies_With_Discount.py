class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()

        add = 0
        count = 0

        for i in range(len(cost)-1, -1, -1):
            count += 1

            if count == 3:
                count = 0
                continue

            add += cost[i]

        return add