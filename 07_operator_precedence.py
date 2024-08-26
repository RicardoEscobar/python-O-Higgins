"""
Operator Precedence.
Associativity and Order of
Evaluation.
"""

# Operator Precedence
# 1. Parentheses
# 2. Exponentiation
# 3. Multiplication, Division, Floor Division, Modulus
# 4. Addition, Subtraction

# 1. Parentheses
print((15 + 5) * 5)  # 100

# 2. Exponentiation
print(15 + 5 ** 2)  # 40

# 3. Multiplication, Division, 
# Floor Division, Modulus
print(15 + 5 * 2)  # 25
print(15 + 5 / 2)  # 17.5
print(15 + 5 // 2)  # 17
print(15 + 5 % 2)  # 16

# 4. Addition, Subtraction
print(15 + 5 - 2)  # 18

# Combining Operators
print(15 + 5 * 2 ** 2)  # 35
print(20 - 5 // 2)  # 18
print(15 + 5 * 2 - 2)  # 23
