def parse(text):
    markers = {}
    pointer = 0
    offsets = 0
    newtext = text
    while text.find('(', pointer) != -1:
        index = text.find('(', pointer)
        details = tuple(int(x) for x in text[index+1:text.find(')', index)].split('x'))
        markers[text.find('(', pointer) - offsets] = details
        newtext = newtext[:newtext.find('(', pointer)] + newtext[newtext.find(')', newtext.find('(',pointer)) + 1:]
        offsets += len(text[index:text.find(')', index) + 1])

        pointer = text.find('(', pointer) + details[0]


    return markers, newtext

def mutate(markers, text):
    print(markers)
    jump = 0
    for index, modifiers in markers.items():
        text = text[:index+jump] + text[index+jump:index+modifiers[0]+jump]*modifiers[1] + text[index+modifiers[0]+jump:]
        jump = modifiers[1]
    return text

# print(parse('A(2x2)BCD(2x2)EFG'))
# print(mutate(*parse('ADVENT')))
# print(mutate(*parse('A(1x5)BC')))
# print(mutate(*parse('(3x3)XYZ')))
# print(mutate(*parse('A(2x2)BCD(2x2)EFG')))
# print(mutate(*parse('(6x1)(1x3)A')))
# print(mutate(*parse('X(8x2)(3x3)ABCY')))

with open('inputs.txt') as f:
    line = f.readline()
    print(len(mutate(*parse(line)))-4)