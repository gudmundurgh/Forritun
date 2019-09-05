low = int(input("Enter an integer: "))
high = int(input("Enter another integer: "))
sum_of_integers = 0

for i in range(low, high+1):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_integers = sum_of_integers + i
        print(i)
print(sum_of_integers)
