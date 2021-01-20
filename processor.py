
def process_numbers(my_list):
    new_list = []
    
    if type(my_list) == list:
        for i in my_list:
            if type(i) == int or  i.isnumeric():
                new_list.append(int(i))
                new_list.sort()
               
        return new_list
    else:
        return new_list


def process_names(my_list):

    new_list = []

    if type(my_list) == list:
        for i in my_list:
            if type(i) == str and  i.isalpha():
                new_list.append(i)
                new_list.sort()
               
        return new_list
    else:
        return new_list
