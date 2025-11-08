def main():
    result = 50
    while True:
        print(f"Amount Due: {result}")
        num = int(input("Insert Coin: "))
        if num == 25:
            result -= 25
        elif num == 10:
            result -= 10
        elif num == 5:
            result -= 5
        if result <= 0:
            print(f"Change Owed: {abs(result)}")
            break


if __name__ == "__main__":
    main()
