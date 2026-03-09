class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def status_stack(self):
        return self.stack

    def check(self, strs):

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in strs:

            if ch in '({[':
                self.push(ch)

            elif ch in ')}]':

                if self.is_empty():
                    return False

                top = self.pop()

                if top != pairs[ch]:
                    return False

        return self.is_empty()




# def check_brakets(text):
#     stack=[]                # 빈스텍 생성
#     for char in text:       # 시작 괄호 확인
#         if char in '({[':       # 시작 괄호 확인
#             stack.append(char)  # 스텍 괄호 추가
#         elif char in ')}]':     # 종료 괄호 확인
#             if not stack:       # 스택이 비었다면
#                 return False
#             top = stack.pop()
#             # print(f"top={top}")
#             # print(f"char={char}")
            
#             # 괄호 짝 일치하지 않는 경우
#             if (char == ')' and top != '(') or \
#             (char == '}' and top != '{') or \
#             (char == ']' and top != '['):
#                 return False
#     return  len(stack) == 0    


# print(check_brakets("(a+b)")) 
# print(check_brakets("(a+b)]}"))  
# print(check_brakets('[{(x+y)+3}-4]'))
# print(check_brakets('[{x+y)+3}-4]'))