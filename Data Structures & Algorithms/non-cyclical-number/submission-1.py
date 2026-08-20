class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            if n in seen :
                return False
            seen.add(n)
            totalSum = 0
            while n > 0 :
                digit = n%10
                totalSum += digit**2
                n//=10

            n= totalSum
        return True