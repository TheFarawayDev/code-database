def remove_sort_reverse(my_list):
    while "eggplant" in my_list:
        my_list.remove("eggplant")
    my_list.sort()
    my_list.reverse()
    print("List after removing eggplant, sorting, and reversing:", my_list)
    return my_list

print(remove_sort_reverse(["eggplant", "apple", "zucchini", "rambutan", "grapefruit"]))
print(remove_sort_reverse(["men in black", "fresh prince of bel-air", "hitch", "eggplant"]))