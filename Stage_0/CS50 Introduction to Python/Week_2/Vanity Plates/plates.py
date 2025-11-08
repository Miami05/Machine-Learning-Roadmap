def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if any(not ch.isalnum() for ch in s):
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    seen_digit = False
    for ch in s:
        if ch.isdigit():
            if not seen_digit:
                if ch == "0":
                    return False
                seen_digit = True
        else:
            if seen_digit:
                return False
    return True


main()
