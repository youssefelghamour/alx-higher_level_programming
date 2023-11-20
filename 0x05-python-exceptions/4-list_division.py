#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0]*list_length
    for i in range(list_length):
        try:
            new_element = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            new_element = 0
        except ZeroDivisionError:
            print("division by 0")
            new_element = 0
        except IndexError:
            print("out of range")
            new_element = 0
        finally:
            new_list[i] = new_element
    return new_list
