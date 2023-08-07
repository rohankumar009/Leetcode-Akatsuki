class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)

        for n in nums:
            count = sum(1 for i in nums if i == nums)
            
            if count > n / 2:
                return num

        return -1
