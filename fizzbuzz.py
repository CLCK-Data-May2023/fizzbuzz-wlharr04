for i in range(1,101):
    output_string = ""
    if i % 3 == 0:
        output_string += "Fizz"
    if i % 5 == 0:
        output_string += "Buzz"
    if output_string == "":
        output_string += str(i)
    print(output_string)