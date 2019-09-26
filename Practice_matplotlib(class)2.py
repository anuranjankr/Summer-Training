import matplotlib.pyplot as plt
from matplotlib import style

plt.subplot(311)
plt.plot([1,2,3],[4,5,6],'r',label='Line1',linewidth=0.5)
plt.plot([2,4,6],[9,7,3],'b',label='Line2')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("My Plot")
plt.legend()
style.use('ggplot')
plt.grid(True,color='k')
plt.subplot(312)
# x-axis values 
x = [1,2,3,4,5,6,7,8,9,10] 
# y-axis values 
y = [2,4,5,7,6,8,9,11,12,12] 
  
# plotting points as a scatter plot 
plt.scatter(x, y, label= "stars", color= "green",  
            marker= "*", s=30) 
  
# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My scatter plot!') 
# showing legend 
plt.legend()

plt.subplot(3,1,3)
# frequencies 
ages = [2,5,70,40,30,45,50,45,43,40,44, 
        60,7,13,57,18,90,77,32,21,20,40] 
  
# setting the ranges and no. of intervals 
range = (0, 100) 
bins = 10  
  
# plotting a histogram 
plt.hist(ages, bins, range, color = 'green', 
        histtype = 'bar', rwidth = 0.8) 
  
# x-axis label 
plt.xlabel('age') 
# frequency label 
plt.ylabel('No. of people') 
# plot title 
plt.title('My histogram')


activities = ['eat', 'sleep', 'work', 'play'] 
  
# portion covered by each label 
slices = [3, 7, 8, 6] 
  
# color for each label 
colors = ['r', 'y', 'g', 'b'] 
  
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        radius = 1.2, autopct = '%1.1f%%') 
  
# plotting legend 
plt.legend()
  
'''
plt.subplot(2,1,1)         #(no_of_row , no_of_col , figure_no{Position of graph})
plt.plot([1,2,3],[4,5,6],'r',label='Line1',linewidth=0.5)
plt.subplot(2,1,2)
plt.plot([2,4,6],[9,7,3],'b',label='Line2')
'''

plt.show()
