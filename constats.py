#You live in a country with only 2 tax brackets. Everyone earning less Ghs12,000 pays 25% in taxes and everyone earning
#earning Ghs12,000 or more pays 30%. Write a function to display how much tax a worker owes.

"""def get_taxes(earnings):
    
    if earnings < 12000:
        tax_owed = earnings * 0.25
    else:
        tax_owed = earnings * 0.3

    return tax_owed

get_taxes = get_taxes(25000)
print(f"Your current tax owed GRA is Ghs{get_taxes}")
"""

""""
#Define a function to accept a number as input and adds 3 if the input is less than 10, and otherwise add 8
def num_test(num):
    if num < 10:
        num_output = num + 3
    else:
        num_output = num + 8
    return num_output

num = input("Enter any number ")
num = float(num)
num_test = num_test(num)
print("Number is:", num_test)

numbers = range(80,90,1)
print(list (numbers))
"""

"""
def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"
    else :
        grade = "F"
    return grade

print(get_grade(20))
"""
"""def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10 * len(engraving)
    else:
        cost = 50 + 7 *len(engraving)
    return cost


print(cost_of_project("Caleb Adala", True))
"""

""""
#Calculate water bill for water gallons ranging 0-8000 = $5, 8001-22000 = $6
# 22001-30000 = $$7, 30001+ = $10. NOTE: prices are per gallon
def get_water_cost(num_gallons):
    if num_gallons <= 8000:
        bill = num_gallons/1000 * 5
    elif num_gallons <= 22000:
        bill = num_gallons/1000 * 6
    elif num_gallons <= 30001:
        bill = num_gallons/1000 * 7
    else:
        bill  = num_gallons/1000 * 10
    return bill 

print(get_water_cost(50000))
"""
"""
age_students = [12, 14, 16, 17, 15, 22, 19, 13, 20, 21]
age_students.append(25)
age_students.append(35)
age_students.remove(35)
print(age_students)
print(age_students[:3])
print(age_students[-3:])
print("The sum of the ages of the students is", sum(age_students))
print("The average age of the class is:", sum(age_students)/11)
print("Indexing student number 7:", age_students[7])
print("The total number of students in the class is:", len(age_students))
print("The oldest student is:", max(age_students))
print("The youngest student is:", min(age_students))

#You can use the .split function to convert a series of strings in python into a list. E.g print(menu.split(",")) NB: depending on what is used in sepating the strings,
#you will have to change the separator in the "" marks. It can be . or , or / etc
menu = "gobe, waakye, banku, tuo-zaafi, abolo, fufu"
print(menu.split(","))

class_marks = "12, 20, 45, 30, 53, 61, 87, 26"
print(class_marks.split(","))
"""
"""
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1]) / num_users[len(num_users)-yrs_ago-1] 
    return growth

num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

print(percentage_growth(num_users_test, 1))
print(percentage_growth(num_users_test, 7))
"""
"""print(5//2)
print(5/2)

alice_candies = 121
bob_candies = 71
carol_candies = 89

smash_candies = (alice_candies + bob_candies + carol_candies) % 3

print(smash_candies)
"""
help(dict)