# This program is designed to calculate the average value of a list of integers, but without using the sum() function.

# The below line of code instructs the Python interpreter to split a string (given by the user as an input) into a list,
# and to store the resultant list in a variable "student_heights". The list will be a list of strings.

studentHeights = input("Input a list of student heights.\n").split()
for n in range(0, len(studentHeights)):
  studentHeights[n] = int(studentHeights[n])


# Important You should not use the sum() or len() functions in your answer. You should try to replicate their
# functionality using what you have learnt about for loops.

sumStudentHeights = 0
for height in studentHeights:
    sumStudentHeights += height
print(sumStudentHeights)

sumStudents = 0
for student in studentHeights:
   sumStudents += 1
print(sumStudents)

avgHeight = round(sumStudentHeights / sumStudents)
print(avgHeight)