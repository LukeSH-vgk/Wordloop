import numpy as np
data1 = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding = 'utf8')
data2 = np.loadtxt("loop2.csv", delimiter=",", dtype=str, encoding = 'utf8')
data3 = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding = 'utf8')
data4 = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

def num_letters(num_row,num_col): # the numbers are (3,4)
    return (num_row * num_col) - (num_row - 2) * (num_col - 2)

print(np.array(data3))
print(num_letters(6,4))
assert num_letters(13, 4) == 30  # loop1: 13 is the num_rows and 4 is the num_columns
print("Checking assertions.")

assert num_letters(4, 4) == 12  # loop2: 4 is the num_rows and 4 is the num_columns
print("Checking assertions.")

assert num_letters(6, 7) == 22  # loop4: 6 is the num_rows and 7 is the num_columns
print("Checking assertions.")

assert num_letters(6, 4) == 16  # loop3: 6 is the num_rows and 4 is the num_columns
print("Checking assertions.")
