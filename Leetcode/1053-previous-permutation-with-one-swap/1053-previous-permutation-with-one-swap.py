class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        size = len(arr)
        i, j = size - 2, size - 1        
        while i >= 0 and arr[i] <= arr[i + 1]: 
            i -= 1        
        if i < 0:
            return arr
        
        while j > i and arr[j] >= arr[i]: 
            j -= 1

        while arr[j] == arr[j - 1]: 
            j -= 1

      
        arr[i], arr[j] = arr[j], arr[i]
        return arr
