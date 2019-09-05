top_num = int(input("Upper number for the range: ")) # Do not change this line

divisor = 0
sum_of_divisors = 0

for j in range (1,top_num+1):
    sum_of_divisors = 0
    for i in range(1, j):
        if j % i == 0:
            sum_of_divisors = sum_of_divisors + i
    if sum_of_divisors == j:
        print(j)