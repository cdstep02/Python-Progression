# Problem #4

if __name__ == "__main__":
    forks = {"forks", "knorks", "splayds", "sporks"}
    spoons = {"spoons", "sporks", "splayds", "spifes"}
    knives = {"knifes", "knorks", "splayds", "spifes"}
    userfork = input("Do you need a fork?")
    userspoon = input("Do you need a spoon?")
    userknife = input("Do you need a knife?")
    if userfork == "yes" and userspoon == "yes" and userknife == "yes":
        print(forks.intersection(spoons, knives))
    elif userfork == "yes" and userspoon == "yes":
        print(forks.intersection(spoons))
    elif userfork == "yes" and userknife == "yes":
       print(forks.intersection(knives))
    elif userspoon == "yes" and userknife == "yes":
        print(spoons.intersection(knives))
    elif userspoon == "yes":
        print(spoons)
    elif userknife == "yes":
        print(knives)
    elif userfork == "yes":
        print(forks)
    else:
        print("Please select something:")



