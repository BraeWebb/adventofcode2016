import sys

def has_code(code, check, sublen):
    for i in range(len(code) - (sublen-1)):
        subcode = code[i:i+sublen]
        if check(subcode):
            return True
    return False

abba = lambda subcode: subcode[0] == subcode[3] and subcode[1] == subcode[2] and subcode[0] != subcode[1]
aba = lambda subcode: subcode[0] == subcode[2] and subcode[0] != subcode[1]

def support_tls(code):
    supports = False
    code = code.replace('[', '|').replace(']', '|')
    for i, subsec in enumerate(code.split('|')):
        if not i % 2:
            if has_code(subsec, abba, 4):
                supports = True
    for i, subsec in enumerate(code.split('|')):
        if i % 2:
            if has_code(subsec, abba, 4):
                supports = False
    return supports

#print(support_tls('abba[mnop]qrst'))
#print(support_tls('abcd[bddb]xyyx'))
#print(support_tls('aaaa[qwer]tyui'))
#print(support_tls('ioxxoj[asdfgh]zxcvbn'))

aba_return = lambda subcode: (subcode[0], subcode[1])

def find_code(code, check, sublen, returner):
    codes = []
    for i in range(len(code) - (sublen-1)):
        subcode = code[i:i+sublen]
        if check(subcode):
            codes.append(returner(subcode))
    return codes

def support_ssl(code):
    supports = False
    code = code.replace('[', '|').replace(']', '|')
    codes = []
    for i, subsec in enumerate(code.split('|')):
        if i % 2:
            if has_code(subsec, aba, 3):
                codes += find_code(subsec, aba, 3, aba_return)
    for i, subsec in enumerate(code.split('|')):
        if not i % 2:
            if has_code(subsec, aba, 3):
                found_codes = find_code(subsec, aba, 3, aba_return)
                for subcode in found_codes:
                    if tuple(reversed(subcode)) in codes:
                        return True
    return False

#print(has_code('aba', aba, 3))
#print(find_code('aba', aba, 3, aba_return))
#print(find_code('aaa[kek]eke', aba, 3, aba_return))
#print(has_code('abba', abba, 4))
#print(support_ssl('aaa[kek]eke'))

def run(stdin):
    print(sum(1 if support_tls(line) else 0 for line in stdin.splitlines()))
    print(sum(1 if support_ssl(line) else 0 for line in stdin.splitlines()))

if __name__ == "__main__":
    run(sys.stdin.read())
