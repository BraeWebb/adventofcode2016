import re

class Output(object):
    def __init__(self, id):
        self.chips = []
        self.id = id

    def recieve(self, microchip):
        self.chips.append(microchip)

    def update(self, recurr=False):
        pass

    def get_chips(self):
        return self.chips

    def __contains__(self, item):
        return item in self.chips

    def __str__(self):
        return 'Output #{} with chips {}'.format(self.id, self.chips)

    def __repr__(self):
        return 'Output({}, {})'.format(self.id, self.chips)

    def get_id(self):
        return self.id

class Bot(Output):
    def __init__(self, id, high=None, low=None):
        self.chips = []
        self.id = id
        self.low = low
        self.high = high

    def set_low(self, low):
        self.low = low

    def set_high(self, high):
        self.high = high

    def recieve(self, microchip):
        self.chips.append(microchip)
        # self.update() #auto-updating

    def update(self, recurr=False):
        if len(self.chips) >= 2:
            self.pass_on()
            if recurr:
                self.low.update(recurr=True)
                self.high.update(recurr=True)

    def pass_on(self):
        chips = sorted(self.chips)
        if self.low and self.high:
            self.low.recieve(chips[0])
            self.high.recieve(chips[1])
            self.chips = []

    def __str__(self):
        return 'Bot #{} with chips {}'.format(self.id, self.chips)

    def __repr__(self):
        return 'Bot({}, low={}, high={}, {})'.format(self.id, self.low, self.high, self.chips)

    def get_id(self):
        return self.id


class Factory(object):
    def __init__(self):
        self.bots = {}
        self.outputs = {}

    def __getitem__(self, item):
        if item.__class__ == Bot:
            if self.bots.get(item.get_id(), False):
                return self.bots[item.get_id()]
            else:
                self.bots[item.get_id()] = item
                return item
        else:
            if self.outputs.get(item.get_id(), False):
                return self.outputs[item.get_id()]
            else:
                self.outputs[item.get_id()] = item
                return item

    def __contains__(self, item):
        if item.__class__ == Bot:
            return item.get_id() in self.bots
        else:
            return item.get_id() in self.outputs

    def __setitem__(self, key, value):
        if value.__class__ == Bot:
            self.bots[key] = value
        else:
            self.outputs[key] = value

    def __iter__(self):
        for bot in self.bots.values():
            yield bot
        for output in self.outputs.values():
            yield output

def find_responsible(factory, value1, value2):
    # keep updating each bot until one has both chips
    found = False
    while not found:
        for bot in factory:
            if value1 in bot and value2 in bot:
                found = bot
            bot.update()
    return found


def get_outputs(factory):
    for bot in factory:
        bot.update(recurr=True)

    outputs = {}
    for bot in factory:
        if bot.__class__ == Output:
            outputs[bot.get_id()] = bot.get_chips()
    return outputs

def generate_factory(commands):
    # load the factory bots from the given commands
    factory = Factory()
    for line in commands:
        if line[:5] == 'value':
            bot_id = int(re.search('bot (.*)', line).group(1))
            chip = int(re.search('value (.*) goes', line).group(1))
            bot = Bot(bot_id)
            factory[bot].recieve(chip)
        else:
            bot_id = int(re.search('bot (.*) gives', line).group(1))
            low_type = Bot if re.search('to bot (.*) and', line) else Output
            high_type = Bot if re.search('to bot (.*)', line) else Output
            low = factory[low_type(int(re.search('to (.*) (.*) and', line).group(2)))]
            high = factory[high_type(int(re.search('to (.*) (.*)', line).group(2)))]

            bot = Bot(bot_id)
            factory[bot].set_low(low)
            factory[bot].set_high(high)
    return factory

with open('inputs.txt') as f:
    # commands = '''value 5 goes to bot 2
    # bot 2 gives low to bot 1 and high to bot 0
    # value 3 goes to bot 1
    # bot 1 gives low to output 1 and high to bot 0
    # bot 0 gives low to output 2 and high to output 0
    # value 2 goes to bot 2'''.split('\n')
    commands = f.read().splitlines()
    print(find_responsible(generate_factory(commands), 17, 61))
    outputs = get_outputs(generate_factory(commands))
    product = 1
    for i in range(3):
        product *= sum(outputs[i])
    print(product)