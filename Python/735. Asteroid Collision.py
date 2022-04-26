from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack =[]
        for asteroid in asteroids:
            while stack:
                break
            else:
                stack.append(asteroid)
        return stack
print(Solution().asteroidCollision([5,1,-5]))
            