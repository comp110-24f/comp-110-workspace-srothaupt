def number_info(num: int) -> int:
    if num < 10:
        print("Small number.")
    else:
        if num % 2 == 0:
            print("Even number.")
        else:
            print("Odd number.")
    return num


number_info(num=11)
print(number_info(num=4))
