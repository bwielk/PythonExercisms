SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL
    if first_list in check_if_block_of_elements_exists(first_list, second_list):
        return SUBLIST
    if second_list in check_if_block_of_elements_exists(second_list, first_list):
        return SUPERLIST
    return UNEQUAL


def check_if_block_of_elements_exists(block_of_elements, list_to_compare_with):
    results = []
    if len(block_of_elements) > 0:
        first_element_of_a_block = block_of_elements[0]
        for i in range(0, len(list_to_compare_with)):
            if list_to_compare_with[i] == first_element_of_a_block:
                new_list_with_found_els = list_to_compare_with[i: i+len(block_of_elements)]
                results.append(new_list_with_found_els)
        return results
    else:
        results.append([])
        return results