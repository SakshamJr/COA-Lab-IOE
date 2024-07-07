from binary_subtraction import binary_adder

def adjust_number(x, y):
    l1, l2 = len(x), len(y)
    # For n-bit multiplication, the result is 2n-bit
    max_bit = max(l1, l2)
    x = x.rjust(2 * max_bit, "0")
    y = y.rjust(2 * max_bit, "0")
    return (x, y)


def binary_multiplication(x, y, count): # 1011, 0001, 2
    sum = "0" * len(x)                  # 0000
    for i in range(count):              # 2
        if y[-1] == "1":                
            sum = binary_adder(sum, x)  # 0000 + 1011 # 1011 + 1011
        x = x[1:] + "0"                 # 0110 
        y = "0" + y[:-1]                # 01
    return sum


if __name__ == "__main__":
    x = input("Enter multiplicand: ") # 1011
    y = input("Enter multiplier: ")   # 11
    count = len(y)  # no of bits in y # 2
    x, y = adjust_number(x, y)        # 1011, 0001
    product = binary_multiplication(x, y, count) 
    print(f"Product = {product}")
