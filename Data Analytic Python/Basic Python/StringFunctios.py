## String Python Functions
a = "hello"
b = "Hello123"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123@"
g = "1.234"
h = "123hello"
## isalnum - Returns True if all characters in the string are alphanumeric
print(a, a.isalnum())
print(b, b.isalnum())
print(c, c.isalnum())
print(d, d.isalnum())
print(e, e.isalnum())
print(f, f.isalnum())
print(g, g.isalnum())
## isalpha - Returns True if all characters in the string are in the alphabet
print(a, a.isalpha())
print(b, b.isalpha())
print(c, c.isalpha())
print(d, d.isalpha())
print(e, e.isalpha())
print(f, f.isalpha())
print(g, g.isalpha())
## isdecimal - Returns True if all character in the string are Decimals
print(a, a.isdecimal())
print(b, b.isdecimal())
print(c, c.isdecimal())
print(d, d.isdecimal())
print(e, e.isdecimal())
print(f, f.isdecimal())
print(g, f.isdecimal())
## isdigit - Returns True if all character in the string are digits
print(c,c.isdigit())
print(g, g.isdigit())
print(b, b.isdigit())
## isnumeric - Returns True if all character in the string are Numeric
print(b, b.isnumeric())
print(c, c.isnumeric())
print(e, e.isdigit())
print(g, g.isdigit())
## islower - Check if the string is lower case or not
print(a, a.islower())
print(b, b.islower())
print(d, d.islower())
h = "123hello"
print(h, h.islower())
## isupper - Check if the string is Upper case or not
print(a, a.isupper())
print(b, b.isupper())
print(d, d.isupper())
print(h, h.isupper())
i = "Hello"
print(i, i.isupper())
## isspace - Returns True if all characters in the string are whitespaces
print(e, e.isspace()) # Only & Only spaces
print(f, f.isspace())

## istitle - Returns True if the string follows the rules of a title
j = "HELLO everyOne"
k = "Harry Potter And The Goblet Of Fire"
print(a, a.istitle())
print(d, d.istitle())
print(f, f.istitle())
print(j, j.istitle())
print(k, k.istitle())
