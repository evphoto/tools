#!/usr/bin/env python3

def value_exists(look_up_value: str, look_up_list: list):
    """ Function find if provided value exists within
        the provided list

        Args:
            look_up_value (str): value to be found

            look_up_list (list): list of values

        Returns:
            return_status: (int): 1 if found, 0 if not found
    """
    
    if look_up_value in look_up_list:
        print(f'value was found')
        return 1
    else:
        print(f'value not found')
        return 0