def is_permutation(this: str, that: str):
    if this == that:
        return True

    this = sorted(this)
    that = sorted(that)

    return this == that


if __name__=="__main__":
    print(is_permutation("abc", "cab"))
    print(is_permutation("abc", "cabc"))

