class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(" ")
        # print(list_s)
        if len(pattern) != len(list_s):
            return False
        map_ptos = {}
        map_stop = {}

        for x,y in zip(pattern,list_s):
            if(x in map_ptos):
                if(map_ptos[x] != y):
                    return False
            else:
                map_ptos[x] = y
            if(y in map_stop):
                if(map_stop[y] != x):
                    return False
            else:
                map_stop[y] = x
        return True