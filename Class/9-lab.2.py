a = int(input("Enter the number of rows: "))
b = int(input("Enter the number of columns: "))

num_list = [[a for a in range(b)] for _ in range(a)]


for i in range(a):
    for j in range(b):
        num_list[i][j] = int(input(f"Enter value for [{i}][{j}]: "))


for i in num_list:
    for j in i:
        print(j, end = " ")
    print()