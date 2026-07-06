# Conditional statements in Python allow you to execute different blocks of code based on
# whether a specific condition is true or false.
# Python uses the if, elif (else if), and else keywords for this logic.
# 1. If the Statement
# 2. If-else Statement
# 3. If-elif-else Statement
# 4. Short Hand if Statement
# 5. Nested Statement

# if Statement: Executes a block of code only if the condition evaluates to True
age = 20
if age >= 18:
    print("You are an adult.")
#else Statement: Catches anything that wasn't caught by the preceding conditions.
temperature = 15
if temperature > 25:
    print("It is hot outside.")
else:
    print("It is cold outside.")
# elif Statement: Checks another condition if the previous conditions were False.
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
#Short Hand if: Use this when you only have a single statement to execute after the condition.
a = 15
b = 11
if a > b: print("a is greater than b")
# A nested conditional is an if statement placed inside the block of another if statement. Use this layout when a secondary check depends entirely on the success of the first check.
# #if external_condition:
#     # Executes if external_condition is True
#     if internal_condition:
#         # Executes only if BOTH conditions are True
#         print("Both are true")

age = 22
is_registered = True

if age >= 18:
    print("Age requirement met.")

    if is_registered:
        print("Access granted: You are fully registered.")
    else:
        print("Access denied: Please register first.")
else:
    print("Access denied: You must be 18 or older.")

