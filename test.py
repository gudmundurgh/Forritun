# Find and print all positive numbers < 100
# that have 10 divisors.

number = 1
test_divisor = 1
divisor_count = 0

for number in range(1,100):
    divisor_count = 0
    for test_divisor in range(1,100):
        if number % test_divisor == 0:
            divisor_count += 1
    if divisor_count == 10:
        print(number) #need to print number value from last iteration
