from collections import defaultdict

'''

## Input
example 1:
    broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a

example 2:
    broadcaster -> a
    %a -> inv, con
    &inv -> b
    %b -> con
    &con -> output 
'''

HIGH = True
LOW = False

class Module:
    def __init__(self, name: str):
        self.name = name
        self.outlets = []
        self.lows = 0
        self.highs = 0
    def add(self, new_outlet):
        self.outlets.append(new_outlet)
    def receive(self, source, pulse):
        if pulse == HIGH:
            # print (f'{self.name} receiving high')
            self.highs+=1
        if pulse == LOW:
            # print (f'{self.name} receiving low')
            self.lows+=1
    def send(self, *args):
        return False

class Broadcaster(Module):
    def send(self):
        # print('broadcast receiving low')
        # extra pulse sent from the button to the broadcast module
        self.lows+=1
        # print(f'sending: {[(outlet.name, self.name, LOW) for outlet in self.outlets]}')
        return [(outlet.name, self.name, LOW) for outlet in self.outlets]
        
    
class FlipFlop(Module):
    def __init__(self, name: str):
        self.name = name
        self.outlets = []
        self.on = False
        self.highs = 0
        self.lows = 0
        self.sendpulse = True
    def add(self, new_outlet):
        self.outlets.append(new_outlet)  
    def receive(self, source, pulse):
        if pulse == HIGH:
            self.highs +=1
            # print(f'{self.name} receiving high')
            self.sendpulse = False
        if pulse == LOW:
            self.lows +=1
            # print(f'{self.name} receiving low')
            
            self.on = not self.on
            self.pulse = HIGH if self.on else LOW
            self.sendpulse = True
    def send(self):
        # print(f'{self.name} sending')
        if self.sendpulse:
            return [(outlet.name, self.name, self.pulse) for outlet in self.outlets]
        return False

class Conjunction(Module):
    def __init__(self, name):
        self.outlets = []
        self.name = name
        self.receivers = {}
        self.highs = 0
        self.lows = 0
    def add(self, new_outlet):
        self.outlets.append(new_outlet)  
    def receive(self, source, pulse):
        if pulse == LOW:
            self.lows +=1
            # print(f'Conjunction {self.name} receiving low')
        if pulse == HIGH:
            self.highs +=1
            # print(f'Conjunction {self.name} receiving high')
        self.receivers[source] = pulse
    def send(self):
        # print(f'conjunction {self.name} sending')
        pulse = LOW
        for remembered_pulse in self.receivers.values():
            if remembered_pulse == LOW:
                pulse = HIGH
        pulse_sum = sum(self.receivers.values()) != len(self.receivers)
        return [(outlet.name, self.name, pulse) for outlet in self.outlets]
        


with open('D20.txt', 'r') as file:
    input = [line.split(' -> ') for line in file.read().splitlines()]

print(input)

modules = {}

# create all the modules we need
for line in input:
    type = line[0][0]
    name = line[0][1:]
    if type == '%':
        modules[name] = FlipFlop(name)
    elif type == '&':
        modules[name] = Conjunction(name)
    elif line[0] == 'broadcaster':
        modules[line[0]] = Broadcaster('broadcaster')
    else:
        modules[line[0]] = Module(line[0])

print(modules)

# connect them all up
for line in input:
    name = line[0][1:] if line[0] != 'broadcaster' else 'broadcaster'
    connections = line[1].split(', ')
    for conn_name in connections:
        if conn_name not in modules:
            modules[conn_name] = Module(conn_name)
        modules[name].add(modules[conn_name])
        if isinstance(modules[conn_name], Conjunction):
            modules[conn_name].receivers[name] = LOW

# for module in modules.values():
#     print(module.name)
#     print([o.name for o in module.outlets])

def part1():
    for i in range(1000):
        # print('*******************')
        queue = modules['broadcaster'].send()

        while len(queue):
            # print(f'queue: {queue}')
            (target, source, pulse) = queue.pop()
            modules[target].receive(source, pulse)
            if result := modules[target].send():
                queue = result + queue

    highs = 0
    lows = 0
    for module in modules.values():
        highs += module.highs
        lows += module.lows

    print(f'part 1: {highs * lows}')

part1()