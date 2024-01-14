# https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

class Solution:
    def subArraySum(self, arr, n, s):
        left, right, total = 0, 0, 0
        if s < min(arr):
            return [-1]
        while right < n:
            total += arr[right]
            while total > s:
                total -= arr[left]
                left += 1
            if total == s:
                return [left + 1, right + 1]
            right += 1

        return [-1]