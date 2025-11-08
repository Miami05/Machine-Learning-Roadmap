def main():
    text = input("What time is it? ").strip()
    time = convert(text)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    time = time.strip()
    hours_str, minute_str = time.split(":")
    minute_int = int(minute_str)
    hours_int = int(hours_str)
    return hours_int + (minute_int / 60.0)


if __name__ == "__main__":
    main()
