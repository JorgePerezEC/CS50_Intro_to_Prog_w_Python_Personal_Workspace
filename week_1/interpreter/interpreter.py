def main():
    user = input("Expression: ")
    x, op, z = user.split(" ")
    x_num = float(x)
    z_num = float(z)
    result = evaluate_operation(x_num, z_num, op)
    print(f"{result:.1f}")

def evaluate_operation(x, z, simb):
    if simb == "+":
        return x+z
    elif simb == "-":
        return x-z
    elif simb == "/":
        return x/z
    elif simb == "*":
        return x*z

main()

