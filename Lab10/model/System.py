
class System:
    def __init__(self, rules):
        self.input_variables = {}
        self.output_variable = None
        self.rules = rules

    def save(self, name, description, available=False):
        if available:
            self.output_variable = description
        else:
            self.input_variables[name] = description

    def compute_rules(self, values):
        return [rule.eval(values) for rule in self.rules if rule.eval(values)[1] != 0]

    def compute_linguistic_variables(self, values):
        return {name: self.input_variables[name].fuzzify(values[name]) for name, value in values.items()}

    def compute_all(self, values):
        linguistic_values = self.compute_linguistic_variables(values)
        rule_values = self.compute_rules(linguistic_values)

        output_values = [(list(rule[0].values())[0], rule[1]) for rule in rule_values]

        total, sum = 0, 0

        for output in output_values:
            sum += output[1]
            total += self.output_variable.defuzzify(*output) * output[1]

        return total / sum
