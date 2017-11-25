import sys

def decode(lines, sort_func=max):
    code = ''
    for i in range(len(lines[0])):
        letters = []
        for line in lines:
            letters.append(line[i])
        code = code + sort_func(set(letters), key=letters.count)
    return code

code = '''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''

#print(decode(code.split('\n'), sort_func=max))
#print(decode(code.split('\n'), sort_func=min))

def run(stdin):
    lines = stdin.splitlines()
    print(decode(lines, sort_func=max))
    print(decode(lines, sort_func=min))

if __name__ == "__main__":
    run(sys.stdin.read())
