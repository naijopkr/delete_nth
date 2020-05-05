def delete_nth(n, num_list):
    num_map = dict()
    out_list = []

    for num in num_list:
        try:
            num_map[num] += 1
        except KeyError:
            num_map[num] = 1

        if num_map.get(num) <= n:
            out_list.append(num)

    return out_list
