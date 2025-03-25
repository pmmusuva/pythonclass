import numpy as np

"""
NumPy (Numerical Python) is an open source Python library 
Its widely used in science and engineering. 
The NumPy library contains multidimensional array data structures, 
and a large library of functions that operate efficiently on these data structures. 
"""
#create a numpy array
nparr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

#accessing elements in the array
print(nparr[0]) 

#sort using the inbuilt method
nparr.sort() 
print(nparr)

#slice elements using index. The result includes the start index, but excludes the end index.
print(nparr[3:5])

#Slice elements from index 4 to the end of the array:
print(nparr[3:])