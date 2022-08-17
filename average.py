# Problem #2

def avgcalc(entries):
    entry = 0
    for i in range(entries):
        entry += int(input("Enter a number:"))
    avg = entry / entries
    print("The average is:", avg)





if __name__ == '__main__':
    num_of_entries = int(input("How many numbers would you like to input?:"))
    avgcalc(num_of_entries)
