
def calc():
    x_values = list(range(-10, 11))
    y_values = []
    for x in x_values:
        y = x**3 - 2*x + 1
        y_values.append(y)
    
    for i in range(len(x_values)):
        print("x =", x_values[i], "y =", y_values[i])

calc()