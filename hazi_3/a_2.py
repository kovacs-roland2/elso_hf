numbers = {'a': 3, 'b': -4}
equation = "a+b+a+a"

result = sum([numbers[i] for i in equation.split("+")])
print(result)