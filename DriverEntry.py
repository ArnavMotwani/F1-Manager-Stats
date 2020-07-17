def driver():
    num = int(input("How many racers are you comparing "))
    dName = [""] * num
    dLevel = [0.0] * num

    for i in range(num):
        dName[i - 1] = input("Enter driver last Name ")
        dLevel[i - 1] = float(input("Enter driver level "))

    return dName, dLevel, num
