# stack_class.py

class Stack:
    def __init__(self):
        self.stack = []
    # 1. push
    # 기능: 스택에 데이터 넣기
    # 입력: 데이터
    # 출력: 없음
    def push(self,data):
        self.stack.append(data)
    
    # 1. pop
    # 기능: 스택에 데이터 제거하기
    # 입력: 없음
    # 출력: 데이터
    def pop(self):
        # 3. (비어있는 경우 고려)
        if not self.is_empty():
            return self.stack.pop()
        return
    # 4. 스택 내 데이터 유무 확인
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    # 5. 스택 최상위(Top) 데이터 확인
    def peak(self):
        # 3. (비어있는 경우 고려)
        if not self.is_empty():
            return self.stack[-1]
        return
    # 6. 스택 상태 반환
    def status_stack(self):
        return self.stack
    
s1 = Stack()
print(s1.peak())
s1.pop()
s1.push(1)
s1.push(2)
s1.pop()
s1.push(3)
s1.push(4)
print(s1.peak())
print(s1.status_stack())