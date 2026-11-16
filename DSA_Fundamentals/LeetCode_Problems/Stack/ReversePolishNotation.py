class Solution:
    def ReversePolishNotation(self, tokens : list[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else :
                    stack.append(int(a/b))
            else :
                stack.append(int(token))
        return stack[0]

items = [
    ["2","1","+","3","*"] , ["4","13","5","/","+"], 
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
]
obj = Solution()
for item in items:
    print(f"Result : {obj.ReversePolishNotation(item)}")