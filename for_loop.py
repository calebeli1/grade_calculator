#Write a list of all students names
#Print with  index position
#Shuffle list
#Print using with item
#Select a random students
#Print it
#Add 3 more names
#Shuffle list
#Print it

import random 

student_list = ["Kristel", "Maya", "Dice", "Precious", "Abena", "Sam", "Peter", "Gracious", "Ernest", "Daniella"]

#print("\n\nThe index position of the students in the class is:")
#for i in enumerate(student_list, start=1):
    #print(i)

#for i in range(len(student_list,)):
    #print(i)

#print a shuffled list of student names
random.shuffle(student_list)
print("\n\n Class list shuffled:")
print(student_list)

#Print the list of all student names
for item in student_list:
    print("\n\n", item, "\n\n")

#Select the name of a random student
print(random.choices(student_list))

#Add 3 more students
student_list.extend(["Patricia", "Nora", "Angela"])
print(student_list)

#Shuffle new name list
random.shuffle(student_list)
print(student_list)




