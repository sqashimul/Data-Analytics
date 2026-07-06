### Nested Loop
### A loop inside a loop is called as nested loop.
### Nested loops are also used to solve patter

# for i in range (1,4):
#     for j in range (1,11):
#         print(j)
#     print()
# for i in range (1,4):
#     for j in range (1,11):
#         print(j, end = "")
#     print()
        ### Pattern problem
                 ###Outers count to Rows
        ###Inners count to Columns
# for i in range (1,6):
#     for j in range (1, i+1):
#         print(j, end = "")
#     print()
for i in range (1,6):
    for j in range (1, i+1):
        print(j, end = " ")
    print()