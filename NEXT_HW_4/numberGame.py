max = int(input("숫자게임 최댓값을 입력해주세요: "))
min = 0
tries = 0

print(f"1부터 {max}까지의 숫자를 생각해주세요")
print("준비가 되었다면 Enter키를 누르세요")
input()

while(True) :
    mid = (max + min) // 2
    print(f"당신이 생각한 숫자는 {mid}입니까?")
    hint = input("제가 맞췄다면 '맞음', 제가 제시한 숫자보다 크다면 '큼', 제가 제시한 숫자보다 작다면 '작음'을 입력해주세요: ")
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