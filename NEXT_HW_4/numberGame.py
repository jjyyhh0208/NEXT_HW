max = int(input("숫자게임 최댓값을 입력해주세요: "))
min = 0
tries = 0

print(f"1부터 {max}까지의 숫자를 생각해주세요\n")
print("시작을 위해 Enter키를 누르세요")
input()

while(True) :
    mid = (max + min) // 2
    print(f"생각한 숫자가 {mid} 인가요?")
    hint = input("맞으면 '맞음', 생각한 숫자가 더 크다면 '큼', 생각한 숫자가 더 작다면 '작음'을 입력해주세요: ")
    tries += 1
    
    if hint == "맞음":
        print(f"{tries}번 만에 맞췄다")
        break
    elif hint == "큼":
        min = mid
    elif hint == "작음":
        max = mid
    else:
        print("올바른 명령어가 아닙니다")