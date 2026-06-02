class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):
        
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                lfin = landStartTime[i] + landDuration[i]
                wst = max(lfin, waterStartTime[j])
                ans = min(ans, wst + waterDuration[j])
                wfin = waterStartTime[j] + waterDuration[j]
                lst = max(wfin, landStartTime[i])
                ans = min(ans, lst + landDuration[i])

        return ans