id = input("아이디를 입력하세요: ")
if id == "kenneth":
    print("아이디 일치")
    pw=input("암호를 입력하세요: ")
    if pw=="1234":
        print("로그인 성공")
    else:
        print("암호 불일치!")
else:
    print("존재하지 않는 아이디!")