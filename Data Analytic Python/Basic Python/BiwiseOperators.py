# Bitwise Operators
# for Binary

print(bin(10))
print(bin(8))
a = 10  #binary 10 = 1010
b = 8   #binary 8 = 1000
# AND operation
print(a & b) # And operation both a & b result should: 8 = 1000
print(bin(a & b)) #output = 0b1000
# OR operation
print(a | b) # OR operation both a & b result should: 10 = 1010
print(bin(a | b)) #output = 0b1010
# XOR operation
print(a ^ b)  # XOR operation both a & b result should: 2 = 0010
print(bin(a ^ b))  #output = 0b10

# Zero fill Left shift binary using
#10 = 1010 =  10>>2 = 0010 = 2; fill left side  two zero
#10 = 1010 =  10>>1 = 0101 = 5; fill left side one zero
print(10>>2)
print(10>>1)
# Zero fill Right shift binary using
#10 = 1010 =  10<<2 = 101000 = 40; fill Right side  two zero
#10 = 1010 =  10<<1 = 10100 = 20; fill Right side one zero
print(10<<2)
print(10<<1)
print(bin(40))
print(bin(20))
