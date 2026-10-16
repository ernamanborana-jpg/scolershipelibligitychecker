name = (input("Enter your name: "))
age = int(input("enter your age: "))
marks = float(input("Enter your marks in last passed exam : "))
income = float(input("Enter family income: "))
category = input("Enter your category (General/OBC/SC/ST): ")

if category == "General":
    if age <= 18 and marks >= 70 and income <= 300000:
        print(" You are eligible.")
    else:
        print(" You are not eligible.")
elif category == "OBC":
    if age <= 20 and marks >= 60 and income <= 300000:
        print("You are eligible.")
    else:
        print("You are not eligible.")

elif category == "SC":
    if age <= 21 and marks >= 50 and income <= 500000:
        print(" You are eligible.")
    else:
        print(" You are not eligible.")

elif category == "ST":
    if age <= 21 and marks >= 50 and income <= 500000:
        print("You are eligible.")
    else:
        print(" You are not eligible.")

else:
    print("Invalid category.")