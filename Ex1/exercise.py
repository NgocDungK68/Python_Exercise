# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
count_positive = sum(filter(lambda x: x > 0, data1))
count_negative = sum(filter(lambda x: x < 0, data1))

# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

char = dict.fromkeys(data2, 0)
for i in data2:
    char.update({i: char.get(i) + 1})

data2 = list(filter(lambda x: char.get(x) > k, char.keys()))
print(data2)

# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

maximum = data3[0] + data3[1]
for i in range(1, len(data3) - 2):
    if maximum < data3[i] + data3[i + 1]:
        maximum = data3[i] + data3[i + 1]
print(maximum)

# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

for i in data4:
    print_data = []
    copy_data = data4.copy()
    print_data.append(i)
    copy_data.remove(i)
    for j in copy_data:
        print(print_data + copy_data)
        copy_data[0], copy_data[1] = copy_data[1], copy_data[0]

# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

data5_list1 = list(filter(lambda x: x is not None, data5_list1))
data5_list2 = list(filter(lambda x: x is not None, data5_list2))
for i in range(len(data5_list1)):
    data5_list1[i].extend(data5_list2[i])

print(data5_list1)

# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
numbers = [str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
print(', '.join(numbers))

# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers = [str(num) for num in range(1000, 3001) if all(digit in '02468' for digit in str(num))]
print(', '.join(numbers))

# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient
