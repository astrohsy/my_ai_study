import random

class Perceptron:
    def __init__(self, training_examples, N, yeta, number):
        self.training_exmaples = training_examples
        self.label_index = N
        self.N = N
        self.w = [random.uniform(0.0001, 0.0002) for i in range(N)]
        self.yeta = yeta
        self.number = number

    def train(self):
        for repeat in range(10):
            flag = False

            dw = [0 for i in range(self.N)]
            for example in self.training_exmaples:
                o = self.test(example)
                t = example[-1]
                tar = 0
                if t != self.number:
                    tar = -1
                else:
                    tar = 1

                for i in range(self.N):
                    dw[i] += self.yeta * (tar - o) * example[i]

            for i in range(self.N):
                self.w[i] += dw[i]

    def test(self, x):
        res = 0.0
        for i in range(self.N):
            res += x[i] * self.w[i]

        if res >= 0:
            return 1
        else:
            return -1
