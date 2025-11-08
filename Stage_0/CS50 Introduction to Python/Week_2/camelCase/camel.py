def camel_case(name):
    i = 0
    camel = ""
    while i < len(name):
        if name[i].isupper():
            camel += "_"
        camel += name[i].lower()
        i += 1
    print(f"snake_case: {camel}")


def main():
    name = input("camelCase: ")
    camel_case(name)


if __name__ == "__main__":
    main()
