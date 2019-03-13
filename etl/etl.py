def transform(legacy_data):
    results = {}
    for x in range(1, 11):
        try:
            value = legacy_data[x]
            for i in range(0, len(value)):
                results[value[i].lower()] = x
        except KeyError:
            continue
    return results
