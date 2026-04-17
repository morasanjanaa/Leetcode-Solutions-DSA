class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atMost(k):
            if k < 0:
                return 0
            
            last_seen = {}
            left = 0
            consonants = 0
            res = 0
            
            for right in range(len(word)):
                if word[right] in "aeiou":
                    last_seen[word[right]] = right
                else:
                    consonants += 1
                
                while consonants > k:
                    if word[left] not in "aeiou":
                        consonants -= 1
                    left += 1
                
                # check if all vowels are present
                if len(last_seen) == 5:
                    # minimum index among vowels
                    min_vowel_index = min(last_seen.values())
                    
                    if min_vowel_index >= left:
                        res += (min_vowel_index - left + 1)
            
            return res
        
        return atMost(k) - atMost(k - 1)