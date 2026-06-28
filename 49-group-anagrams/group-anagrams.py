class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = defaultdict(list)
        result = []
        for i in strs:
            sort = tuple(sorted(i))
            pairs[sort].append(i)
        
        for key in pairs:
            result.append(pairs[key])

        return result
       