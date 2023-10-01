"""
full_name = input("Enter your full name:")
your_location = input("Enter your location:")
your_height = input("Enter your height:")
your_weight = input("Enter your weight:")
fav_car = input("What is your favorite car?")
fav_quote = input("What is your favorite quote?")

your_height = float(your_height)
your_weight = float(your_weight)

text = f"My name is {full_name} and i live at {your_location}. I currently stand at {your_height} feet tall and weighing {your_weight}. My favorite car is {fav_car} and my favorite quote is {fav_quote}"
c="*"*20

print(text)
print(c)
print(text.lower())
print(c)
print(text.upper())
print(c)
print("The length of the text is" + str(len(text)))
print(c)
print("The total number of a's in the text", str(text.count("a")))

"""
