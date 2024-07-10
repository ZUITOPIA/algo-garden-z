while True:
    text = input()
    stack = []

    if text == ".":
        break    # . 만 입력되었을 때는 stack에 아무것도 저장 X -> YES 출력

    for v in text:
        if v == "(" or v == "[":
            stack.append(v)
        elif v == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
        elif v == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")