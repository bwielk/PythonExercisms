def triplets_with_sum(sum_of_triplet):
    results = []
    for b in range(1, sum_of_triplet):
        #print("current number b====> %s" % b)
        for a in range(1, b):
            #print("current number a====> %s" % a)
            c = (a**2 + b**2)**0.5
            if a+b+c == sum_of_triplet:
                results.append((int(a), int(b), int(c)))
    return set(sorted(results))
