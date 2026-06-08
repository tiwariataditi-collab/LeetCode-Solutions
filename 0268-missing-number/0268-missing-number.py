class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expec_sum = n*(n+1)//2
        actual_sum = sum(nums)

        return expec_sum - actual_sum

        