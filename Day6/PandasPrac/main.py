from array import array

import numpy as np

# ! creating array from array in built class of python
my_arr = array("u", ["a", "b", "f", "d"])
for num in my_arr:
    pass
    # print(num)

# ! creating array from numpy

my_list = [12, 1, 33, 44, 56, 76]

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

np_array = np.array(my_list, int)

float_arr = np.array(my_list, float)

two_d_arr = np.array(two_dimensional_list)

# print(two_d_arr)
# print(float_arr)
# print(type(np_array.tolist()))
# print(two_d_arr.shape)

# ! datatype of numpy arr

# ? Type of data types: str, int, float, complex, bool, list, None

int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

# print(int_array.size)
# print(int_array.dtype)
# print(float_array)
# print(float_array.dtype)

print(two_d_arr.size)

# ! We can perform math operations using numpy with array easily without using loop

numbers = [15, 55, 14, 22, 63, 14]
my_numbers_arr = np.array(numbers, int)
# * 3 + 2 - 10
ten_minus_original_nums = my_numbers_arr / 2
# print(ten_minus_original_nums)
ten_minus_original_nums *= 3
# print(ten_minus_original_nums)
ten_minus_original_nums += 2
# print(ten_minus_original_nums)
ten_minus_original_nums -= 10
# print(ten_minus_original_nums)


# ! Typ conversion in numpy arraylist

print(my_numbers_arr.astype(dtype=float).astype(dtype=str))

# * shape attribute shows what is the shape of data structure

# * size attribute shows what is size of data structure

# * dtype attribute shows what data type our ds has

# ! Getting items of numpy arr normally as usual

print(my_numbers_arr[1])

# ! Slicing of arr

print(my_numbers_arr[1:4])

two_d_arr[1, 1] = 44

print(two_d_arr.flatten())

print(np.random.choice(["a", "e", "i", "o", "u"], size=10))

rand2 = np.random.randn(2, 2)

print(rand2)
