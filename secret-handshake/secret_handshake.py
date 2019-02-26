dict_of_secret_code_actions = {1: 'wink',
                               10: 'double blink',
                               100: 'close your eyes',
                               1000: 'jump'}


def handshake(code):
    result = []
    code_in_binary_code = int('{0:b}'.format(code))
    code_in_binary_code_for_loop_copy = \
        code_in_binary_code - 10000 if code_in_binary_code >= 10000 else code_in_binary_code

    points_in_incremental_order = sorted(dict_of_secret_code_actions.keys())
    points_in_decremental_order = points_in_incremental_order[::-1]
    for points in points_in_decremental_order:
        if code_in_binary_code_for_loop_copy >= points:
            code_in_binary_code_for_loop_copy -= points
            result.append(dict_of_secret_code_actions[points])
    return result if code_in_binary_code >= 10000 else result[::-1]


def secret_code(actions):
    actions_in_decremental_order_of_keys = \
        [dict_of_secret_code_actions[k] for k in sorted(dict_of_secret_code_actions.keys())]
    result_in_binary = 0
    current_actions_values = []
    for action in actions:
        for k, v in dict_of_secret_code_actions.items():
            current_actions_values.append(k) if dict_of_secret_code_actions[k] == action else False

    # Checks if the list of generated point values for actions is in ascending or descending order.
    # This will help us define if the binary for searched value was larger than 10000
    are_actions_points_descending = \
        all(current_actions_values[i] >= current_actions_values[i+1] for i in range(len(current_actions_values)-1))

    result_in_binary += 10000 if are_actions_points_descending and len(actions) > 1 else False
    for action in actions:
        index_of_action_in_dict_of_actions = actions_in_decremental_order_of_keys.index(action)
        result_in_binary += sorted(dict_of_secret_code_actions.keys())[index_of_action_in_dict_of_actions]
    result_translated_from_binary_to_int = (int('0b' + str(result_in_binary), 2))
    return result_translated_from_binary_to_int
