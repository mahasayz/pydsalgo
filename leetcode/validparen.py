def checkValidString(s: str) -> bool:
    if s == "":
        return True

    brace_stack = []
    wild_stack = []

    for idx, ch in enumerate(s):
        if ch == '(':
            brace_stack.append((ch, idx))
        elif ch == '*':
            wild_stack.append((ch, idx))
        else:
            if brace_stack:
                brace_stack.pop()
            elif wild_stack:
                wild_stack.pop()
            else:
                return False

    if brace_stack:
        while brace_stack and wild_stack:
            _, brace_idx = brace_stack[len(brace_stack)-1]
            _, wild_max_idx = wild_stack[len(wild_stack) - 1]
            if wild_max_idx < brace_idx:
                return False
            for idx in range(0, len(wild_stack)):
                _, wild_idx = wild_stack[idx]
                if wild_idx > brace_idx:
                    wild_stack.pop(idx)
                    brace_stack.pop()
                    break

    if brace_stack:
        return False

    return True


if __name__=="__main__":
    print(checkValidString("(*)"))
    print(checkValidString("(*))"))
    print(checkValidString("()"))
    print(checkValidString("*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"))
