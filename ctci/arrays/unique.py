def is_unique(input: str):
    char_set = [False] * 128

    for ch in input:
        ascii_value = ord(ch)
        if char_set[ascii_value]:
            return False
        else:
            char_set[ascii_value] = True

    return True


if __name__=="__main__":
    print(is_unique("abc"))
    print(is_unique("123a1"))
