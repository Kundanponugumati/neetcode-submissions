class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    val = num1 + num2
                elif token == '-':
                    val = num1 - num2
                elif token == '*':
                    val = num1 * num2
                elif token == '/':
                    val = int(num1/num2)
                stack.append(val)
        return stack[-1]


