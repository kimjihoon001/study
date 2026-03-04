# try_except.py

# print("try_except")

# #ValueError
# while True:
#     x = int(input("Please enter a number: "))
#     break

# print("program exit")




print("try_except")

# 비정상종료 => 정상종료

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again..")
    finally:
        print("try or except 실행시, 무조건 실행")
        
        
print("program exit")

# except : 작성시 다음 예외까지 처리하므로
#     KeyboardInterrupt(Ctrl+c)
#     SystemExit(exit())
#프로그램 강제 종료시, 종료가 안될 수 있음

#   조건물을 예외처리와 비교
#   조건문 
#   목적: 미리 상황을 검사
#   시점: 실행 전 판단
#   성격: 정상 흐름 제어 
#   사용 기준: 예상 가능한 경우    
 
#   예외처리
#   목적: 오류가 발생했을 떄 처리
#   시점: 실행 중 오류 발생 후
#   성격: 비정상 상황 대응
#   사용 기준: 예측 어려운 오류