import numpy as np
data1 = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding = 'utf8')
data2 = np.loadtxt("loop2.csv", delimiter=",", dtype=str, encoding = 'utf8')
data3 = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding = 'utf8')
data4 = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

def num_letters(num_row,num_col): # the numbers are (3,4)
    return (num_row * num_col) - (num_row - 2) * (num_col - 2)

n_rows = data1.shape[0]
n_cols = data1.shape[1]

word = []
assert num_letters(13, 4) == 30  # loop1: 13 is the num_rows and 4 is the num_columns
print("Checking assertions.")

assert num_letters(4, 4) == 12  # loop2: 4 is the num_rows and 4 is the num_columns
print("Checking assertions.")

assert num_letters(6, 7) == 22  # loop4: 6 is the num_rows and 7 is the num_columns
print("Checking assertions.")

assert num_letters(6, 4) == 16  # loop3: 6 is the num_rows and 4 is the num_columns
print("Checking assertions.")

for c in range(n_cols):
    word.append(str(data1[0,c]).strip())

for r in range(1,n_rows):
    word.append(str(data1[r,-1]).strip())
    
for c in range(2,n_cols):
    word.append(str(data1[-1,-c]).strip())

for r in range(1,n_rows):
    word.append(str(data1[-r,0]).strip())
print(word)

n_rows2 = data2.shape[0]
n_cols2 = data2.shape[1]

word2 = []
for c in range(n_cols2):
    word2.append(str(data2[0,c]).strip())

for r in range(1,n_rows2):
    word2.append(str(data2[r,-1]).strip())
    
for c in range(2,n_cols2):
    word2.append(str(data2[-1,-c]).strip())

for r in range(1,n_rows2):
    word2.append(str(data2[-r,0]).strip())
print(word2)

n_rows3 = data3.shape[0]
n_cols3 = data3.shape[1]

word3 = []
for c in range(n_cols3):
    word3.append(str(data3[0,c]).strip())

for r in range(1,n_rows3):
    word3.append(str(data3[r,-1]).strip())
    
for c in range(2,n_cols3):
    word3.append(str(data3[-1,-c]).strip())

for r in range(1,n_rows3):
    word3.append(str(data3[-r,0]).strip())
print(word3)

n_rows4 = data4.shape[0]
n_cols4 = data4.shape[1]

word4 = []
for c in range(n_cols4):
    word4.append(str(data4[0,c]).strip())

for r in range(1,n_rows4):
    word4.append(str(data4[r,-1]).strip())
    
for c in range(2,n_cols4):
    word4.append(str(data4[-1,-c]).strip())

for r in range(1,n_rows4):
    word4.append(str(data4[-r,0]).strip())
print(word4)
