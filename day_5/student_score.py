# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])  # type: ignore
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0

# using for loop and if statements to check the highest number in the list
for score in student_scores:
    if score > highest_score:  # type: ignore
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
