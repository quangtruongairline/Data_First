from cmath import exp
from tkinter import Label
from turtle import color
import matplotlib.pyplot as plt

a=[1,2,3,4,5,6,7,8]
b=[1,4,9,16,25,36,49,64]

# plt.plot(a,marker ='*');

#fmt marker| line| color

# plt.plot(a,'o-r')
# plt.plot(a,'o--b')



font1={'family':'serif','color': 'blue', 'size':16}

# plt.plot(a,b)
# plt.title("Test", fontdict=font1,loc='left');

# # plt.grid(axis='x');

# plt.grid(color='blue', linestyle='--', linewidth=0.5);

# plt.scatter(a,b);
# plt.scatter(b,a);
mylabels=['A','B','C','D','E','F','G','H']

myexlpde=[0.4,0,0,0,0,0,0,0]
plt.pie(a,labels=mylabels, startangle=90, explode=myexlpde);
plt.show();