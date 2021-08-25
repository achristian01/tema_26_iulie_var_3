# This is a sample Python script.

def ssum(*args):
    args_list = list(args)
    print("This is the list or our arguments: ", args_list)
    sum_args = 0
    for i in args_list:
        if type(i) == int or type(i) == float:
            sum_args += i

    return print("The sum of numeric arguments in our list is: ", sum_args)

ssum("q", "a", 5, 5, 3.0)