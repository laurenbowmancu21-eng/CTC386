#Lauren Bowman
#Lab 2
#CTC 387

print("Enter 6 bits one at a time:")

b5 = int(input("Bit 1): "))
b4 = int(input("Bit 2): "))
b3 = int(input("Bit 3): "))
b2 = int(input("Bit 4): "))
b1 = int(input("Bit 5): "))
b0 = int(input("Bit 6): "))

decimal_value = (b5 * 32) + (b4 * 16) + (b3 * 8) + (b2 * 4) + (b1 * 2) + (b0 * 1)

print(f"The decimal equivalent is: {decimal_value}")
