entered_number = int(input("Enter an integer: "))
sum_entered_numbers = 0
oddcount = 0
evencount = 0
largest_number = 0
counter = 0

while entered_number > 0:
    counter += 1
    if entered_number % 2 == 0:
        evencount += 1
    if entered_number % 2 != 0:
        oddcount += 1
    if entered_number > largest_number:
        largest_number = entered_number
    if entered_number > 0:
        sum_entered_numbers = sum_entered_numbers + entered_number
        print("Cumulative total: ", sum_entered_numbers)
    entered_number = int(input("Enter an integer: "))
if counter > 0:
    print("Largest number: ", largest_number)
if evencount > 0 or oddcount > 0:
    print("Count of even numbers: ", evencount)
    print("Count of odd numbers: ", oddcount)