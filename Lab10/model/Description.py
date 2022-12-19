
class Description:
    def __init__(self):
        self.linguistic_variables = {}
        self.inverse = {}

    def save(self, name, function, inverse=None):
        self.linguistic_variables[name] = function
        self.inverse[name] = inverse

    def fuzzify(self, function_value):
        return {name: function(function_value) for name, function in self.linguistic_variables.items()}

    def defuzzify(self, name, function_value):
        return self.inverse[name](function_value)
