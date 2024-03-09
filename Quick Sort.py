# https://www.geeksforgeeks.org/problems/quick-sort/1

class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            q = self.partition(arr, low, high)
            self.quickSort(arr, low, q - 1)
            self.quickSort(arr, q + 1, high)

    def partition(self, arr, low, high):
        x = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1