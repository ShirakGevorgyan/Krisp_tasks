def find_min_pledge(pledge_list):
    pledges_set = set(pledge_list)
    if max(pledge_list) <= 0:
        return 1
    for i in range(1, max(pledge_list) + 2):
        if i not in pledges_set:
            return i