class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = []
        n = len(nums)
        for i in range(n):
            ans = nums[i]**2       
            s.append(ans)
            s.sort()
        
        return s