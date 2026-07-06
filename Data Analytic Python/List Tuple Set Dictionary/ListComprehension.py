## List Comprehension
## Kono ek list er value onno kono list er moddhe copy korakei bujhay
## List copy in another list means list comprehension

l1 = [30,40, 50,60]

l2 = []
for i in l1:
    l2.append(i)

print(l1, "\n", l2)
## Value 45 above then
l2 = []
for i in l1:
    if i > 45:
        l2.append(i)

print(l1, "\n", l2)
## List Comprehension method means above code in a one liner
l3 = [ i for i in l1]
print(l3)

l3 = [ i for i in l1 if i > 45]
print(l3)


