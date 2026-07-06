### String Slicing
a = "Harry Potter and the Goblet of fire"

print(a)
print(a[0:5])
print(a[6:12])

print(a[:5]) ## Default Automatic Start Value
print(a[-4:]) ## Default Automatic Ends Value

b = "0123456789"
print(b)
print(b[::2]) #Here start / ending value not defin, direct step value defin
print(b[::3]) #Here start / ending value not defin, direct step value defin
print(b[:7:2]) #Gap/Step value is 2, as you wish you can set, 3, 4 etc.
print(b[:7:3]) #Gap/Step value is 2, as you wish you can set, 3, 4 etc.
print(b[::-1]) ## Revers String
print(b[6::-1]) ## I want this string revers start with 6543210
