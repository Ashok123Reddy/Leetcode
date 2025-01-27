class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Handle negative numbers and numbers ending in zero (except 0)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Step 2: Reverse half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Step 3: Check if the number is a palindrome
        # We check x == reversed_half or x == reversed_half // 10 (in case of odd length numbers)
        return x == reversed_half or x == reversed_half // 10
 