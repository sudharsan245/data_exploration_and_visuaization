import numpy as np
import pandas as pd

arr=np.array([[1,2,3],[4,2,5]]) 
print("Array is of type:",type(arr)) 
print("No of dimensions:",arr.ndim) 
print("Shape of array:",arr.shape) 
print("Size of array:",arr.size) 
print("Array stores elements of type:",arr.dtype)
a=np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print(a) 
print("After Slicing") 
print(a[1:])
a=np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print('Our array is:') 
print(a) 
print('The items in the second column are:') 
print(a[...,1]) 
print('\n') 
print('The items in the second row are:') 
print(a[1,...]) 
print('\n') 
print('The items column 1 onwards are:') 
print(a[...,1]) 
data = np.array([
    ['Col0', 'Col1', 'Col2'],
    ['Row1', 1, 2],
    ['Row2', 3, 4]
])

# Create DataFrame using proper slicing
df = pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])
print(df)

# Other examples from your code
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(my_2darray))

my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print(pd.DataFrame(my_dict))

my_df = pd.DataFrame(data=[4, 5, 6, 7], index=range(0, 4), columns=['A'])
print(my_df)

my_series = pd.Series({
    "UnitedKingdom": "London",
    "India": "NewDelhi",
    "United States": "Washington",
    "Belgium": "Brussels"
})
print(pd.DataFrame(my_series))

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
print(df.shape)
print(len(df.index))
import matplotlib.pyplot as plt 
x=[1,2,3] 
y=[2,4,1] 
plt.plot(x,y) 
plt.xlabel('x-axis') 
plt.ylabel('y-axis') 
plt.title('My first graph')
plt.show()

import matplotlib.pyplot as plt 
a=[1,2,3,4,5] 
b=[0,0.6,0.2,15,10,8,16,21] 
plt.plot(a) 
plt.plot(b,"or") 
plt.plot(list(range(0,22,3))) 
plt.xlabel('Day->') 
plt.ylabel('Temp->') 
c=[4,2,6,8,3,20,13,15] 
plt.plot(c,label='4th Rep') 
ax=plt.gca() 
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False)
ax.spines['left'].set_bounds(3,40) 
plt.xticks(list(range(3,10)))
plt.yticks(list(range(3,20,3))) 
 
 
import matplotlib.pyplot as plt 
a=[1,2,3,4,5] 
b=[0,0.6,0.2,15,10,8,16,21] 
c=[4,2,6,8,3,20,13,15] 
fig=plt.figure(figsize=(10,10)) 
sub1=plt.subplot(2,2,1) 
sub2=plt.subplot(2,2,2) 
sub3=plt.subplot(2,2,3) 
sub4=plt.subplot(2,2,4) 
sub1.plot(a,'sb') 
sub1.set_xticks(list(range(0,10,1))) 
sub1.set_title('ist Rep') 
sub2.plot(b,'or') 
sub2.set_xticks(list(range(0,10,2))) 
sub2.set_title('2nd Rep') 
sub3.plot(list(range(0,22,3)),'vg') 
sub3.set_xticks(list(range(0,10,1))) 
sub3.set_title('3rd Rep') 
sub4.plot(c,'Dm') 
sub4.set_yticks(list(range(0,24,2))) 
sub4.set_title('4th Rep') 
plt.show() 