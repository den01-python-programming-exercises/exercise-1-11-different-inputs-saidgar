def main():
    #write your code below this line
    input1 = input("Give a string:")
    input2 = int(input("Give an integer:"))
    input3 = float(input("Give a float:"))
    input4 = input("Give a boolean:")
    result = False
    if input4 == "True":
        result = True
    print("You gave the string " + str(input1))
    print("You gave the integer " + str(input2))
    print("You gave the float " + str(input3))
    print("You gave the boolean " + str(result))

if __name__ == '__main__':
    main()
