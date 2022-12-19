from model.System import System

class Controller:
    def __init__(self, temperature, capacity, power, rules):
        self.system = System(rules)
        self.system.save('temperature', temperature)
        self.system.save('capacity', capacity)
        self.system.save('power', power, available=True)

    def compute(self, inputs):
        return "Capacity: " + str(inputs['capacity']) + \
               " and temperature: " + str(inputs['temperature']) + \
               " will yield a consumption power of: " + str(self.system.compute_all(inputs))
