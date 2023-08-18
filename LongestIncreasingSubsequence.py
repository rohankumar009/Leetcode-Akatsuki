# Basic Brute force in O(n^2) time complexity

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
        n = len(nums)
        dp = [1] * n  # Initialize DP array with all values set to 1
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
