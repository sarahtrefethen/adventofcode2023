'''
#Part 1

## Input 
    px{a<2006:qkq,m>2090:A,rfg}
    pv{a>1716:R,A}
    lnx{m>1548:A,A}
    rfg{s<537:gd,x>2440:R,A}
    qs{s>3448:A,lnx}
    qkq{x<1416:A,crn}
    crn{x>2662:A,R}
    in{s<1351:px,qqz}
    qqz{s>2770:qs,m<1801:hdj,R}
    gd{a>3333:R,R}
    hdj{m>838:A,pv}

    {x=787,m=2655,a=1222,s=2876}
    {x=1679,m=44,a=2067,s=496}
    {x=2036,m=264,a=79,s=2244}
    {x=2461,m=1339,a=466,s=291}
    {x=2127,m=1623,a=2188,s=1013}

## Description

the first section of the input is a series of workflows by which to assess
the elements in the second section of the input, which are parts. the outcome 
of applying a workflow to a part is either acceptance(A) regection(R) or 
moving on to another workflow. our goal is to add together all of the attribute
values (x,m,a, and s) of the accepted parts.

## Approach
Just parse the input and follow the steps. 
'''
x='x'
m='m'
a='a'
s='s'
GRTRT='>'
LESST='<'
ACCEPT = "A"
REJECT = "R"
ELSE = 'else'

with open('D19.txt', 'r') as file:
    [flows_blob, parts_blob] = file.read().split('\n\n')

def part1():
    workflows = {}
    for line in flows_blob.splitlines():
        [key, cases] = line.split('{')
        workflows[key] = [(ELSE, case) if ':' not in case else (case.split(':')[0][0], case.split(':')[0][1], int(case.split(':')[0][2:]),case.split(':')[1]) for case in cases.strip('}').split(',')]

    parts = []
    for line in parts_blob.splitlines():
        parts.append({elem.split('=')[0]:int(elem.split('=')[1]) for elem in line.strip("{").strip("}").split(',')})

    def process(part, step):
        for condition in step:
            if condition[0]==ELSE:
                return condition[1]
            if condition[1] == LESST and part[condition[0]] < condition[2]:
                return condition[3]
            if condition[1] == GRTRT and part[condition[0]] > condition[2]:
                return condition[3]
        pass

    accepted = []
    for part in parts:
        res = process(part, workflows['in'])
        while True:
            if res == ACCEPT:
                accepted.append(part)
                break
            if res == REJECT:
                break
            res = process(part, workflows[res])

    print(f'part 1: {sum([value for part in accepted for value in part.values()])}')

part1()
