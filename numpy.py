import numpy as np
print(np.__version__)
arr=np.array([[1,2,3,4], [1,2,3,4]])
print(arr)
print()
arr1=np.linspace(0,2,9) #any 9 no. from 1 to 2 of any space
print(arr1)
arr2= np.arange(1,10,2) #range between two no.
print(arr2)
arr3=np.eye(3) #identity matrix
print(arr3)
arr1=np.random.randint(5,size=(2,3))#random integer no.
print(arr1)
arr1=np.random.rand(2,3)*255 #scalar matrix multiplication
print(arr1)
print(arr1.shape) #height,width
print(arr1.size) #no. of elements
print(arr.min)
