from item import *


def write_to_file(file_data):
    try:
        file = open("inventory.txt", "w")
        for x in file_data:
            file.write(x.fields_as_string() + "\n")
        file.close()
    except FileNotFoundError:
        print("unknown error has happen :(")
        return -1


def read_from_file():
    list_of_items = []
    try:
        file = open("inventory.txt")
        for x in file:
            temp_list = x.split(",")
            list_of_items.append(Item(int(temp_list[0]), temp_list[1], int(temp_list[2]), float(temp_list[3])))
        file.close()
        return list_of_items
    except FileNotFoundError:
        file = open("inventory.txt", "w")
        list_of_items.append(Item(1, "Apple", 50, 0.5))
        list_of_items.append(Item(2, "Banana", 30, 0.3))
        list_of_items.append(Item(3, "Orange", 20, 0.7))
        write_to_file(list_of_items)
        return list_of_items
    except FileExistsError:
        print("unknown error has happen :(")
        return -1
