class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = 0
        if len(arr) <= 1:
            return [-1]
        for i in range(len(arr) - 1):
            print(arr[i:])
            arr[k] = max(arr[i + 1:])
            print(i, arr[i], k)
            k += 1
        arr[i + 1] = -1

        return arr
            
        