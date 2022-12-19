class Rule:
    def __init__(self, input_set, expected_output):
        self.input_set = input_set
        self.expected_output = expected_output

    def eval(self, values):
        return [self.expected_output, min([values[name][variable] for name, variable in self.input_set.items()])]
