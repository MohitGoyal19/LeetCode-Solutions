class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ('[', '{', '('):
                stack.append(char)

            else:
                if len(stack) > 0 and ((char == ']' and stack[len(stack)-1] == '[') or (char == '}' and stack[len(stack)-1] == '{') or (char == ')' and stack[len(stack)-1] == '(')):
                        stack.pop(len(stack)-1)

                else:
                    return False

        if len(stack) == 0:
            return True

        return False