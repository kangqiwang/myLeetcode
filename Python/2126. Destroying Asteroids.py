from platform import release
from tokenize import Triple
from typing import List
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids=sorted(asteroids)
        for i in asteroids:
            if mass >= i:
                mass+=i
            else:
                return False
        return True
        # return [mass - x for x in asteroids]
            
        
print(Solution().asteroidsDestroyed(10,[3,9,19,5,21]))
