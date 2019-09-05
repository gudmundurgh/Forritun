first = int(input("First: "))
step = int(input("Step: "))
#If first is less than 100 the first value of i
#will make total >= 100

end = 0
if first < 100:
    end = first * step + 100
else:
    end = first + 1

total = 0

for i in range(first,end,step):
    total = total + i
    print(i, end=" ")
    if total >= 100:
        break
print("Sum of series: ", total)