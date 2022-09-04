def my_function():
    print("Please select an option from these below")
    print("1:\tPython")
    print("2:\tJava")
    print("3:\tJavascript")
    print("4:\tGolang")
    print("5:\tRuby")
    print("6:\tCSS")
    print("7:\tC++")
    print("0:\tExit")
my_function()
while True:
    choice = input()
    if choice in "1234567":
        print("You chose number {}".format(choice))
    elif choice == "0":
        break
    else:
        my_function()