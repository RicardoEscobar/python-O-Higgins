"""Binary numbers and the bin() function."""

# The bin() function converts an integer to a binary string.
print(bin(0))  # 0b0
print(bin(1))  # 0b1
print(bin(2))  # 0b10
print(bin(3))  # 0b11
print(bin(4))  # 0b100
print(bin(5))  # 0b101

# Get the decimal value of a binary number.
print(int('0b111', 2))  # 7
print(int('0b1010', 2))  # 10
print(int('0b1100', 2))  # 12
