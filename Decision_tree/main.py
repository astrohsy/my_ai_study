from tool_box import fileio_module as io
from tool_box import tree_module as tm

test_file = "data/mushroom"
to_index, attributes, train_set, target_attr = io.read_data(test_file+".names", test_file+".train", ' ', ',')

root = tm.DecisionTree(train_set, attributes, target_attr, to_index)
root.build_tree()

test_set = io.read_test_data(test_file+".test", ',')

cnt_success, total = 0, 0
for test in test_set:
    total += 1
    if test[0] == root.check_data(test):
        cnt_success += 1

root.pprint()

print("Accuracy rate : ", "%.5f%%" % (cnt_success / total * 100))
