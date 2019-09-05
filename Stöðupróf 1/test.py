first = int(input("First: "))
step = int(input("Step: "))
total = 0
i = first
while total <= 100:
    print(i, end=" ")
    total = total + i
    i = i + step
print()
print("Sum of series: ", total)

