#print all positive two-digit numbers where the sum of its two digits 
#squared equals the number.


for number in range(10,100):
    first_digit = number // 10
    last_digit = number % 10
    sum_of_digits = first_digit + last_digit
    sum_of_digits_squared = sum_of_digits ** 2
    if sum_of_digits_squared == number:
        print(number)