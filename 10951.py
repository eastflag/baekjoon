# 무한루프, control-d 같은 키를 입력시 에러를 내지 않고 종료되어야 한다.
while True:
    try:
        enter = input().split(' ')
        A = int(enter[0])
        B = int(enter[1])
        print(A + B)
    except:
        break