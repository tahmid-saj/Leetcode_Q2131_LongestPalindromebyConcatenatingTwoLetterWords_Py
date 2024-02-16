class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen, middle, res = {}, 0, 0
        for word in words:
            if word not in seen:
                seen[word[1] + word[0]] = seen.get(word[1] + word[0], 0) + 1
                if word[0] == word[1]: middle += 1
            elif word in seen:
                seen[word] -= 1
                if seen[word] == 0: seen.pop(word)
                res += 4
                if word[0] == word[1]: middle -= 1
        
        if middle >= 1: res += 2
        return res
