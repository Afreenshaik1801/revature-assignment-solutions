for i in range(5):
    if i == 0 or i == 5 - 1:
        print("* " * 5)
    else:
        print("* " + "  " * (5 - 2) + "*")
