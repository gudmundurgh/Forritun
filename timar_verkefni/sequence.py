#design an algorithm that generates the first n
#numbers in the following sequence 1,2,3,6,11,20,37, ... , ... 

#Sequence where first three are known 0,1,2. each after that is 
#sum of last three

#ask for a number to determine the length of the sequence
#start with first three that are known and print them out
#iterate till n to add last three together and print next number
n = int(input("Enter the number of integers in the sequence: "))
third_from_i = 1
second_from_i = 2
next_from_i = 3
print(third_from_i)
print(second_from_i)
print(next_from_i)
next_number_stored = 0
for i in range(4,n+1):
    next_number = third_from_i + second_from_i + next_from_i
    next_number_stored = next_number
    third_from_i = second_from_i
    second_from_i = next_from_i
    next_from_i = next_number_stored
    print(next_number)
