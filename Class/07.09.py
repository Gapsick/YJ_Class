bar = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]]]

for matrix in bar:
    for row in matrix:
        for col in row:
            print(col, "\t", end = "")
        print()
    print("-" * 10)