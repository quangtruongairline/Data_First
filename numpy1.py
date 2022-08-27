import numpy as np

a=[[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]
print(np.ndim(a))

b=np.array([1,2,3,4,5])
x=b.copy()
y=b.view()

b[0]=30

print(x," \n")
print(y," \n")

for x in np.nditer(b):   #in ra tu phan tu ke ca 2,3 chieu
    print(x)


print(np.where(b==4)) #in cac chi so co gia tri la 4

#tạo mảng bang random

m=np.random.randint(100,size=(2)) #random 0 -> 100 mang 1D 
aa=np.random.randint(100,size=(2,3)) # random 0->100  man 2D

aaa=np.random.rand(3)
ab=np.random.rand(2,3)
print(ab)




