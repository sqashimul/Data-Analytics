## Slicing Lists
a = ["Ironman", "Thor", "Captain America", "Hulk"]
print(a)
print(a[2])
print(a[-3])
print(a[1])

print(a[1:3]) ## Lists Slicing
print(a[:2])
print(a[1:])

print(a[::2]) ## Lists gap/step use
print(a[-3:-1]) ## Use negative index
print(a[-3:])
print(a[-3::2])
print(a[::-1]) ## Lists Reverse ['Hulk', 'Captain America', 'Thor', 'Ironman']
print(a[-1:-4:-1]) ## Reverse but particular value ['Hulk', 'Captain America', 'Thor']
