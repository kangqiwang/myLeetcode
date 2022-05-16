from typing import List
class Solution:
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack =[]
        for asteroid in asteroids:
            if asteroid >0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1]+ asteroid <0:
                    stack.pop()
                if asteroid+stack[-1]>0:
                    break
                elif asteroid + stack[-1] <0:
                    stack.pop()
                else:
                    stack.pop()
        return stack
    
    def asteroidCollision2(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] + a < 0:
                    print("while loop")
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] + a == 0:
                    stack.pop()
        return stack
    
    
print(Solution().asteroidCollision2([-10,1,2,5,-5,-10]))
            