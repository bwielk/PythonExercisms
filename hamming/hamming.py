def distance(strand_a, strand_b):
    mismatch_counter = 0
    validate_if_strands_are_both_strings(strand_a, strand_b)
    validate_if_strands_are_of_the_same_length(strand_a, strand_b)
    try:
        if strand_a == strand_b:
            return 0
        else:
            for i in range(0, len(strand_a)):
                if strand_a[i] != strand_b[i]:
                    mismatch_counter += 1
            return mismatch_counter
    except IndexError:
        print("Process finished")

def validate_if_strands_are_of_the_same_length(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Both strings have to be of the same length e.g. ABC and EDF")

def validate_if_strands_are_both_strings(strand_a, strand_b):
    if not isinstance(strand_a, str) or not isinstance(strand_b, str):
        raise ValueError("The arguments must be strings")
