# This code is like a shopping list, you can make changes to it
# When you add an item to the list with the index number of the item it adds it to the list
# and when you exit the program but entering 0, it prints out all the things you added to the list
# Take note that w hen testing the program, if you input an index that was already in the list before,
# It removes it from the list
# Have fun learning


available_parts = ["computer",
                   "monitor",
                   "mouse",
                   "dvd cable",
                   "laptop",
                   "mouse mat",
                   "printer",
                   "hdmi cable"]
chosen_parts = "-"
computer_parts = []
valid_parts = [str(i) for i in range(1, len(available_parts) + 1)]
while chosen_parts != "0":
    if chosen_parts in valid_parts:
        index = int(chosen_parts) - 1
        chosen_parts = available_parts[index]
        if chosen_parts in computer_parts:
            computer_parts.remove(chosen_parts)
            print("Removing {} from the list".format(chosen_parts))
        else:
            computer_parts.append(chosen_parts)
            print("Adding {} to the list".format(chosen_parts))
        print("Your lists now includes {}".format(computer_parts))
    else:
        print("please add options from the list below")
        for number, parts in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, parts))

    chosen_parts = input()
print(computer_parts)


