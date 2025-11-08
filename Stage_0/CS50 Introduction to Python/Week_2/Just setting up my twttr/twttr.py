def print_without_vowels(names):
    string = ""
    for name in names:
        if name == "a" or name == "e" or name == "i" or name == "o" or name == "u":
            string += name.replace(name, "")
        elif name == "A" or name == "E" or name == "I" or name == "O" or name == "U":
            string += name.replace(name, "")
        else:
            string += name
    print(f"Output: {string}")


def main():
    names = input("Input: ")
    print_without_vowels(names)


if __name__ == "__main__":
    main()
