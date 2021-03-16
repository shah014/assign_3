n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
ope = input("Enter the operator: ")


def fun(ope):
    if ope == '+':
        return n1 + n2
    elif ope == '-':
        return n1 - n2
    elif ope == '*':
        return n1 * n2
    else:
        try:
            return n1/n2
        except ZeroDivisionError:
            return f"Divide by 0 error"


print(fun(ope))


