import numpy as np
# a = np.array([1,2,3,4])
# print(a)

# a = [[1,2,3,4] , [11, 11 , 10 , 30]]
# b = [[5,6,7,8] , [11, 20 , 30 , 49]]
# c = []
# for i in range(0,len(a)):
#      c.append(a[i] * b[i])
  
# print(c) 

# a = np.array([[1,2,3,4] , [11,11,10,30]])
# b = np.array([[5,6,7,8] , [11,20,30 ,49]])
# c = a * b
# c = a + b
# print(c)

# a = np.array([1,23,4,4884,48484,44844])
# print(a[0:])
# print(a[:])
# print(a[:len(a)])


# # numpy
# a = np.zeros(2)
# print(a)
# b = np.zeros((2,3))
# print(b)
# b = np.zeros((3,2,4,3))
# print(b)




# a = np.arange(2,6,3)
# print(a)
# b = np.arange(1,200,10)
# print(b)
# c = np.arange(1,5,0.5)
# print(c)
# d = np.arange(10,0,-1)
# print(d)
# print(np.argsort(d))


# #reshaping
# a = np.arange(1,9,2)
# print(a)
# b = a.reshape(2,2)
# print(b)

# a = np.array([1,100,2020,5,5,6,66])
# print(a < 10)
# print(a > 10)
# print(a % 2 == 0)
# a = a * 100
# print(a)



# a = np.arange(1,11)
# b = np.arange(5,15)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a.min())
# print(min(b))

# #sum
# print(a.sum())
# print(b.sum())
 
# print(b.mean())
# print(b.mean())


# # {low , high , (shape)}

# a = np.random.randint(1, 100 ,(5,5))
# print(a)


# #unique
# a = np.array([1,1,1,1,2,2,2,3,3,3,4,4,56,78,78])
# print(np.unique(a))


# #transpose
# print(np.transpose(a))

####quetsion####
# att={}
# all = ["Rudra" , "Tarun" , "Vikram" , "Yash" , "Ojaswi" , "Vanshika"]
# day1 = ["Rudra" , "Tarun" , "Vikram" , "Yash"]
# day2 = ["Rudra" , "Tarun" , "Ojaswi"]
# day3  = ["Rudra" , "Tarun" , "Ojaswi" , "Vikram"]
# # att = {"day1": day1, "day2": day2, "day3": day3}
# # absent = {}
# # for day, present in att.items():
# #     absent[day] = [s for s in all if s not in present]

# # print(absent)
# for student in all:
#     if student in att and att[student] ==3:
#         print("present for 3 days")
# for student in all:
#     if student in att and att[student] ==3:
#         print("present for 2 days")
        
# for student in all:
#     if student in att and att[student] ==3:
#         print("present for 1 days")
# for student in all:
#     if student in att and att[student] ==3:
#         print("present for 0 days")


# movies = { 
# "Obsession" : {
#     "tickets" : 10;
#     "price" : 367;
#     "ratings" : 8.9
# },
# "Teach you a lesson" : {
#     "tickets" : 50;
#     "price" : 256;
#     "ratings" : 6.6
# },
# "From" : {
#     "tickets" : 80;
#     "price" : 551;
#     "ratings" : 9.1
# },
# "Odyessy" : {
#     "tickets" : 36;
#     "price" : 330;
#     "ratings" : 7.4
# }
# }
# # --- Display all movies --- #
# print("=== NOW SHOWING ===")
# for movie, info in movies.items():
#     status = "Available" if info["tickets"] > 0 else "Housefull"
#     print(f'{movie} | Price: ₹{info["price"]} | Rating: {info["ratings"]} | Tickets: {info["tickets"]} | {status}')



# list_of_movies = []
# while True:
#     operation = input("Enter : ")
#     if operation == "buy":
#         ticket = int(input("Available : "))






