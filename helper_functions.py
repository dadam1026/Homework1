import os

# Contains helper functions for your apps!

# If the io following files are in the current directory, remove them!
# 1. 'currency_pair.txt'
# 2. 'currency_pair_history.csv'
# 3. 'trade_order.p'
def check_for_and_del_io_files():
    # Your code goes here.
    starting_path = "/Users/derrickadam/PycharmProjects/Homework1"
    dir_list = os.listdir(starting_path)
    for file in dir_list:
        if file == "currency_pair.txt":
            path = os.path.join(starting_path, file)
            os.remove(path)
        if file == "currency_pair_history.csv":
            path = os.path.join(starting_path, file)
            os.remove(path)
        if file == "trade_order.p":
            path = os.path.join(starting_path, file)
            os.remove(path)

    # nothing gets returned by this function, so end it with 'pass'.