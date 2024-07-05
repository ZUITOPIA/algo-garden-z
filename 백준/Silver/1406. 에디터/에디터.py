import sys
st1 = list(sys.stdin.readline().rstrip())
st2 = [] # 커서를 기준으로 두 개의 스택으로 쪼개주기 위해 새로 정의

m = int(sys.stdin.readline())

for _ in range(m):
    inputText = sys.stdin.readline().rstrip().split(" ")

    if inputText[0] == "L" :
        if st1:
            st2.append(st1.pop())
    elif inputText[0] == "D":
        if st2:
            st1.append(st2.pop())
    elif inputText[0] == "B":
        if st1:
            st1.pop()
    else:
        st1.append(inputText[1])

st1.extend(reversed(st2))
print("".join(st1))