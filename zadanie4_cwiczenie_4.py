# CODE HERE
def num_fact(x):
    if x == 0:
        return 1
    else:
        return x * num_fact(x - 1)


if __name__ == '__main__':
    print(num_fact(10))