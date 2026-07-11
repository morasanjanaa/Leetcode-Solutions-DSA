class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            survive = True

            while stack and asteroid < 0 and stack[-1] > 0:

                if stack[-1] < -asteroid:
                    stack.pop()

                elif stack[-1] == -asteroid:
                    stack.pop()
                    survive = False
                    break

                else:
                    survive = False
                    break

            if survive:
                stack.append(asteroid)

        return stack