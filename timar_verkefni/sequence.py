#design an algorithm that generates the first n
#numbers in the following sequence 1,2,3,6,11,20,37, ... , ... 

#Sequence where first three are known 0,1,2. each after that is 
#sum of last three

#set the first 3 values from start
#use a for loop

# set first_num = 1 and second_num = 2
# next is the sum of last two
n = int(input("Enter the number of integers in the sequence: "))
third_from_i = 0
second_from_i = 1
next_from_i = 2
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

