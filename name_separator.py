# Problem #1
def seperator(user):
    first = ""
    last = ""
    # used as a counting variable in the program
    k = 0
    for i in range(len(user)):
        if user[i] == " ":
            k += 1
        elif k <= 0:
            first += user[i]
        else:
            last += user[i]
    print("First name:", first)
    print("Last name:", last)


if __name__ == "__main__":
    name = input("Please enter a name:")
    seperator(name)
