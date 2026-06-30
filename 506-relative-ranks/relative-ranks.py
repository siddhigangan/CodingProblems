class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)

        # store score with original index
        arr = []
        for i in range(n):
            arr.append((score[i], i))

        # sort in decreasing order of score
        arr.sort(reverse=True)

        res = [""] * n

        for rank in range(n):
            original_index = arr[rank][1]

            if rank == 0:
                res[original_index] = "Gold Medal"
            elif rank == 1:
                res[original_index] = "Silver Medal"
            elif rank == 2:
                res[original_index] = "Bronze Medal"
            else:
                res[original_index] = str(rank + 1)

        return res