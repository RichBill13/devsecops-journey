def main():
    expression = input("Expression: ")
    print(calculate(expression))

def calculate(exp):
    exp = exp.lower().strip()
    exp = exp.split(" ")
    num1 = float(exp[0])
    num2 = float(exp[2])


    match exp[1]:
        case "+":
            return f"{num1 + num2:.1f}"
        case "-":
            return f"{num1 - num2:.1f}"
        case "*":
            return f"{num1 * num2:.1f}"
        case "/":
            return f"{num1 / num2:.1f}"

main()