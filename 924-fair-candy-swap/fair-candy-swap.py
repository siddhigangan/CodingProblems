# class Solution:
#     def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
#         result = []
#         n = sum(aliceSizes)
#         m = sum(bobSizes)
#         diff = (n-m)/2
#         for i in aliceSizes:
#             for j in bobSizes:
#                 if(i-j == diff):
#                     result.append(i)
#                     result.append(j)
#         return list(set(result))
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        n = sum(aliceSizes)
        m = sum(bobSizes)
        
        diff = (n - m) // 2 
        bob_set = set(bobSizes)
        for i in aliceSizes:
            j = i - diff 
            if j in bob_set:
                return [i, j] 
