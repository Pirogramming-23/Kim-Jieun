def call_num():
    while True:
        num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
        if not num.isdigit():
            print("정수를 입력하세요")
        elif num not in ['1', '2', '3']:
            print("1,2,3 중 하나를 입력하세요")
        else:
            return int(num)

start_num = 1
count = 1

while True:
    player = 'B' if count % 2 == 0 else 'A'
    num = call_num()
    end_num = start_num + num
    for i in range(start_num, end_num):
        print(f"player{player}: {i}")
        if i == 31:
            break
    if end_num > 31:
        count+=1
        break
    start_num = end_num
    count+=1

player = 'B' if count % 2 == 0 else 'A'
print(f"player{player} win!")
