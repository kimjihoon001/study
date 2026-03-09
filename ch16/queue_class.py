# queue_class.py

class Queue:
    
    def __init__(self):
        self.queue = []
    # 1. Enqueue (데이터 삽입)
    def enqueue(self,data):
        self.queue.append(data)
    # 2. Dequeue (데이터 제거)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return
    # 3. 큐가 비어있는 경우, 
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
    # 4. 큐 상태 반환
    def status_queue(self):
        return self.queue

q1 = Queue()
q1.dequeue()
print(q1.status_queue())
q1.enqueue(1)
q1.enqueue(2)
q1.dequeue()
q1.enqueue(3)
q1.enqueue(4)
print(q1.status_queue())


# 들여쓰기 4칸
# 클래스명 첫자 대문자
# 함수명
# 변수명
# 명명 시 규칙 
# 1. 스네이크 case: 단어와 단어사이 _  활용
# ex) is_empty
# 함수명, 변수명
# 2. camel case: 단어와 단어사이 대문자 활용
# ex) userName, addNumber
# 함수명, 변수명
# 3. 파스칼case: 단어의 첫글자를 대문자 작성
# ex) Queue, UserAccount
# 클래스명
## 한줄 길이: 코드 최대 79자, 주석 72자
# 공백 규칙: 
# - 연산자 앞뒤 공백사용
# - 함수 호출시 공백 미사용
## 상수 규칙
# 대문자 + 언더스코어
# 예) PI, MAX_SIZE
## import 규칙: 한줄에 하나씩

# obutton, o_button
# inumber
# fnum