def urlify(input: str):
    space_idx = 1
    copy_input = list(input)
    for idx, ch in enumerate(input[::-1]):
        print(f"{idx} - {ch}")
        if ch == ' ' and space_idx == 1:
            continue
        elif ch == ' ':
            copy_input[-space_idx] = '0'
            space_idx += 1
            copy_input[-space_idx] = '2'
            space_idx += 1
            copy_input[-space_idx] = '%'
            space_idx += 1
        else:
            print(f"{idx} - {ch}")
            copy_input[-space_idx] = ch
            space_idx += 1

    return "".join(copy_input)


if __name__=="__main__":
    print(urlify("Mr John Smith    "))