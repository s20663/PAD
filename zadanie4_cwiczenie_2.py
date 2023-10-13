# CODE HERE
def unique_list(input_list):
    return list(set(input_list))


# CODE HERE
if __name__ == '__main__':
    my_list = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]
    print(unique_list(my_list))
    print("-=-=-=-=-=-")
    unique_list = list(set(my_list))
    print(unique_list)

