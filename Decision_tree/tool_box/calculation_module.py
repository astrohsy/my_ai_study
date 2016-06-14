import math
from functools import reduce


def cal_entropy(portion):
    total = reduce(lambda x, y: x + y, portion)
    res = 0.0
    for p in portion:
        if p == 0:
            return 0
        res += (p / total) * math.log2(p / total)
    return -res


def cal_gain(data_set, attribute, attributes, target_attr, to_index):
    classed_data_set = div_set(data_set, 0, attributes, target_attr, to_index)
    res_gain = cal_entropy([len(classed_data_set[0]), len(classed_data_set[1])])

    total = len(data_set)
    for sub_data_set in div_set(data_set, attribute, attributes, target_attr, to_index):
        sub_classed_data_set = div_set(sub_data_set, 0, attributes, target_attr, to_index)
        sub_p = []

        sub_total = 0
        for one_classed_data in sub_classed_data_set:
            sub_total += len(one_classed_data)
            sub_p.append(len(one_classed_data))
        res_gain -= sub_total / total * cal_entropy(sub_p)

    return res_gain


def div_set(data_set, attribute, attributes, target_attr, to_index):
    res_set = []

    if attribute == 0:
        for state in target_attr:
            res_set.append([datum for datum in data_set if datum[to_index[attribute]] == state])
    else:
        for state in attributes[attribute]:
            res_set.append([datum for datum in data_set if datum[to_index[attribute]] == state])
    return res_set


def cal_most_common_value(learning_set, target_attr):
    fre = {}
    for target_state in target_attr:
        fre[target_state] = 0
        for datum in learning_set:
            if datum == target_state:
                fre[target_state] += 1
    return max(fre)
