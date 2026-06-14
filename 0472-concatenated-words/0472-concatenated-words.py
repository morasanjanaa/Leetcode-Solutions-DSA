from functools import lru_cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Step 1 : convert the words into set
        # step 2 : for each word and each character check if prefix and suffix in set by is_concat function
        # step 3: so if prefix is a word in set then there are 2 cases 
        # step 4: case 1: suffix is also a word in set
        # step 5 : case 2 suffix is a isConcat word and then true
        # step 6 : return True and append to ans 
        @lru_cache(None)
        def is_concat(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set:
                    if suffix in word_set:
                        return True
                    if is_concat(suffix):
                        return True
            return False
        word_set = set(words)
        ans = []
        for word in words:
            word_set.remove(word)
            if is_concat(word):
                ans.append(word)
            word_set.add(word)
        return ans