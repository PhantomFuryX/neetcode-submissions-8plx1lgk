class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()

        front = 0
        rear = len(s) - 1
        if(len(s) == 1):
            return True
        print(s)
        while (front < rear):
            while(front < rear and not s[front].isalnum()):
                front += 1
            while(front < rear and not s[rear].isalnum()):
                rear -= 1   
            if(s[front] == s[rear]):
                front += 1
                rear -= 1
            else:
                return False
        
        return True
        