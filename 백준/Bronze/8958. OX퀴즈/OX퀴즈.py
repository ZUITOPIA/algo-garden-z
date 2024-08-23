n = int(input())

for _ in range(n):
    text = input()
    count = 0
    score = 0
    for i in text:
        if i == "O":
            count += 1
        else:
            count = 0
        score += count
    print(score)
