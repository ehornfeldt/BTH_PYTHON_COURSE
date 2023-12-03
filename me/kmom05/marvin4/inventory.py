#!/usr/bin/env python3

""" Bag file """

def pick(bag, items, position = -1):
    """ 
    A function who takes a bag with items where more items can be added 
    to a list with a specified position or at the end of the list 
    """
    items_list = items.split(",")
    if int(position) > len(bag):
        print("Error: Index ", position, " är för högt")
    elif int(position) >= 0:
        bag[int(position):int(position)] = items_list
        print("Du har lagt in ", items, " på plats ", position, " i ryggsäcken")
    else:
        bag.extend(items_list)
        print("Du har lagt in ", items, " längst bak i ryggsäcken")
    
    return bag


def inventory(bag, start = False, stop = False):
    """ Get lenght and content of bag between start and stop """
    if start and stop:
        temp = bag[int(start):int(stop)]
        print("Antalet saker i ryggsäcken ", len(temp), " och alla saker är: ", temp)
    else:
        print("Antalet saker i ryggsäcken ", len(bag), " och alla saker är: ", bag)

    


def drop(bag, item):
    """ Remove item from bag """
    try:
        bag.remove(item)
        print("Saken som kastades är ", item)
    except ValueError:
        print("Error: ", item, " finns inte i ryggsäcken")
    
    return bag


def swap(bag, item_one, item_two):
    """ Swap two items in the bag """

    try:
        index_item_one = bag.index(item_one)
        index_item_two = bag.index(item_two)
        bag[index_item_two] = item_one
        bag[index_item_one] = item_two
    except ValueError:
        print("Error: ", item_one, " och/eller ", item_two, " finns inte i ryggsäcken")

    print("Sakerna som bytte plats är: ", item_one, " och ", item_two)

    return bag
