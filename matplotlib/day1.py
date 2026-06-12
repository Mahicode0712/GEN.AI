import matplotlib.pyplot as plt
import numpy as np

# plt.plot([2,4,6,8] , [10,20,30,40])
# plt.show()
# hours = [2,4,6,8]
# marks = [50,68,78,95]
# plt.plot(hours,marks)
# plt.title("MARKS VS HOURS")
# plt.xlabel("hours")
# plt.ylabel("marks")
# plt.xticks(2,4,6,8,10)
# plt.yticks(50,68,78,95)
# plt.show()

# hours = [2,3,4,5,6]
# DSA_marks = [25,36,50,60,80]
# ML_marks = [10,30,45,68,87]
# plt.title("MARKS VS HOURS" , fontdict= {'fontstyle' : 'italic' , "color" : 'blue' , 'fontsize' : '2.5'})
# plt.plot(hours,DSA_marks, label = "DSA MARKS",  color = "green" , linewidth = 2 , marker = '.' , linestyle = "--")
# plt.plot(hours,ML_marks, label = "ML MARKS" , color = "red" , linewidth = 2 , marker = '*' , linestyle = "-.")
# plt.legend(loc = "upper left")
# plt.xlabel("hours" , fontdict= {'fontstyle' : 'italic' , "color" : 'blue' , 'fontsize' : '2.5'})
# plt.ylabel("marks" , fontdict= {'fontstyle' : 'italic' , 'color' : 'blue' , 'fontsize' : '2.5'})
# plt.show()


#plt.plot(x ,y , color,marker,linestyle) we can use this instead rather than typing long codes

# plt.plot(hours,DSA_marks, 'p*--')
# plt.plot(hours,ML_marks, 'b^--')
# plt.show()



# #horizontal alignment
# x = np.arange(0,5,0.2)
# plt.figure()
# plt.subplot(3,1,1)
# plt.plot(x,x, 'r*--')
# plt.subplot(3,1,2)
# plt.plot(x,x**2, 'g*--')
# plt.subplot(3,1,3)
# plt.plot(x,x**3, 'b*--')
# plt.show()

# #vertical alignment
# x = np.arange(0,5,0.2)
# plt.figure()
# plt.subplot(1,3,1)
# plt.plot(x,x, 'r*--')
# plt.title("linear graph")
# plt.subplot(1,3,2)
# plt.plot(x,x**2, 'g*--')
# plt.title("quadratic graph")
# plt.subplot(1,3,3)
# plt.plot(x,x**3, 'b*--')
# plt.title("cubic graph")
# plt.subtilte("Different functions of x")
# #to have spacing btw all the graphs 
# plt.tight_layout()
# plt.show()


# #better way of sub plotting 
# #linspace
# x = np.linspace(1,10,100)
# fig, axes = plt.subplots(2,3)
# axes[0,0].plot(x,np.sin(x))
# axes[0,0].set_title("sinx function")
# axes[0,0].set_xlabel("X")
# axes[0,0].set_ylabel("sin(x)")

# axes[0,1].plot(x,np.cos(x))
# axes[0,1].set_title("cosx function")
# axes[0,1].set_xlabel("X")
# axes[0,1].set_ylabel("cos(x)")

# axes[0,2].plot(x,np.tan(x))
# axes[0,2].set_title("tanx function")
# axes[0,2].set_xlabel("X")
# axes[0,2].set_ylabel("tan(x)")

# axes[1,0].plot(x,np.cosec(x))
# axes[1,0].set_title("cosecx function")
# axes[1,0].set_xlabel("X")
# axes[1,0].set_ylabel("cosex(x)")

# axes[1,1].plot(x,np.sec(x))
# axes[1,1].set_title("secx function")
# axes[1,1].set_xlabel("X")
# axes[1,1].set_ylabel("sec(x)")

# axes[1,2].plot(x,np.cot(x))
# axes[1,2].set_title("cotx function")
# axes[1,2].set_xlabel("X")
# axes[1,2].set_ylabel("cot(x)")
# plt.tight_layout()
# plt.show()

# #scatter plot
# x = np.random.rand(50)*10
# y = np.random.rand(50)*10
# plt.scatter(x,y)
# plt.show()

#pie chart

courses = ['DSA' , 'ML' , 'LANGUAGE' , 'LLD' , 'WEB-DEV']
student = [65,78,34,45,23]
plt.pie(student , labels = courses , shadow= True , explode=[0.2,0,0,0,0] , colors=['lightcoral' , 'blue' , 'yellow' , 'green' , 'purple'])
plt.show()