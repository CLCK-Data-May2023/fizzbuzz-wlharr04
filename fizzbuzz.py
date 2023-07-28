for i in range(1,101):
    output_string = ""
    if i % 3 != 0 and i % 5 != 0:
        output_string += str(i)
    if i % 3 == 0:
        output_string += "Fizz"
    if i % 5 == 0:
        output_string += "Buzz"
    print(output_string)