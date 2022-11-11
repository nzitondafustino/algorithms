class Solution:
    def divisorGame(self, n: int) -> bool:
        times = 0
        i = 1
        while n > 1:
            if n % i == 0:
                times += 1
                n-=i
                i = 1
            else:
                i += 1
        return False if not (times % 2) else True