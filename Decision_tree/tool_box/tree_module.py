from tool_box import calculation_module as cm


class DecisionTree:
    def __init__(self, learning_set=[], attributes={}, target_attr=[], to_index={}, name=None):
        self.learning_set = learning_set
        self.attributes = attributes
        self.target_attr = target_attr
        self.to_index = to_index
        self.name = name
        self.children = {}

    def find_best_attribute(self):
        best_attribute, best_gain = None, -1

        for attribute in self.attributes:
            temp = cm.cal_gain(self.learning_set, attribute, self.attributes, self.target_attr, self.to_index)
            if best_gain < temp:
                best_gain = temp
                best_attribute = attribute

        return best_attribute

    def build_tree(self):

        # case when attributes are all used
        if not self.attributes:
            self.name = cm.cal_most_common_value(self.learning_set, self.target_attr)
            return

        # case when all data has same target value
        count = [check[0] for check in self.learning_set]
        if set(count).__len__() == 1:
            for target_state in self.target_attr:
                if target_state == count[0]:
                    self.name = target_state
            return
        count.clear()

        best_attribute = self.find_best_attribute()
        self.name = best_attribute

        divided_learning_set = cm.div_set(self.learning_set, best_attribute,
                                          self.attributes, self.target_attr, self.to_index)

        for state, partial_learning_set in zip(self.attributes[best_attribute], divided_learning_set):
            if not partial_learning_set:
                # fill it with most common value in the data set when partial data-set is empty
                leaf_value = cm.cal_most_common_value(self.learning_set, self.target_attr)
                self.children[state] = DecisionTree(name=leaf_value, target_attr=self.target_attr)
            else:
                next_attribute = self.attributes.copy()
                next_attribute.pop(best_attribute)
                self.children[state] = DecisionTree(partial_learning_set, next_attribute, self.target_attr,
                                                    self.to_index)
                self.children[state].build_tree()

    def check_data(self, test_data):
        if self.name in self.target_attr:
            return self.name

        return self.children[test_data[self.to_index[self.name]]].check_data(test_data)

    def pprint(self, indent=" "):
        if self.name in self.target_attr:
            print(indent, self.name)
            return

        print(indent, self.name)
        indent += '\t\t'

        for child in self.children:
            print(indent, child)
            self.children[child].pprint(indent + '\t\t')
