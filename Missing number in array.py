# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1

class Solution:
    def missingNumber(self,array,n):
        sum1toN = n*(n+1)//2
        sumArr = sum(array)
        return sum1toN - sumArr