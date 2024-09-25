x: int = 10
result: str = ""

while x > 0:
    if x % 3 == 0:
        result = result + str(x)
        print(result)
    else:
        result = str(x) + result
        print(result)
    x = x // 2
print(result)
