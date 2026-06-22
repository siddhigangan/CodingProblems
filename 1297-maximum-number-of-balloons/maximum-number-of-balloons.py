class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0
        }
        for i in text.lower():
            if i in count:
                count[i] +=1

        can_b = count['b'] // 1
        can_a = count['a'] // 1
        can_l = count['l'] // 2
        can_o = count['o'] // 2
        can_n = count['n'] // 1

        return min(can_b,can_a,can_l,can_o,can_n)

            
