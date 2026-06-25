class Solution:
    def reverseWords(self, s):
        # code here
        word_list = s.split(".")
        rev_words = []
        for i in range(len(word_list)-1,-1,-1):
            word = word_list[i].strip(".")
            if word:
                rev_words.append(word)
        return ".".join(rev_words)