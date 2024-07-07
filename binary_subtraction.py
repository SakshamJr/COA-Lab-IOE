def make_same_len(x, y):
    return (x.zfill(8), y.zfill(8))

def full_adder(x, y, cin):
    sum = (x + y + cin) % 2
    cout = int((x + y + cin) / 2)
    return (sum, cout)


def binary_adder(x, y, cin=0):
    l = len(x)
    sum = ""
    carry = cin
    for i in range(l - 1, -1, -1):
        bit_sum, carry = full_adder(int(x[i]), int(y[i]), carry)
        sum = str(bit_sum) + sum
    return sum


def binary_multiplication(x, y, count):
    sum = "0" * len(x)
    for i in range(count):
        if y[-1] == "1":
            sum = binary_adder(sum, x)
        x = x[1:] + "0"
        y = "0" + y[:-1]
    return sum


def twos_complement(y):
    inverted_y = "".join("1" if bit == "0" else "0" for bit in y)
    carry = 1
    result = ""
    for i in range(len(inverted_y) - 1, -1, -1):
        sum_bit, carry = full_adder(int(inverted_y[i]), 0, carry)
        result = str(sum_bit) + result
    return result


x = input("Enter first number X: ")
y = input("Enter second number Y: ")
x, y = make_same_len(x, y)
choice = int(input("Enter 1 for Subtraction and 2 for Multiplication: "))
if choice == 1:
    sum = binary_adder(x, twos_complement(y))
    print(f"Difference = {sum}")
elif choice == 2:
    product = binary_multiplication(x, y, len(y))
    print(f"Product = {product}")
