class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkpal(text):
            cleaned = "".join(char.casefold() for char in text if char.isalnum())
            return cleaned == cleaned[::-1]

        if checkpal(s):
            return True
        else:
            for i in range(len(s)):
                news = s[:i] + s[i+1:]
                if checkpal(news):
                    return True
            return False