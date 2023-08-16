class Solution:

# In bruteforce method:

    def isPalindrome(self, s: str) -> bool:
        org = 0
        rev = len(s) - 1
        
        while org < rev:
            
            while org < rev and s[org].isalnum() == False: 
                org += 1
            
            while rev > org and s[rev].isalnum() == False: 
                rev -= 1

            if org > rev or s[org].lower() != s[rev].lower():
                return False
            
            else:
                org += 1
                rev -= 1

        return True
