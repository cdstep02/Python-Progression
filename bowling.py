# Problem #3
if __name__ == "__main__":
    scores = [[8, 1], [5, 3], [3, 5], [8, 1], [7, 1], [1, '-'], [9, '-'], [5, '-'], [6, '-'], [8, 1]]
    total = 0
    row = len(scores)
    column = len(scores[0])
    for i in range(row):
        for k in range(column):
            if scores[i][k] == "-":
                total += 0
            else:
                total += scores[i][k]
    print(total)
