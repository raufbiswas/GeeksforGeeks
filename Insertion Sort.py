# https://www.geeksforgeeks.org/problems/insertion-sort/1

#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        key = alist[index]
        j = index - 1
        while j >= 0 and key < alist[j]:
                alist[j+1] = alist[j]
                j -= 1
        alist[j+1] = key
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for i in range(1, n):
            self.insert(alist, i, n)