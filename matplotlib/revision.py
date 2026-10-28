import matplotlib.pyplot as plt

# Line Chart 
# x=[10,20,30,40,50]
# y=[20,30,40,50,60]

# plt.plot(x,y)
# plt.title("My Graph")
# plt.xlabel("X-axis")
# plt.ylabel("y-axis")
# plt.grid(True)
# plt.show()

# Bar Chart

# name=["prateek","ajay","deepak","mohit"]
# salary=[1000,2000,3000,4000]

# plt.barh(name,salary)

# plt.title("Student Marks")
# plt.xlabel("Students")
# plt.ylabel("Marks")

# plt.show()

# 4. Scatter plot 
# height=[170,165,180,160,175]
# weight=[70,60,80,50,75]

# plt.scatter(height,weight)
# plt.xlabel("Height")
# plt.ylabel("weight")
# plt.title("Height vs Weight")

# plt.show()

# 5. Pie Chart

# subjects = ["Python", "Java", "Math", "OS"]
# marks = [30, 25, 20, 25]

# plt.pie(marks, labels=subjects,autopct="%1.1f%%")

# plt.title("Subject Distribution")

# plt.show()

# 6. Histogram

# used to show the distribution /frequency of numerical data

# ages=[18,19,29,22,21,20,18,19,25,23,24]

# plt.hist(ages)

# plt.xlabel("Age")
# plt.ylabel("frequency")
# plt.title("Age distribution")

# plt.show()

#7. Multpiple  lines 

# months = ["Jan", "Feb", "Mar", "Apr"]

# sales1 = [20, 30, 25, 40]
# sales2 = [15, 25, 30, 35]

# plt.plot(months, sales1, label="Product A")
# plt.plot(months, sales2, label="Product B")

# plt.legend()

# plt.show()

# <<<<<<<<<<<<<<<<<<<<<<<<<---------------------------Question1------------------->>>>>>>>>>>>>>>>>>>>>>>>>
# days=[1,2,3,4,5]
# temperature=[30,20,31,35,33]

# plt.plot(days,temperature)
# plt.title("Temperature Report")
# plt.xlabel("Days")
# plt.ylabel("termperature")
# plt.grid()

# plt.show()

# <<<<<<<<<<<<<<<<<<<<<<<<<---------------------------Question2------------------->>>>>>>>>>>>>>>>>>>>>>>>>
# subjects=["python","java","math","os"]
# marks=[89,90,76,45]

# plt.bar(subjects,marks,color="red")
# plt.title("Marks scored by student")
# plt.xlabel("subjects")
# plt.ylabel("marks")
# plt.show()

# scatterplot question

# hours=[1,2,3,4,5]
# marks=[34,45,74,8,68]
# plt.title("study hours vs marks")
# plt.scatter(hours,marks)

# plt.show()

# subjects=["python","java","math","os"]
# students=[10.19,23,16,24]

# plt.pie(students, labels=subjects,autopct="%1.1f%%")
# plt.show()
 
#histogram 
# marks = [45, 50, 55, 60, 65, 65, 70, 70, 70,
#          75, 80, 80, 85, 90, 95]

# plt.hist(marks, bins=5, color="green", edgecolor="black")

# plt.show()

# players = ["Virat", "Rohit", "Gill", "Pant", "Dhoni"]
# runs = [620, 580, 540, 490, 430]

# plt.bar(players,runs)
# plt.grid()
# plt.show()

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# sales = [120, 150, 135, 180, 200, 220]

# plt.plot(months,sales)
# plt.xlabel("months")
# plt.ylabel("sales")

# plt.show()

# matches = [1, 2, 3, 4, 5,6,7,8]

# virat = [1,30,40,78,70,132,90,165]
# rohit = [0,32,44,60,40,75,55,80]

# plt.plot(matches,virat,label="virat",color="red")
# plt.plot(matches,rohit,label="rohit",color="blue")

# plt.title("Virat vs Rohit Performance ")
# plt.xlabel("matches")
# plt.ylabel("runs")
# plt.legend()
# plt.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

python = [60, 65, 70, 75, 80, 85]
java = [50, 55, 60, 58, 65, 70]

plt.plot(months,python,label="python",color="red")

plt.plot(months,java,label="java",color="black")
plt.title("Learning progress")
plt.xlabel("Months")
plt.ylabel("score")
plt.grid()
plt.legend()

plt.show()