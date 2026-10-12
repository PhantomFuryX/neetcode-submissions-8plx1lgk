# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
        #ans.append(list(pairs))
        #print(ans)
        for i in range(len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                print("value is greater. exchanging")
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            ans.append(list(pairs))
            #print(ans)
        return ans

        