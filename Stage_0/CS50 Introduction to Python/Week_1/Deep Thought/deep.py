name = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
).lower()
if name == "forty-two":
    print("Yes")
elif name == "forty two":
    print("Yes")
elif name.strip() == "42":
    print("Yes")
else:
    print("No")
