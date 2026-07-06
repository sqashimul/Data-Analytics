#String Python Functions Methods

# endswith() - Returns true if the string ends with the specified value
a = "Harry Potter"
print(a.endswith("r"))
print(a.endswith("P"))
print(a.endswith("t", 6, 9))

# starwith() - Returns true if the string starts with the specified valur
a = "Harry Potter"
print(a.startswith("H"))
print(a.startswith("h"))
print(a.startswith("P"))
print(a.startswith("P",6,9))

# swapcase() - Swaps cases, lower case becomes upper case and vice versa
a = "Harry Potter"
print(a.swapcase())

# strip() - Returns a trimmed version of the string
a = "       Harry Potter    "
print(a)
print(a.strip())
a = "   *** Harry Potter  .....  "
print(a.strip())
print(a.strip("., *, "))
# split() - Splits the string at the specified separator, and returns a list
a = "#OOFD#BRB#OMY#TB"  ### Hast Tag - OOFD = Output of the Day
                        ### BRB =
                        ### OMY = On My Way
                        ### TB = Through Back
print(a.split("#"))
a = "OOFD#BRB#OMY#TB"
print(a.split("#"))
b= "hello. my name is john. i am 23 years old"
print(b.split("."))

# ljust() - Returns a left justified version of the string
a = "Harry Potter"
x= a.ljust(20)
x= a.ljust(20, "*")
print(x, "is my favorite movie")

# rjust() - Returns a right justified version of the string
a = "Harry Potter"
x = a.rjust(20)
print(x)
x = a.rjust(40, "~") ## Along with ~~~~~~~~Harry Potter this 40
print(x, "is my favourite movie")
# replace() - Returns a string where a specified value is replaced with a specified value
a = "My name is Tanzim. Tanzim like Soccer"
print(a.replace("Tanzim", "Shail"))

# rindex() - Searches the string for a specified value and returns the last position of where it was found
a = "Harry Potter and the Prisoner of Azkaban"
print(a.rindex("Prisoner"))
print(a.rindex("Harry"))
print(a.rindex("a", 6, 20))

# rfind() - Searches the string for a specified value and returns the last position of where it was found
a = "Harry Potter and the Prisoner of Azkaban"
print(a.rfind("Potter"))
b = "bibidy bobidy boo"
print(b.rfind("dy",6,14))
print(b.rfind("i",6,14))