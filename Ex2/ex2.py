import numpy as np
# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
arr_1 = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37])
reverse_arr_1 = arr_1[::-1]

print('Reverse array:', reverse_arr_1)

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]


# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]
arr_3 = np.array([1, 6, 4, 8, 9, -4, -2, 11])
maximum = minimum = arr_3[0]
max_index = min_index = 0
for i in range(len(arr_3)):
    if maximum < arr_3[i]:
        maximum = arr_3[i]
        max_index = i
    if minimum > arr_3[i]:
        minimum = arr_3[i]
        min_index = i
print('Indice of maximum:', max_index)
print('Indice of minimum:', min_index)


# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...