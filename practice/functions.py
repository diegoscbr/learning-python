def withDefaultArgs(age = 24, name = "Diego", state = True):
    print(f"Age: ", age)
    print(f"Name: ", name)
    print(state)

withDefaultArgs(14, "Santi", False)
withDefaultArgs()


