from controller.Controller import Controller
from model.Description import Description
from model.Rule import Rule


def write(fileName, content):
    f = open(fileName, 'w')
    for line in content:
        f.write(line)
        print(line)
        f.write("\n")
    f.close()


def trapezoid(a, b, c, d):
    return lambda x: max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))


def triangle(a, b, c):
    return trapezoid(a, b, b, c)


def inverse_line(a, b):
    return lambda x: x * (b - a) + a


def inverse_triangle(a, b, c):
    return lambda x: (inverse_line(a, b)(x) + inverse_line(c, b)(x)) / 2


if __name__ == '__main__':
    temperature = Description()
    capacity = Description()
    power = Description()
    rules = []

    temperature.save('cold', trapezoid(-100, 20, 30, 50))
    temperature.save('cool', triangle(30, 50, 70))
    temperature.save('moderate', triangle(60, 70, 80))
    temperature.save('hot', triangle(70, 90, 110))
    temperature.save('very hot', trapezoid(90, 110, 120, 100))

    capacity.save('small', triangle(-100, 0, 5))
    capacity.save('medium', triangle(3, 5, 7))
    capacity.save('high', triangle(5, 10, 100))

    power.save('small', triangle(-100, 0, 10), inverse_line(10, 0))
    power.save('medium', triangle(5, 10, 15), inverse_triangle(5, 10, 15))
    power.save('high', triangle(10, 20, 100), inverse_line(10, 20))

    rules.append(Rule({'temperature': 'cold', 'capacity': 'small'},
                      {'power': 'small'}))
    rules.append(Rule({'temperature': 'cold', 'capacity': 'medium'},
                      {'power': 'medium'}))
    rules.append(Rule({'temperature': 'cold', 'capacity': 'high'},
                      {'power': 'high'}))

    rules.append(Rule({'temperature': 'cool', 'capacity': 'small'},
                      {'power': 'small'}))
    rules.append(Rule({'temperature': 'cool', 'capacity': 'medium'},
                      {'power': 'medium'}))
    rules.append(Rule({'temperature': 'cool', 'capacity': 'high'},
                      {'power': 'high'}))

    rules.append(Rule({'temperature': 'moderate', 'capacity': 'small'},
                      {'power': 'small'}))
    rules.append(Rule({'temperature': 'moderate', 'capacity': 'medium'},
                      {'power': 'small'}))
    rules.append(Rule({'temperature': 'moderate', 'capacity': 'high'},
                      {'power': 'small'}))

    rules.append(Rule({'temperature': 'hot', 'capacity': 'small'},
                      {'power': 'small'}))
    rules.append(Rule({'temperature': 'hot', 'capacity': 'medium'},
                      {'power': 'small'}))
    rules.append(Rule({'temperature': 'hot', 'capacity': 'high'},
                      {'power': 'small'}))

    rules.append(Rule({'temperature': 'very hot', 'capacity': 'small'},
                      {'power': 'small'}))
    rules.append(Rule({'temperature': 'very hot', 'capacity': 'medium'},
                      {'power': 'small'}))
    rules.append(Rule({'temperature': 'very hot', 'capacity': 'high'},
                      {'power': 'small'}))

    ctrl = Controller(temperature, capacity, power, rules)

    outputs = [ctrl.compute({'capacity': 2, 'temperature': 30}), ctrl.compute({'capacity': 4, 'temperature': 100}),
               ctrl.compute({'capacity': 5, 'temperature': 60}), ctrl.compute({'capacity': 9, 'temperature': 110}),
               ctrl.compute({'capacity': 2, 'temperature': 110}), ctrl.compute({'capacity': 10, 'temperature': 20}),ctrl.compute({'capacity': 5, 'temperature': 100})]

    write("../output.txt", outputs)

