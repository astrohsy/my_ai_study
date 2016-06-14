def read_data(names_name, train_name, delimeter1=' ', delimeter2=' '):
    names_file = open(names_name)
    target_attr = names_file.readline().split()

    to_index = {0: 0}
    attributes = {}
    for i, line in enumerate(names_file):
        label, *attr_data = line.rstrip('\n').split(delimeter1)
        to_index[label] = i + 1
        attributes[label] = attr_data
    names_file.close()

    train_file = open(train_name)

    train_set = []
    for line in train_file:
        train_set.append(line.rstrip('\n').split(delimeter2))
    train_file.close()

    return to_index, attributes, train_set, target_attr


def read_test_data(test_name, delimeter=' '):
    test_file = open(test_name)

    test_data_set = []
    for line in test_file:
        test_data_set.append(line.rstrip('\n').split(delimeter))
    test_file.close()

    return test_data_set
