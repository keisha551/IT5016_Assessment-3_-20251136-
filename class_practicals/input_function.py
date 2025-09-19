'''

ask user to enter the grade
calculating average grades
display the total grade
'''

# input grade from user
grade1=int(input("enter grade :"))
grade2=int(input("enter grade :"))
grade3=int(input("enter grade :"))
grade4=int(input("enter grade :"))
#calculate average
total_grades=grade1+grade2+grade3+grade4
print(total_grades)
average=total_grades/4
print(average)
# shows to the user their average
print("average:",average)
# determines the total_grades using the average
if(total_grades>=80):
    print("A")
elif(total_grades>=60):
    print("B")
elif(total_grades>=50):
    print("C")
else:
    print("fail")

