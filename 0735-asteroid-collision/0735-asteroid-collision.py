class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                Survive = True
                while(Survive == True and stack):
                    top = stack[-1]
                    if top < 0:
                        break
                    if top > -i:
                        Survive = False
                    elif top == -i:
                        Survive = False
                        stack.pop()
                    else:
                        stack.pop()
                if Survive == True:
                    stack.append(i)
        return stack

       