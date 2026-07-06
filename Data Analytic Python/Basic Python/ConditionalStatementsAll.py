## If Statement
marks = 97
if marks >= 90:
    print("You will get a mobile phone")

print("Thank You")
##If - else Statement
marks = 87
if marks >= 90:
    print("You will get a mobile phone")
else:
    print("No phone for 1 week")

print("Thank You")
##If-elif-else Statement
marks = 65
if marks >= 90:
    print("You can to to a trip")
elif marks >= 80 and marks < 90:
    print("You will get a New Phone")
elif marks >= 70 and marks <= 80:
    print("You will get a new book")
else:
    print("You will not get your phone back")
print("Thank You")
##Nested If Statement
marks = 96
if marks >= 80:
    print("You will get a mobile phone")
    if marks >= 95:
        print("You can fo to a trip")
else:
    print("No phone for a month")
## Short hand if Statement
## One Liner Statemnet; if conditon: Body of if
marks = 86
if marks >= 85: print("You will get a new phone")
## Short Hand if-else Statement
## Body of if - if condition else - body of else
marks = 85
print("You will go to a trip") if marks >= 90 else print("you will get back phone")


