class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        ans = 0

        while i <= j:
            if i == j:
                ans += nums[i]      # only one element left
            else:
                ans += int(str(nums[i]) + str(nums[j]))

            i += 1
            j -= 1

        return ans