import morph

def flatten(iterable_list):
    result = []
    for el in iterable_list:
        if isinstance(el, list) or isinstance(el, tuple):
            result.extend(flatten(el))
        else:
            result.append(el)
    return list(filter(lambda x: x is not None, result))

    ### SOLUTION WITH THE USE OF MORPH PACKAGE ###

    # result =  morph.flatten(iterable_list)
    # if any(x == None for x in result):
    #     return list(filter(lambda x: x is not None, result))
    # else:
    #     return result
