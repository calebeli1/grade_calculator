#Build a program that calculates and displays students' grades based on their scores
#THINGS NEEDED: 
# 1. Define a function called grade_calculator
# 2. Parse an argument to receive students names and test scores
# 3. Write a function that calculates the grades by accepting scores and convert them
# to pecentages
# 4. Return the grade point, student name, score percentage

def grade_calculator(stu_name, test_score):
    stu_name = stu_name
    test_percent = float(round(test_score))
    if test_score >= 85:
        grade_point = "A+"
    elif test_score >= 75:
        grade_point = "A"
    elif test_score >= 70:
        grade_point = "B"
    elif test_score >= 60:
        grade_point = "C"
    elif test_score >= 50:
        grade_point = "D"
    elif test_score >= 45:
        grade_point = "E"
    else:
        grade_point = "Fail"
    return print(f"{stu_name} got {test_percent}% which is a: {grade_point}")

stu_name = str(input("Enter students full name: "))
test_score = float(input("Enter your score: "))
print(grade_calculator(stu_name, test_score))




# test_score = float(input("Enter your score: "))
# print("Your score percentage is: ", round(test_score), "%")