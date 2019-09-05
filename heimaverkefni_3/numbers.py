#print all positive two-digit numbers where the sum of its two digits 
#squared equals the number.


for number in range(10,100):
    first_digit = number // 10
    last_digit = number % 10
    sum_of_digits = first_digit + last_digit
    sum_of_digits_squared = sum_of_digits ** 2
    if sum_of_digits_squared == number:
        print(number)

# Find and print all positive numbers < 100
# that have 10 divisors.

number = 1
test_divisor = 1
divisor_count = 0

for number in range(1,100):
    divisor_count = 0
    for test_divisor in range(1,number+1):
        if number % test_divisor == 0:
            divisor_count += 1
    if divisor_count == 10:
        print(number) 