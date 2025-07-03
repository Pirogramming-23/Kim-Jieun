def call_num():
    while True:
        num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
        if not num.isdigit():
            print("정수를 입력하세요")
        elif num not in ['1', '2', '3']:
            print("1,2,3 중 하나를 입력하세요")
        else:
            return int(num)

a_num = call_num()
for i in range(1, a_num+1):
            print(f"playerA:{i}")
b_num = call_num()
for i in range(1, b_num+1):
            print(f"playerB:{a_num + i}")
