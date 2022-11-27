# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0

# using for loop to get the sum of the height
for height in student_heights: 
    total_height += height  

total_students = 0

# using for loop to get the number of students
for student in student_heights:  
    total_students += 1

avg_height = (total_height/total_students)

print(round(avg_height))