#  read from file and split by new line char into list
def read_file():
    with open("input1.txt") as f:
        lines = f.read().splitlines()
    return lines


def main():
    lines = read_file()
    #  go throw the listt
    total = 0
    for line in lines:
        first_char = 0
        last_char = 0

        #  go throw the each char and find the sava the cahr if number only the first and the last char
        for char in line:
            if char.isdigit():
                if first_char == 0:
                    first_char = char
                last_char = char
                # print the first and the last char
        # print("first char is: " + first_char)
        # print("last char is: " + last_char)
        # now combine the first and the last char and make it one number of two digits the first is tens and the last is units
        #  convert to int
        first_char = int(first_char)
        last_char = int(last_char)
        #  combine the first and the last char
        result = first_char * 10 + last_char

        #  print the result
        # print("the result is: " + str(result))
        #  now calculate the result of all  the result
        #  now add the result to the total
        total = total + result
        #  print the total
    print("the total is: " + str(total))


if __name__ == "__main__":
    main()
