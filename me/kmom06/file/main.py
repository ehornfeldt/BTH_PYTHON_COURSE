#!/usr/bin/env python3
""" main """

filename = "items.txt" # global variable for holding filename

def menu():
    print(
        """
1. Show file content
2. Add item, append
3. Replace content
4. Remove an item
        """
        )
    return int(input("Choice: "))

def choice(inp):
    if inp == 1:
        print(readfile())
    elif inp == 2:
        write_to_file("\n" + input("Item to add: "), "a")
    elif inp == 3:
        replace_content()
    elif inp == 4:
        remove_item()
    else:
        exit()

def readfile():
    # with - as for reading a file automatically closes it after reading is done
    with open(filename) as filehandle:
        content = filehandle.read()
    return content

def write_to_file(content, mode):
    with open(filename, mode) as filehandle:
        filehandle.write(content)

def replace_content():
    item = ""
    result = ""
    while item != "q":
        result += item + "\n"
        item = input("Item to add: ")
    write_to_file(result.strip(), "w")

def remove_item():
    content = readfile()
    remove = input("What item should be removed: ")

    if remove in content: # check if item to remove exists
        if content.index(remove) == 0: # if the item is the first line in the file
            modified_content = content.replace(remove, "")
        else:
            modified_content = content.replace("\n" + remove, "")
        write_to_file(modified_content.strip(), "w")

if __name__ == "__main__":
    while(True):
        choice(menu())