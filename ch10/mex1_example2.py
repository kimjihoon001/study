from mex1 import plus
from mex1 import Cvalue
from mex1 import p1

value = plus(3,4)
print(value)

# 파이썬 모듈 임포트시 특정 클래스, 함수, 변수를 명시하는 이유
# 1. 코드의 간결화(가독성) ex)mex1.plus() -> plus()
# 2. 네임스페이스 충돌 방지
# 3. 기능 사용의 명확성
# 단, 실행 성능 차이는 거의 없다