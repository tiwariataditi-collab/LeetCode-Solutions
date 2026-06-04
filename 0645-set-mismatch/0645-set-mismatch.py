class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = 0

        for x in nums:
            idx = abs(x) - 1

            if nums[idx] < 0:
                duplicate = abs(x)
            else:
                nums[idx] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return [duplicate , i +1]