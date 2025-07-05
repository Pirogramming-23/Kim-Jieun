import random

def call_num():
    while True:
        num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        if not num.isdigit():
            print("정수를 입력하세요")
        elif num not in ['1', '2', '3']:
            print("1,2,3 중 하나를 입력하세요")
        else:
            return int(num)
        
def check_player(count):
    player = 'player' if count % 2 == 0 else 'computer'
    return player

def brGame(start_num, end_num):
    for i in range(start_num, end_num):
        print(f"{player}: {i}")
        if i == 31:
            return "game_over"


start_num = 1
count = 1

while True:
    player = check_player(count)
    
    #player, computer에 따라 num 입력 방식 결정
    if player == "player":
        num = call_num()
    else:
        num = random.randint(1, 3)
    
    end_num = start_num + num
    
    result = brGame(start_num, end_num)
    if result == "game_over":
        count+=1
        player = check_player(count)
        print(f"{player} win!")
        break
    
    start_num = end_num
    count+=1
